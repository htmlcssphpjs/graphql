import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    pitch = sa.Column(sa.Integer, autoincrement=True, nullable=True)
    picture = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.Integer, autoincrement=True)
    skills = sa.Column(sa.Integer, autoincrement=True, nullable=True)
    roadmap = sa.Column(sa.Integer, autoincrement=True, nullable=True)
    hashed_password = sa.Column(sa.Integer, autoincrement=True)
