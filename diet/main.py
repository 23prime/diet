from diet.config import app
import diet.view


def main():
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
