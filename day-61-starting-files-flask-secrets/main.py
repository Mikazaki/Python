from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5




app = Flask(__name__)
bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label='Log In')
    csfr_token = app.secret_key = "banana"


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login = MyForm()
    if login.validate_on_submit():
        if login.email.data == "admin@email.com" and login.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
        
    return render_template('login.html', form = login)


if __name__ == '__main__':
    app.run(debug=True)
