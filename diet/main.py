import os
import requests
import json
from flask import *

from diet.plot import Graph
from diet.weight import *
from diet.tweet import Tweet
from diet.auth import Auth
from diet.config import app, db

weight = None
graph_path ='/app/diet/static/weight.png'

@app.route('/', methods=['GET', 'POST'])
def root():
    return redirect('/diet/')

@app.route('/diet/', methods=['GET', 'POST'])
def index():
    global graph_path

    if request.method == 'POST':
        msg = 'パスワードが違うよ。'
        return render_template('index2.html', msg=msg)
    else:
        Graph().plot_graph(graph_path)
        return render_template('index.html')

@app.route('/diet/confirm/', methods=['GET', 'POST'])
def confirm():
    global weight
    weight = None

    if request.method == 'POST':
        password = request.form['password']

        if password != Auth.query.first().password:
            return redirect('/diet/', code=307)

        t_weight = request.form['weight']
        weight = Weight(t_weight)

        try:
            weight_msg = weight.format_weight()
        except WeightsAlreadyExistException:
            return render_template('exist.html')
        else:
            return render_template('confirm.html', weight_msg=weight_msg)
    else:
        return redirect('/diet/')

@app.route('/diet/success/', methods=['GET', 'POST'])
def success():
    global weight
    global graph_path

    if weight is None:
        return redirect('/diet/')

    if request.method == 'POST':
        try:
            weight.update_db()
            weight = None
            msg = request.form['msg']
            Graph().plot_graph(graph_path)
            Tweet().tweet(msg, graph_path)
            return render_template('success.html')
        except WeightsDBException as e:
            return render_template('error', error_msg=e)
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
