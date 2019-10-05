import os
import requests
import json
from flask import *

from src.plot import Graph
from src.weight import Weight
from src.tweet import Tweet
from src.auth import Auth
from config import app, db

objs = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = 'パスワードが違うよ。'
        return render_template('index2.html', msg=msg)
    else:
        return render_template('index.html')

@app.route('/confirm/', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        password = request.form['password']
        if password != Auth.query.first().password:
            return redirect(request.url[-1], code=307)

        t_weight = request.form['weight']
        weight = Weight(t_weight)
        objs.append(weight)

        try:
            weight_msg = weight.format_weight()
        except:
            return render_template('exist.html')
        else:
            return render_template('confirm.html', weight_msg=weight_msg)
    else:
        return redirect(request.url[-1])

@app.route('/success/', methods=['GET', 'POST'])
def success():
    if len(objs) == 0:
        return redirect(request.url[-1])

    if request.method == 'POST':
        weight = objs[0]
        try:
            msg = request.form['msg']
            weight.update_db()
            Graph().plot_graph()
            Tweet().tweet(msg, '/tmp/weight.png')
            return render_template('success.html')
        except Exception as e:
            weight.delete_rec()
            return render_template('error', error_msg=e)

@app.route('/error/', methods=['GET'])
def error():
    return render_template('error.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
