import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class VidioTour(SqlAlchemyBase):
    __tablename__ = 'vidiotours'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title_image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    resource = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def __repr__(self):
        return f"<vidiotour> {self.title}, {self.created_date}"

    def get_info(self):
        d = {"id": self.id,
             "title": self.title,
             "description": self.description,
             "title_image": self.title_image,
             "resource": self.resource}
        return d
