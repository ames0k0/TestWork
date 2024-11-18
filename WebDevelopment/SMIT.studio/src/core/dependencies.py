from src.database.app import get_session


def get_sqldb():
    db = get_session()
    try:
        yield db
    finally:
        db.close()
