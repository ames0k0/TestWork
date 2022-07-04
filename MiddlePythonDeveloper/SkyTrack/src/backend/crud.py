import json

from sqlalchemy.orm import Session

from ..sqldb.models import User, Order, OrderItem


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_orders(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).order_by(Order.id.desc()).all()


def create_new_order(db: Session, user_id: int, order_items: OrderItem):
    order = Order(user_id=user_id)
    db.add(order)
    db.commit()

    for book in order_items.books:
        order_item = OrderItem(order_id=order.id,
                               book_id=book.id, book_quantity=book.quantity,
                               shop_id=book.shop_id)
        db.add(order_item)

    db.commit()
    

def get_order_data_by_id(db: Session, order_id: int):
    return db.query(OrderItem).filter(OrderItem.order_id == order_id).order_by(OrderItem.id).all()
