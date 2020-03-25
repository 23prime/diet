import diet.view
from diet.config import app


def main():
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
