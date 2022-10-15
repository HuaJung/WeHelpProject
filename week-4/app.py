from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'


accounts = [{'username': 'test', 'password': 'test'},
            {'username': 'panda', 'password': 'panda'}]


@app.route('/')
def index():
    return render_template('index.html', title='LOGIN')


@app.route('/signin', methods=['POST'])
def signin():
    account = request.form['account']
    pwd = request.form['pwd']
    if account == '' or pwd == '':
        return redirect('/error?message=empty')
    else:
        for acc in accounts:
            if account == acc['username'] and pwd == acc['password']:
                session['username'] = account
                return redirect('/member')
        return redirect('/error?message=incorrect')


@app.route('/member')
def member():
    if 'username' in session:
        return render_template('member.html', title='Member Page')
    return redirect('/')


@app.route('/error')
def error():
    message = request.args.get('message')
    if message == 'empty':
        return render_template('error.html', message='Please enter your account or password', header='OOPS!')
    elif message == 'incorrect':
        return render_template('error.html', message='Invalid Account Or Password', header='OOPS!')


@app.route('/signout')
def sign_out():
    session.pop('username')
    return redirect('/')


# making a redirect route to get the variable
@app.route('/cal')
def cal():
    num = request.args.get('num')
    return redirect(url_for('square', number=num))


@app.route('/square/<int:number>')
def square(number):
    number = number**2
    return render_template('square.html', square_number=number)


@app.route('/register')
def register():
    return render_template('construction.html', header='SORRY!')


app.run(port=3000)