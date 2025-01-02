from restapi import config, connections, crud


# lifespan
connections.Redis.initialize()
connections.Celery.initialize()
connections.Postgres.initialize()

app = connections.Celery.ins


@app.task(name="update_transactions_analysis")
def update_transactions_analysis(*, api_key: str) -> None:
    """Analyses the transactions for the given `api_key`

    Update the analysed cache
    """
    total_transactions_amount: float = 0.0
    top_transactions: list = []

    transactions = crud.Postgres.get_all(
        api_key=api_key,
        session=connections.Postgres.get_scoped_session(),
    )
    if not transactions:
        return

    for transaction in transactions:
        total_transactions_amount += transaction.amount

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

    crud.Redis.set(
        api_key=api_key,
        transactions_analysis={
            "total_transactions": len(transactions),
            "average_transaction_amount": round(
                total_transactions_amount / len(transactions),
                2,
            ),
            "top_transactions": [
                {
                    "transaction_id": t.transaction_id,
                    "amount": t.amount,
                }  for t in top_transactions
            ],
        },
    )
