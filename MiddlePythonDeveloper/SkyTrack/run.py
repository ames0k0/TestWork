from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from src.sqldb.database import SessionLocal, engine
from src.sqldb.models import Base
from src.sqldb.schemas import OrderItem
from src.backend import crud


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_sqldb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/{user_id}")
def get_user_data(user_id: int, db: Session = Depends(get_sqldb)):
    """Получение данных пользователя (имя, адрес эл. Почты и т.п.);
    """
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        # serializer ??
        # return {status_code: 400, message: User not found}
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@app.get("/users/{user_id}/orders")
def get_user_orders(user_id: int, db: Session = Depends(get_sqldb)):
    """Просмотр истории заказов пользователя;
    """
    return crud.get_user_orders(db, user_id)


@app.post("/users/{user_id}/order")
def create_new_order(user_id: int, order_items: OrderItem, db: Session = Depends(get_sqldb)):
    """Добавление нового заказа (N книг каждая из которых в M количестве);
    """
    return crud.create_new_order(db, user_id, order_items)


@app.get("/orders/{order_id}")
def get_order_data(order_id: int, db: Session = Depends(get_sqldb)):
    """Получение данных определенного заказа
    """
    return crud.get_order_data_by_id(db, order_id)
