from flask import Flask, render_template, redirect, request, flash, session, jsonify, make_response, url_for
from wtf import *
from db import data_query_one, insert_or_update
import secrets

app = Flask(__name__, static_folder='panda', static_url_path='/')
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Le5pdwiAAAAAPJtCCdn5oLDMdrfyxHpBCvIXZrs'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'secret'
app.config['TESTING'] = True   # to skip reCAPTCHA


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        password = form.password.data
        sql = 'INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
        insert_or_update(sql, (name, username, password))
        flash('Thanks for registering. You can login now!', 'success')
        return redirect('/login')
    return render_template('register-form.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if 'user-id' in session:
        flash('You logged in already', 'warning')
    if request.method == 'POST' and form.validate_on_submit():
        user_id = invalid_credentials(form, form.password)
        session['user-id'] = user_id[0]
        return redirect('/member')
    return render_template('login-form.html', form=form)


@app.route('/member', methods=['POST', 'GET'])
def member():
    if 'user-id' in session:
        form = UpdateForm()
        user_id = session['user-id']
        name_sql = 'SELECT name FROM member WHERE id=%s'
        name = data_query_one(name_sql, (user_id,))[0]
        return render_template('member.html', name=name, form=form)

    else:
        flash('Please Sign In', 'danger')
        return redirect('/login')


@app.route('/logout')
def logout():
    if 'user-id' in session:
        session.pop('user-id')
        flash('Log out successful', 'success')
    return redirect('/login')


@app.route('/api/member', methods=['PATCH', 'GET'])
def api():
    if request.method == 'PATCH':
        if 'user-id' in session:
            update_dic = request.get_json()
            print(update_dic)
            new_name = update_dic['name']
            user_id = session['user-id']
            name_sql = 'UPDATE member SET name=%s WHERE id=%s'
            insert_or_update(name_sql, (new_name, user_id))
            return make_response(jsonify(ok=True))
        return make_response(jsonify(error=True))
    else:
        username = request.args.get('username', '')
        username_sql = 'SELECT id, name, username FROM member WHERE username=%s'
        record = data_query_one(username_sql, (username,))
        data = {}
        if record and 'user-id' in session:
            data['id'] = record[0]
            data['name'] = record[1]
            data['username'] = record[2]
            return jsonify({'data': data})
        return jsonify(data=None)


app.run(port=3000, debug=True)