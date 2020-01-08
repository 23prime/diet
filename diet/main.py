import os
import requests
import json
from flask import *

from diet.plot import Graph
from diet.weight import Weight
from diet.tweet import Tweet
from diet.auth import Auth
from diet.config import app, db

weight = None

@app.route('/', methods=['GET', 'POST'])
def root():
    return redirect('/diet/')

@app.route('/diet/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = 'パスワードが違うよ。'
        return render_template('index2.html', msg=msg)
    else:
        return render_template('index.html')

@app.route('/diet/confirm/', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        password = request.form['password']
        if password != Auth.query.first().password:
            return redirect('/diet/', code=307)

        t_weight = request.form['weight']
        global weight
        weight = Weight(t_weight)

        try:
            weight_msg = weight.format_weight()
        except:
            return render_template('exist.html')
        else:
            return render_template('confirm.html', weight_msg=weight_msg)
    else:
        return redirect('/diet/')

@app.route('/diet/success/', methods=['GET', 'POST'])
def success():
    global weight

    if weight is None:
        return redirect('/diet/')

    if request.method == 'POST':
        try:
            msg = request.form['msg']
            weight.update_db()
            Graph().plot_graph()
            Tweet().tweet(msg, '/tmp/weight.png')
            weight = None
            return render_template('success.html')
        except Exception as e:
            weight.delete_rec()
            return render_template('error', error_msg=e)

@app.route('/diet/error/', methods=['GET'])
def error():
    return render_template('error.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

def main():
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
