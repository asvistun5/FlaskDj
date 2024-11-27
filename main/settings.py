import flask, flask_sqlalchemy, flask_migrate, os

project = flask.Flask(
    import_name='main',
    template_folder='templates',
    static_folder='static',
    static_url_path='/main/',
    instance_path= os.path.abspath(__file__ + '/..')
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(app = project, db = db)