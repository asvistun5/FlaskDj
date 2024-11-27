import flask_mail
from .settings import project

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USE_TLS'] = True
project.config['MAIL_USERNAME'] = 'flaskproject155@gmail.com'
project.config['MAIL_PASSWORD'] = 'qwertyqwerty123098' 
project.config['MAIL_DEFAULT_SENDER'] = 'flaskproject155@gmail.com'
mail = flask_mail.Mail(project)