from flask import Flask
# from forms.loginform import LoginForm
# from forms.registerform import RegisterForm
import db
import json

from flask import request

db.main()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwekwqkJDHASIqwop'


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.args
    print(data)
    return str(data)


@app.route('/questtours', methods=['GET', 'POST'])
def _questtours():
    # data = request.data
    db_sess = db.db_session.create_session()
    data = db.get_questtours(db_sess)
    print("questtours", data)
    return json.dumps(data)


@app.route('/vidiotours', methods=['GET', 'POST'])
def _vidiotours():
    # data = request.data
    db_sess = db.db_session.create_session()
    data = db.get_vidiotours(db_sess)
    print("vidiotours", data)
    return json.dumps(data)


@app.route('/tests', methods=['GET', 'POST'])
def _tests():
    tour_id = request.data["tour_id"]
    db_sess = db.db_session.create_session()
    data = db.get_tests(db_sess, tour_id)
    print("tests", data)
    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=False)
