
from sqlalchemy import exists

from data import db_session
from data.users import User
from data.vidiotours import VidioTour
from data.questtours import QuestTour
from data.tests import Test
import datetime

ERR_EMAIL = -10
OUT_SUCCESS = 1


def add_user(db_sess, **qwargs) -> User:
    email = qwargs.get("email").lower()
    if email is None or email_exists(db_sess, email):
        return ERR_EMAIL
    # db_sess = db_session.create_session()
    user = User()
    user.name = qwargs.get("name")
    user.surname = qwargs.get("surname")
    user.email = email
    user.set_password(qwargs.get('password'))
    user.status = qwargs.get("status")
    db_sess.add(user)
    db_sess.commit()
    return User


def create_vidiotour(db_sess, **qwargs) -> VidioTour:
    obj = VidioTour()

    obj.title = qwargs.get("title")
    obj.description = qwargs.get("description")
    obj.title_image = qwargs.get("title_image")
    obj.resource = qwargs.get("resource")

    db_sess.add(obj)
    db_sess.commit()
    return obj


def create_test(db_sess, **qwargs) -> Test:
    obj = Test()

    obj.title = qwargs.get("title")
    obj.task = qwargs.get("task")
    obj.quest_tour = qwargs.get("quest_tour")

    db_sess.add(obj)
    db_sess.commit()
    return obj


def create_questtour(db_sess, **qwargs) -> QuestTour:
    obj = QuestTour()

    obj.title = qwargs.get("title")
    obj.description = qwargs.get("description")
    obj.test = qwargs.get("test")

    db_sess.add(obj)
    db_sess.commit()
    return obj


def get_questtours(db_sess):
    tours = []
    for tour in db_sess.query(QuestTour).all():
        tours.append(tour.get_info())
    return tours


def get_vidiotours(db_sess):
    tours = []
    for tour in db_sess.query(VidioTour).all():
        tours.append(tour.get_info())
    return tours


def get_tests(db_sess, tour_id):
    tests = []
    db_tests = db_sess.query(Test).filter(Test.quest_tour_id == tour_id).all()
    for test in db_tests:
        tests.append(test.get_info())
    return tests


def email_exists(db_sess, email: str) -> bool:
    # db_sess = db_session.create_session()
    is_exists = db_sess.query(exists().where(User.email == email)).scalar()
    return is_exists



def main():
    db_session.global_init("db/gideTMN55.db")



if __name__ == '__main__':
    main()
