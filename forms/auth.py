from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField(u'Email Address', [DataRequired(), Email()])
    password = PasswordField(u'Password', [DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField(
        u'Email Address',
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40)
        ]
    )
    password = PasswordField(
        u'Password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        u'Confirm password',
        validators=[
            DataRequired(),
            EqualTo('password', message=u'Passwords must match.')
        ]
    )
