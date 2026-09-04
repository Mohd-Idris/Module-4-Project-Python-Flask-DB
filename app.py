from flask import Flask, render_template
app = Flask(__name__)

# Home page route -loads HTML from templates Folder
@app.route("/")
@app.route("/home")
def home():
  return render_template("index.html", title="Database Flask Project - Home Page")

# About page route -loads HTML from templates Folder
@app.route("/about")
def about():
  return render_template("about.html", title="Database Flask Project - About Page")

# Add Developer page route -loads HTML from templates Folder
@app.route("/developers")
def add_developer():
  return render_template("developers.html", title="Database Flask Project - Developers Page")

# Add Skill page route -loads HTML from templates Folder
@app.route("/skills")
def add_skill():
  return render_template("skills.html", title="Database Flask Project - Skills Page")

if __name__ == "__main__":
  # Runs local server at http://127.0.0.1:5001,
  # once you save changes, it refreshes automatically
  app.run(debug=True, port=5001)