from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy()
db.init_app(app)




class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

class Update(FlaskForm):
    rating = FloatField('Your Rating Out Of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class Add(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

   
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        all_movies = Movie.query.order_by(Movie.rating.desc()).all()
        
        for i, movie in enumerate(all_movies):
            movie.ranking = i + 1  
        db.session.commit()

        return render_template("index.html", movies=all_movies)

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    movie_to_update = Movie.query.get(id)
    update = Update()
    if request.method == "POST":
        new_rating = request.form['rating']
        new_review = request.form['review']
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=movie_to_update, form = update)

@app.route("/delete")
def delete():
    movie_id= request.args.get('id')


    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    
    form = Add() 
    if form.validate_on_submit():
        title = request.form["title"]
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": ""
        }

        response = requests.get(url, headers=headers)

        data = response.json()

        results = data['results']

        return render_template("select.html", movies=results)
    
    return render_template("add.html", form = form)



@app.route("/find/<int:id>", methods=["GET", "POST"])
def find(id):
        URL_ID = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": ""
        }

        movie_url = "https://image.tmdb.org/t/p/original"
        
        response = requests.get(URL_ID, headers=headers)

        data = response.json()
        
        new_movie = Movie(
            title = data["title"],
            year = data["release_date"].split("-")[0],
            description = data['overview'],
            img_url = f"{movie_url}{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))
    

if __name__ == '__main__':
    app.run(debug=True)
