import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
if os.path.exists("env.py"):
    import env

# creating an instance of the application

app = Flask(__name__)

# environment variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)   #connect to Mongo


@app.route('/')
def index():
    categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=categories)


# Error handling from
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/


@app.errorhandler(HTTPException)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def internal_server_error(e):
    return render_template('500.html'), 500


# User authentication

# Register new user


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
            "password": generate_password_hash(request.form.get("password")),
            "favorite_posts": []
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    categories = list(mongo.db.categories.find())
    return render_template("register.html", categories=categories)


# Login for existing user


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
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

    categories = list(mongo.db.categories.find())
    return render_template("login.html", categories=categories)


# Display user profile page


@app.route("/profile", methods=["GET"])
def profile():
    if session["user"]:
        user = mongo.db.users.find_one_or_404({"username": session["user"]})
        categories = list(mongo.db.categories.find())
        posts = mongo.db.posts.find({"created_by": user['username']})
        if "favorite_posts" in user:
            obj_ids = [ObjectId(x) for x in user["favorite_posts"] if x != ""]
            fav_posts = mongo.db.posts.find({"_id": {"$in": obj_ids}})
        else:
            fav_posts = []
        return render_template(
            "profile.html", username=session["user"], posts=posts,
            fav_posts=fav_posts, categories=categories)
    return redirect(url_for("login"))


# Logout functionality


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Display categories


@app.route('/get_categories')
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template('board.html', categories=categories)


# Search posts


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    categories = list(mongo.db.categories.find())
    return render_template(
        "categories.html", posts=posts, categories=categories)


# CRUD functions-post management

# Get posts that belong in the same category

@app.route("/posts/<category>")
def posts(category):
    categories = list(mongo.db.categories.find())
    filtered_posts = mongo.db.posts.find({"category_name": category})
    return render_template(
          'categories.html', posts=filtered_posts, categories=categories,
          category=category)


# Create post functionality


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        if 'post_image' in request.files:
            post_image = request.files['post_image']
            mongo.save_file(post_image.filename, post_image)
        post = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "contact_details": request.form.get("contact_details"),
            "created_by": session["user"],
            "post_image": post_image.filename,
        }
        mongo.db.posts.insert_one(post)
        flash("Post created")
        return redirect(url_for(
                        "profile", username=session["user"]))
    categories = list(mongo.db.categories.find())
    return render_template("create_post.html", categories=categories)


# Image uploads from https://www.youtube.com/watch?v=DsgAuceHha4
# and I also got ideas from https://github.com/elenasacristan/CookBook


@app.route('/img_uploads/<filename>')
def img_uploads(filename):
    return mongo.send_file(filename)


# View post functionality


@app.route('/view_post/<post_id>')
def view_post(post_id):

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template('view_post.html', post=post, post_id=post_id)


# Edit post functionality


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        if 'post_image' in request.files:
            post_image = request.files['post_image']
            mongo.save_file(post_image.filename, post_image)
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "contact_details": request.form.get("contact_details"),
            "created_by": session["user"],
            "post_image": post_image.filename,
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash("Post updated!")
        return redirect(url_for("profile", username=session["user"]))

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("edit_post.html", post=post, categories=categories)


# Delete post functionality


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post deleted")
    return redirect(url_for("profile", username=session["user"]))



# Add post to User's favorite posts


@app.route("/save_post/<post_id>", methods=["POST"])
def save_post(post_id):
    if request.method == "POST":
        user = mongo.db.users.find_one_or_404({"username": session["user"]})
        if "favorite_posts" in user:
            user["favorite_posts"].append(post_id)
        else:
            user["favorite_posts"] = [post_id]
            # in case the object does not have the favorite_posts property
        mongo.db.users.update_one(
            {"_id": ObjectId(user["_id"])},
            {"$set": {"favorite_posts": user["favorite_posts"]}})
        flash("Post added to favorites")
        return redirect(url_for("profile", username=session["user"]))


# Remove post from to User's favorite posts


@app.route("/unsave_post/<post_id>", methods=["POST"])
def unsave_post(post_id):
    if request.method == "POST":
        user = mongo.db.users.find_one_or_404({"username": session["user"]})
        if "favorite_posts" in user:
            user["favorite_posts"].remove(post_id)
        mongo.db.users.update_one(
            {"_id": ObjectId(user["_id"])},
            {"$set": {"favorite_posts": user["favorite_posts"]}})
        flash("Post removed from favorites")
        return redirect(url_for("profile", username=session["user"]))


# Manage categories-Admin functions
# Create a new category

@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        if 'category_image' in request.files:
            category_image = request.files['category_image']
            mongo.save_file(category_image.filename, category_image)

        category = {
            "category_name": request.form.get("category_name"),
            "category_description": request.form.get("category_description"),
            "category_image": category_image.filename,
        }
        mongo.db.categories.insert_one(category)
        flash("New category successfully added")
        return redirect(url_for("get_categories"))

    categories = list(mongo.db.categories.find())
    return render_template("create_category.html", categories=categories)


# Edit a category


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        if 'category_image' in request.files:
            category_image = request.files['category_image']
            mongo.save_file(category_image.filename, category_image)

        edit = {
            "category_name": request.form.get("category_name"),
            "category_description": request.form.get("category_description"),
            "category_image": category_image.filename,
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, edit)
        flash("Category updated!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    categories = list(mongo.db.categories.find())
    return render_template(
        "edit_category.html", categories=categories, category=category)


# Delete a category


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
