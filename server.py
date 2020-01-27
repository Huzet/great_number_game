from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)

app.secret_key = 'password'


@app.route('/')
def home():
    if "random" not in session:
        session['random'] = random.randint(1, 100)
    print(session['random'])

    game_info = {
        "message": None,
        "css": None,
    }

    if 'guess' not in session:
        game_info['message'] = "take a guess"
        game_info['css'] = "yellow"
    elif session['guess'] > session['random']:
        game_info['message'] = "too high"
        game_info['css'] = "red"
    elif session['guess'] < session['random']:
        game_info['message'] = "too low"
        game_info['css'] = "red"
    else:
        game_info['message'] = "thats correct"
        game_info['css'] = "green"
    return(render_template('index.html', game_info=game_info))


@app.route('/work', methods=['POST'])
def work():
    session['guess'] = int(request.form['guess'])
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
