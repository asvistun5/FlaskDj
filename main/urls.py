from .settings import project
from home import render_home, render_feedback,  home
from tour import render_tour, tour
from auth import render_auth, auth
from registration import render_register, registration



project.add_url_rule(rule='/', view_func=render_home)

project.add_url_rule(rule='/tour', view_func=render_tour)

project.add_url_rule(rule='/auth', view_func=render_auth, methods=['GET', 'POST'])

project.add_url_rule(rule='/reg', view_func=render_register, methods=['GET', 'POST'])

project.add_url_rule(rule='/logout', view_func=render_feedback)


project.register_blueprint(blueprint=home)

project.register_blueprint(blueprint=tour)

project.register_blueprint(blueprint=auth)

project.register_blueprint(blueprint=registration)