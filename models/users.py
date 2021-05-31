import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    fullname = sa.Column(sa.Integer, autoincrement=True)
    username = sa.Column(sa.String, nullable=True)
    mail = sa.Column(sa.Integer, autoincrement=True)
    hashed_password = sa.Column(sa.Integer, autoincrement=True)
    resume = sa.Column(sa.Integer, autoincrement=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "fullname": self.fullname,
            "username": self.username,
            "mail": self.mail,
            "resume": self.resume
        }
