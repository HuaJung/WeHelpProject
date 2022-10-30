from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from db import data_query_one, data_query_all, insert_or_update
from forms import Form, MessageForm
import secrets


app = Flask(__name__, static_folder='panda', static_url_path='/')
db = SQLAlchemy()
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)


@app.route('/')
def index():
    form = Form()
    return render_template('index.html', form=form, header='WELCOME')


@app.route('/signup', methods=['POST'])
def signup():
    # using WTForm method to store form data
    form = Form()
    if form.validate():
        name = form.name.data
        username = form.username.data
        pwd = form.password.data
        repeat_username = data_query_one(f'SELECT * FROM member WHERE username="{username}"')
        if repeat_username:
            query_str = '?message=usernameexists'
            return redirect('/error' + query_str)
        else:
            insert_or_update(f'INSERT INTO member(name, username, password) VALUES("{name}","{username}","{pwd}")')
            flash('Thanks for registering. You can login now!', 'success')
            return redirect('/')
    return redirect('/')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    pwd = request.form['password']
    record = data_query_one(f'SELECT * FROM member WHERE username="{username}" and password="{pwd}"')
    if record:
        session['user_id'] = record[0]
        return redirect('member')
    else:
        query_str = '?message=incorrect'
        return redirect('/error' + query_str)


@app.route('/member')
def member():
    form = MessageForm()
    if 'user_id' in session:
        user_id = session['user_id']
        name = data_query_one(f'SELECT * FROM member WHERE id="{user_id}"')[1]
        member_message_sql = f'SELECT member.name, message.content FROM member ' \
                           f'INNER JOIN message ON member.id=message.member_id'
        members_messages = data_query_all(member_message_sql)
        return render_template('member.html', name=name, form=form, header='MEMBER', record=members_messages)
    else:
        flash('You have been logged out. Try login again!', 'warning')
        return redirect('/')


@app.route('/error')
def error():
    if request.args.get('message') == 'incorrect':
        msg = 'Wrong account or password, please try again!'
    elif request.args.get('message') == 'usernameexists':
        msg = 'The account name has been taken, please try a different one.'
    else:
        msg = 'Something wrong with your registration, please try again!'
    return render_template('error.html', message=msg, header='OPPS!')


@app.route('/signout')
def signout():
    if 'user_id' in session:
        session.pop('user_id')
        flash('You just logged out.', 'info')
    return redirect('/')


@app.route('/message', methods=['POST'])
def message():
    content = request.form['content']
    user_id = session['user_id']
    sql = f'INSERT INTO message(member_id, content) VALUES("{user_id}", "{content}")'
    insert_or_update(sql)
    return redirect('/member')


app.run(port=3000, debug=True)