from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, EqualTo, Regexp


class Form(FlaskForm):
    name = StringField('Your Name', [InputRequired()])
    username = StringField('User Account', [InputRequired(), Length(min=2, max=20),
                                            Regexp('[\\u4e00-\\u9fa5a-zA-Z0-9_]+',
                                                   message='Only letters, numbers and underscore are allowed')])
    password = PasswordField('Password', [InputRequired(), Length(min=4, max=12)])
    confirm = PasswordField('Confirm Password', [InputRequired(), Length(min=4, max=12),
                                                 EqualTo('password', message='Password must match')])
    submit = SubmitField('Sign Up')


class MessageForm(FlaskForm):
    content = TextAreaField('Leave Your Messages', validators=[Length(min=1, max=225)])
    send = SubmitField('Send')