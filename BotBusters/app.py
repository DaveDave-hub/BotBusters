import flask
from flask import Flask, render_template
from twitterBot import get_factors
app = Flask(__name__)

def likelihood(percentage):
    if percentage <= 15:
        return '<span class="has-text-info">Not a bot</span>'
    elif percentage > 15 and percentage <= 40:
        return '<span class="has-text-info">Most likely not a bot</span>'
    elif percentage > 40 and percentage <= 59:
        return '<span class="has-text-info">Hard to verify</span>'
    elif percentage > 59 and percentage <= 84:
        return '<span class="has-text-info">Most likely bot</span>'
    elif percentage > 84 and percentage <= 100:
        return '<span class="has-text-info">Bot</span>'

@app.route('/')
def index():  # put application's code here
    return flask.render_template('index.html')

@app.route('/verify', methods = ['GET', 'POST'])
def verify():
    username = flask.request.form['username']
    message_for_user = f'Verification of the user {username} '

    if get_factors(username) == 'User not found':
        verification =[f'User {username} not found']
    else:
        verification = [likelihood(get_factors(username)),
                        f'Probability of being a bot: {get_factors(username)}']

    return flask.render_template('index.html', prediction = verification[0], probability = verification[1], message_for_user = message_for_user)

if __name__ == '__main__':
    app.run()
