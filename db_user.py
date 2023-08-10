from sqlalchemy.orm.session import Session
from Schema import UserBase
from models import DBUser
from hash import Hash
import pandas


def create_user(db:Session,request:UserBase):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt0(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db:Session):
    return db.query(DBUser).all()