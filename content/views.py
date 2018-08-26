from flask import render_template, request, Blueprint
from content.models import Content, Publication

content_blueprint = Blueprint('content', __name__,)

@content_blueprint.route('/')
def home():
    content = Content.query.filter(Content.slug=='home').first()
    context = {'content': content}
    return render_template('content/home.html', **context)


@content_blueprint.route("/about/")
def about():
    return render_template("content/about.html")



@content_blueprint.route('/publications/', methods=['GET'])
@content_blueprint.route('/publications/view/<slug>/')
def publication(slug=None):
    context = {}
    if slug is None:
        page_number = int(request.args.get('page', 1))
        per_page = 12
        paging = Publication.query.filter(Publication.publicate==True).order_by(Publication.created_date.desc()).paginate(page_number, per_page, error_out=True)
        template = 'publication/publications.html'
        context.update({'publications': paging.items, 'paging': paging})
    else:
        publication = Publication.query.filter(Publication.slug==slug).filter(Publication.publicate==True).first()
        similar_publications = Publication.query.filter(Publication.category_id==publication.category_id).filter(Publication.publicate==True)[0:3]
        template = 'publication/publication.html'
        context.update({'publication': publication, 'similar_publications': similar_publications})
    return render_template(template, **context)
