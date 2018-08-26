# -*- coding: utf-8 -*-
from flask import render_template, request, Blueprint

from forms.feedback import FeedbackForm

feedback_blueprint = Blueprint('feedback', __name__,)


@feedback_blueprint.route('/price/', methods=['GET', 'POST'])
def price():
    form = FeedbackForm(request.form)
    context = {
        'form': form,
        'sent': False
    }
    if form.validate_on_submit():
        message = u'''
            Имя: {firstname}
            Email: {email}
            Город: {city}
            Телефон: {phone}
            Организация: {company}
            Дополнительная информация: {additional}
        '''.format(
            firstname=form.name.data,
            email=form.email.data,
            city=form.city.data,
            phone=form.phone.data,
            company=form.company.data,
            additional=form.additional.data
        )
        form.send(message=message)
        context['sent'] = True

    return render_template('feedback/price.html', **context)


@feedback_blueprint.route('/contacts/')
def contacts():
    return render_template('feedback/contacts.html')


