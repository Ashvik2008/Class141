from crypt import methods
from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch_movies = []

app = Flask(__name__)

@app.route("/get-movies")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "Success"
    })

@app.route("/liked-movies",methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)

    return jsonify({
        "status": "Success"
    }),201

@app.route("/not-liked-movies",methods=["POST"])
def not_liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)

    return jsonify({
        "status": "Success"
    }),201

@app.route("/not-watched-movies",methods=["POST"])
def not_watched_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched_movie.append(movie)

    return jsonify({
        "status": "Success"
    }),201


if __name__ == "__main__":
    app.run()