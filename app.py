from flask import Flask
# from forms.loginform import LoginForm
# from forms.registerform import RegisterForm
import db
import json

from flask import request
from flask import send_from_directory
from flask import send_file


db.main()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwekwqkJDHASIqwop'


@app.route('/download/database')
def download():
    # return "ppp"
    return send_file("db/gideTMN55.db", as_attachment=True, attachment_filename="gideTMN55.db", )
    # return send_from_directory('db/', "gideTMN55.db")


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.args
    data_json = request.json
    print("/////////")
    print(data)
    print(data_json)
    return str(data_json)


@app.route('/hi', methods=['GET', 'POST'])
def _hi():
    return 'Hi angry world! '


@app.route('/questtours', methods=['GET', 'POST'])
def _questtours():
    # data = request.data
    db_sess = db.db_session.create_session()
    data = db.get_questtours(db_sess)
    print("questtours:", data)
    return json.dumps(data)


@app.route('/create_questtour', methods=['GET', 'POST'])
def _create_questtour():
    data_json = request.json
    db_sess = db.db_session.create_session()
    data = db.create_questtour(db_sess, **data_json)
    print("create_questtour:", data)
    return json.dumps({"id": data.id})


@app.route('/create_questtours', methods=['GET', 'POST'])
def _create_questtours():
    data_json = request.json
    return json.dumps(db._create_tests(data_json))


@app.route('/create_test', methods=['GET', 'POST'])
def _create_test():
    data_json = request.json
    db_sess = db.db_session.create_session()
    data = db.create_test(db_sess, **data_json)
    print("create_test:", data)
    return json.dumps({"id": data.id})


@app.route('/create_tests', methods=['GET', 'POST'])
def _create_tests():
    data_json = request.json
    return json.dumps(db._create_tests(data_json))


@app.route('/create_vidiotour', methods=['GET', 'POST'])
def _create_vidiotour():
    data_json = request.json
    db_sess = db.db_session.create_session()
    data = db.create_vidiotour(db_sess, **data_json)
    print("create_vidiotour:", data)
    return json.dumps({"id": data.id})


@app.route('/create_vidiotours', methods=['GET', 'POST'])
def _create_vidiotours():
    data_json = request.json
    return json.dumps(db._create_vidiotours(data_json))


@app.route('/vidiotours', methods=['GET', 'POST'])
def _vidiotours():
    db_sess = db.db_session.create_session()
    data = db.get_vidiotours(db_sess)
    print("vidiotours:", data)
    return json.dumps(data)


@app.route('/tests', methods=['GET', 'POST'])
def _tests():
    tour_id = request.args["tour_id"]
    db_sess = db.db_session.create_session()
    data = db.get_tests(db_sess, tour_id)
    print("tests", data)
    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=False)
