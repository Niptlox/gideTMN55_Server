import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Test(SqlAlchemyBase):
    __tablename__ = 'tests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    task = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    quest_tour_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey("questtours.id"))
    quest_tour = orm.relation('QuestTour')

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def __repr__(self):
        return f"<Test> {self.title}, {self.created_date}"

    def get_info(self):
        d = {"id": self.id,
             "title": self.title,
             "task": self.task,
             "quest_tour_id": self.quest_tour_id}
        return d
