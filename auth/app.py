import flask

auth = flask.Blueprint(
    name="auth",
    import_name="app",
    template_folder="auth/templates",
)