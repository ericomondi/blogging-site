from flask import Flask, render_template, request, redirect, url_for
from dbservice import get_data


app = Flask(__name__)   

@app.route("/")
def index():
    blogs = get_data("blogs")
    cats = get_data("categories")
    users = get_data("users")

    return render_template("index.html", blogs = blogs, cats=cats, users=users)


if __name__ == '__main__':
    app.run(debug=True)


