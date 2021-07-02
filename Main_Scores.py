from Utils import bad_return_code
from flask import Flask, request, render_template, jsonify
from Utils import scores_file , db_connect
import requests

app = Flask(__name__,template_folder='Templates')


@app.route('/scores',methods=['POST','GET'])
def write_scores():
    if request.method == 'POST':
        data = request.json
        user = data.get('user',None)
        score = data.get('score',None)
        return jsonify(data), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

