import flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return flask.render_template('index.html')

@app.route('/verify', methods = ['GET', 'POST'])
def verify():
    username = flask.request.form['username']
    message_for_user = f'Verification of the user @{username} '

if __name__ == '__main__':
    app.run()
