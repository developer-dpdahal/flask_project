from flask import render_template
from flaskproject import app


@app.route('/')
@app.route('/home')
def index():
    return render_template("frontend/pages/home.html")


@app.route('/about')
def about():
    return render_template("frontend/pages/about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("frontend/errors/404.html"), 404
