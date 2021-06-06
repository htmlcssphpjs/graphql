import sqlalchemy as sa
from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer,
                   primary_key=True)
    name = sa.Column(sa.String)
    pitch = sa.Column(sa.Integer, nullable=True)
    picture = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.Integer)
    skills = sa.Column(sa.Integer, nullable=True)
    roadmap = sa.Column(sa.Integer, nullable=True)
    hashed_password = sa.Column(sa.Integer, autoincrement=True)
