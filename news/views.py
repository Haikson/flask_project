from flask import render_template, request, Blueprint

from content.models import News

news_blueprint = Blueprint('news', __name__,)


@news_blueprint.route('/news/', methods=['GET'])
def index():
    page_number = int(request.args.get('page', 1))
    per_page = 12
    news = News.query.order_by(News.date.desc()).paginate(page_number, per_page, error_out=False)
    context = {
        'news': news.items,
        'paging': news
    }
    template = 'news/index.html'
    return render_template(template, **context)


@news_blueprint.route('/news/<slug>/')
def news(slug):
    news = News.query.filter(News.id==slug).first_or_404()
    template = 'news/news.html'

    context = {
        'news': news,
    }
    return render_template(template, **context)

