import flask
from .models import User, db

def render_register():
    is_registered = False
    if flask.request.method == 'POST':

        user = User(
            username = flask.request.form['username'],
            password = flask.request.form['password'],
        )
        try:

            db.session.add(user)
            db.session.commit()
            is_registered = True
            
            return flask.redirect('/auth')

        except Exception as e:
            is_registered = False
            return f"{e}" 
           

              
    
    return flask.render_template(template_name_or_list="registration.html", is_registered = is_registered)


