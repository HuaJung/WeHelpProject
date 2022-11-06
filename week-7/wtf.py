from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, DataRequired, Regexp
from db import data_query_one


def invalid_credentials(form, field):
    """ Username and Password Checker"""
    sql = 'SELECT * FROM member WHERE username=%s AND password=%s'
    username_entered = form.username.data
    pwd_entered = field.data
    valid_account = data_query_one(sql, (username_entered, pwd_entered))
    if valid_account is None:
        raise ValidationError('username or password is incorrect')
    else:
        return valid_account


class RegisterForm(FlaskForm):
    """ Registration Form """
    name = StringField('Your Name', [InputRequired()])
    username = StringField('Username', [InputRequired(),
                                        Length(min=2, max=20, message='username must between 4 and 20 characters'),
                                        Regexp('^\\S*$', message='space is not allowed')])
    password = PasswordField('Password', [InputRequired(),
                                          Length(min=4, max=20, message='password must between 4 and 20 characters')])
    confirm = PasswordField('Confirm Your Password', [InputRequired(),
                                                      EqualTo('password', message='passwords must match')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def validate_username(self, username):
        username_sql = 'SELECT * FROM member WHERE username=%s'
        username_entered = self.username.data
        username_exist = data_query_one(username_sql, (username_entered,))
        if username_exist:
            raise ValidationError('The username already exists. Please choose another one')


class LoginForm(FlaskForm):
    """ Login Form """
    username = StringField('Username', [InputRequired(),
                                        Length(min=2, max=20, message='username must between 4 and 20 characters')])
    password = PasswordField('Password', [InputRequired(),
                                          Length(min=4, max=20, message='password must between 4 and 20 characters'),
                                          invalid_credentials])
    remember = BooleanField('Remember Me', validators=[DataRequired()])
    submit = SubmitField('Login')


class UpdateForm(FlaskForm):
    """ Update Member's Name Form """
    update = StringField('Update My Name', [InputRequired(message='please enter your new name'),
                                            Regexp('^\\S', message='please enter a valid name')])
    submit = SubmitField('Update')

