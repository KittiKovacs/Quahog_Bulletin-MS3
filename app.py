import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=categories)


@app.route('/get_categories')
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template('board.html', categories=categories)


@app.route("/posts/<category>")
def posts(category):
    categories = list(mongo.db.categories.find())
    posts = mongo.db.posts.find()
    return render_template("categories.html", posts=posts, categories=categories)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "house_no": request.form.get("house_number"),
            "street_name":  request.form.get("street").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one()

    if session["user"]:
        categories = list(mongo.db.categories.find())
        posts = mongo.db.posts.find()
        return render_template("profile.html", username=username, posts=posts, categories=categories)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        saved= "on" if request.form.get("saved") else "off"
        post = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "saved": saved,
            "created_by": session["user"],
            "image_name": image_name.filename,
        }
        mongo.db.posts.insert_one(post)
        flash("Post created")
        return redirect(url_for(
                        "profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_post.html", categories=categories)


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        saved= "on" if request.form.get("saved") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "saved": saved,
            "created_by": session["user"]
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash("Post updated!")
        return redirect(url_for("posts"))

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("profile.html", post=post, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post deleted")
    return redirect(url_for("posts"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

