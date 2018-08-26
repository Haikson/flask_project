from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class FeedbackForm(FlaskForm):
    name = StringField(u'Ваше имя', [DataRequired(),])
    city = StringField(u'Город')
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40)
        ]
    )
    phone = StringField(u'Телефон')
    company = StringField(u'Организация')
    additional = TextAreaField(u'Дополнительная информация')

    def send(self, message):
        from app import mail
        from flask_mail import Message
        from flask import current_app

        msg = Message(
            body=message,
            subject='Subject',
            sender=('{sender_domain}', current_app.config.get('DEFAULT_FROM_EMAIL')),
            recipients=current_app.config.get('DEFAULT_TO_EMAIL')
        )
        mail.send(msg)
