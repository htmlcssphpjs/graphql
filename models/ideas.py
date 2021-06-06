import sqlalchemy as sa
from .db_session import SqlAlchemyBase

class Idea(SqlAlchemyBase):
    __tablename__ = 'ideas'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    pitch = sa.Column(sa.Integer, autoincrement=True, nullable=True)
    descriptions = sa.Column(sa.String, nullable=True)
    media = sa.Column(sa.Integer, autoincrement=True)
    jobs = sa.Column(sa.Integer, autoincrement=True, nullable=True)
    team = sa.Column(sa.Integer, autoincrement=True, nullable=True)
    roadmap = sa.Column(sa.Integer, autoincrement=True)
