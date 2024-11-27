import flask
from .models import Article, db


def render_tour():
    return flask.render_template(template_name_or_list='tour.html', articles = Article.query.all())