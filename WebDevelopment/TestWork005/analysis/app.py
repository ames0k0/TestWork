from collections import namedtuple

from restapi import config, connections, crud


# lifespan
connections.Redis.initialize()
connections.Celery.initialize()
connections.Postgres.initialize()

app = connections.Celery.ins


Transaction = namedtuple(
    'Transaction',
    (
        'transaction_id',
        'amount',
    )
)


@app.task(name="update_transactions_analysis")
def update_transactions_analysis(*, api_key: str) -> None:
    """Analyses the transactions for the given `api_key`

    Update the analysed cache
    """
    cache = crud.Redis.get(api_key=api_key)
    transactions = crud.Postgres.get_transactions_to_analyze(
        api_key=api_key,
        analysed_transaction_id=cache['analysed_transaction_id'],
        session=connections.Postgres.get_scoped_session(),
    )
    if not transactions:
        return

    top_transactions: list = []
    if cache['top_transactions']:
        # dict -> nt
        top_transactions = [
            Transaction(t['transaction_id'], t['amount'])
            for t in cache['top_transactions']
        ]

    for transaction in transactions:
        cache['total_transactions_amount'] += transaction.amount

        for idx, top_transaction in enumerate(
            top_transactions[:config.settings.TOP_TRANSACTIONS_ANALYSIS_LIMIT]
        ):
            if transaction.amount > top_transaction.amount:
                top_transactions.insert(idx, transaction)
                if len(
                    top_transactions
                ) > config.settings.TOP_TRANSACTIONS_ANALYSIS_LIMIT:
                    top_transactions.pop()
                break
        else:
            if len(
                top_transactions
            ) < config.settings.TOP_TRANSACTIONS_ANALYSIS_LIMIT:
                top_transactions.append(transaction)

    cache['analysed_transaction_id'] = transactions[-1].transaction_id
    # +1
    cache['total_transactions'] += len(transactions)
    # amount=0
    if cache['total_transactions_amount']:
        cache['average_transaction_amount'] = round(
            cache['average_transaction_amount'] / cache['total_transactions'],
            2,
        )

    cache['top_transactions'] = [
        {
            'transaction_id': t.transaction_id,
            'amount': t.amount,
        } for t in top_transactions
    ]

    crud.Redis.set(
        api_key=api_key,
        transactions_analysis=cache,
    )
