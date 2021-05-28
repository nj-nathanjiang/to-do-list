from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)

tasks = []

name = "example"
rating = "example"
deadline = "example"


@app.route("/", methods=["POST", "GET"])
def home():
    global name, deadline, rating
    if request.method == "POST":
        name = request.form["name"]
        deadline = request.form["deadline"]
        rating = request.form["rating"]

        return redirect("/add")
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<task_name>")
def delete(task_name):
    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)

    return redirect("/")


@app.route("/add", methods=["POST", "GET"])
def add():
    global name, deadline, rating

    for task in tasks:
        if task["name"] == name:
            return render_template("name_already_taken.html")

    tasks.append(
        {"name": name,
         "rating": rating,
         "deadline": deadline})
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
