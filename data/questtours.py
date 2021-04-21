import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class QuestTour(SqlAlchemyBase):
    __tablename__ = 'questtours'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title_image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    tests = orm.relation("Test", back_populates='quest_tour')

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def __repr__(self):
        return f"<questtour> {self.title}, {self.created_date}"

    def get_info(self):
        d = {"id": self.id,
             "title": self.title,
             "description": self.description,
             "title_image": self.title_image,
             "tests": [test.id for test in self.tests]}
        return d
