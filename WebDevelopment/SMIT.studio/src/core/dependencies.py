from src.database.app import SQL


def sql_session():
    db = SQL.session()
    try:
        yield db
    finally:
        db.close()
