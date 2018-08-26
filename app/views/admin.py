from flask import render_template, g, request, Blueprint
from flask_login import login_required
admin_blueprint = Blueprint('admin', __name__,)


@admin_blueprint.route('/admin/')
@login_required
def home():
    context = {}
    return render_template('admin/home.html', **context)