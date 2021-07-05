from flask import Flask, request, render_template, jsonify
from Mysql_Pack.Mysql_connect import MysqlConnector
from config import MY_SQL_CRED

app = Flask(__name__, template_folder='Templates')
db = MysqlConnector(**MY_SQL_CRED)


@app.route('/scores', methods=['POST', 'GET'])
def write_scores():
    if request.method == 'POST':
        data = request.json
        user = data.get('user', None)
        score = data.get('score', None)
        print(user, score)
        db.set_score(user, score)
        return jsonify(data), 201
    if request.method == 'GET':
        user = request.args.get('user')
        show_score = db.get_score(user)
        print(show_score)
        return show_score


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
