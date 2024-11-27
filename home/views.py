import flask
import flask_mail

def render_home():
    return flask.render_template(template_name_or_list= 'home.html')

def render_feedback():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        email = flask.request.form['email']
        feedback_text = flask.request.form['feedback']
        massege = flask_mail.Message('Новий відгук від клієнта', recipients=['admin_email@example.com'], sender= 'flaskproject155@gmail.com')
        massege.body = f"Клієнт {name} залишив/ла відгук:\n\n{feedback_text}.\n\nПошта для зворотнього звʼязку з клієнтом: {email}."
        try:
            flask_mail.send(massege)
            return flask.redirect("/home")
        except Exception as e:
            return flask.redirect("/home")
    return flask.render_template(template_name_or_list= 'feedback.html', methods=['POST', 'GET'])

