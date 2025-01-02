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
        in_top_transactions_limit = len(
            top_transactions
        ) <= config.settings.TOP_TRANSACTIONS_ANALYSIS_LIMIT

        for idx, top_transaction in enumerate(
            top_transactions[:config.settings.TOP_TRANSACTIONS_ANALYSIS_LIMIT]
        ):
            if transaction.amount > top_transaction.amount:
                top_transactions.insert(idx, transaction)
                break
        else:
            # len -> 4
            # amount=3, amount=3
            if in_top_transactions_limit:
                top_transactions.append(transaction)

        # Deleting the last added transaction
        if not in_top_transactions_limit:
            top_transactions.pop()

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
