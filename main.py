 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Movie %r>' % self.title

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/browse')
def browse():
    movies = Movie.query.all()
    return render_template('browse.html', movies=movies)

@app.route('/watch/<int:movie_id>')
def watch(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('watch.html', movie=movie)

@app.route('/mylist')
def mylist():
    movies = Movie.query.all()
    return render_template('mylist.html', movies=movies)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
