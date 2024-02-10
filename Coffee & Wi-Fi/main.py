from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location On Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', validators=[DataRequired()], choices=["✘", "☕️☕️☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️", "☕️☕️", "☕️"])
    wifi = SelectField('Wi-Fi Strength Rating', validators=[DataRequired()], choices=["✘", "💪💪💪💪💪", "💪💪💪💪", "💪💪💪", "💪💪", "💪"])
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=["✘", "🔌🔌🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌", "🔌🔌", "🔌"])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',  methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    file_path = 'Python Projects\Coffee & Wi-Fi\cafe-data.csv'

    if form.validate_on_submit():
        with open(file_path, mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data}," 
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    file_path = 'Python Projects\Coffee & Wi-Fi\cafe-data.csv'

    with open(file_path, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = list(csv_data)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
