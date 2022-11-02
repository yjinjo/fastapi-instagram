from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DBUser


def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Since id is auto_increment, we'll get the ID to our new user.
    return new_user


def get_all_users(db: Session):
    return db.query(DBUser).all()


def get_user(db: Session, id: int):
    # Handle any exception
    return db.query(DBUser).filter(DBUser.id == id).first()


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id)
    # Handle any exception
    user.update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    # Handle any exception
    db.delete(user)
    db.commit()

    return 'ok'
