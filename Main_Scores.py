from Utils import bad_return_code
from flask import Flask, request, render_template
from Utils import scores_file

app = Flask(__name__)

@app.route('/', methods=['GET','POST','DELETE'])
def show_score():
    if request.method == 'GET':
        try:
            scores = open(scores_file , 'r').read()
            return render_template('scores.html', var1=scores)
        except:
            return render_template('error.html', ERROR=bad_return_code)
    else:
        return render_template('error.html', ERROR=bad_return_code)
app.run(host="0.0.0.0", port=5001, debug=True)

