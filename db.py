from sqlalchemy import exists

from data import db_session
from data.users import User
from data.vidiotours import VidioTour, TYPE_VIDIO2D, TYPE_VIDIO360
from data.questtours import QuestTour
from data.tests import Test
import json

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
    obj.type_vidio = qwargs.get("type_vidio")

    db_sess.add(obj)
    db_sess.commit()
    return obj


{
    "title": "title",
    "description": "description",
    "title_image": "title_image",
    "resource": "resource",
    "type_vidio": "TYPE_VIDIO2D = 2; TYPE_VIDIO360 = 3"
}


def create_test(db_sess, **qwargs) -> Test:
    obj = Test()

    obj.title = qwargs.get("title")
    obj.task = qwargs.get("task")
    obj.quest_tour_id = qwargs.get("quest_tour_id")

    db_sess.add(obj)
    db_sess.commit()
    return obj


def _create_tests(data_json):
    db_sess = db_session.create_session()
    for d in data_json:
        data = create_test(db_sess, **d)
    print("create_test:", data)
    return {"id": data.id}


def _create_questtours(data_json):
    db_sess = db_session.create_session()
    data = []
    for d in data_json:
        data.append(create_questtour(db_sess, **d).id)
    print("create_questtours:", data)
    return {"ids": data}


def _create_vidiotours(data_json):
    db_sess = db_session.create_session()
    data = []
    for d in data_json:
        data.append(create_vidiotour(db_sess, **d).id)
    print("_create_vidiotours:", data)
    return {"ids": data}


{
    "title": "title",
    "task": "task json",
    "quest_tour_id": "quest_tour_id"
}


def create_questtour(db_sess, **qwargs) -> QuestTour:
    obj = QuestTour()

    obj.title = qwargs.get("title")
    obj.description = qwargs.get("description")
    obj.title_image = qwargs.get("title_image")
    obj.test = qwargs.get("test")

    db_sess.add(obj)
    db_sess.commit()
    return obj


{
    "title": "title",
    "description": "description",
    "title_image": "title_image"
}


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


def upload_local():
    with open('json/tests.json', 'r', encoding='cp1251') as f:  # открыли файл с данными
        text = json.load(f)  # загнали все, что получилось в переменную
        print(text)
        _create_tests(text)

    with open('json/qtours.json', 'r', encoding='cp1251') as f:  # открыли файл с данными
        text = json.load(f)  # загнали все, что получилось в переменную
        print(text)
        _create_questtours(text)

    with open('json/vtours.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        text = json.load(f)  # загнали все, что получилось в переменную
        print(text)
        _create_vidiotours(text)


def main():
    db_session.global_init("db/gideTMN55.db")
    upload_local()


if __name__ == '__main__':
    main()
