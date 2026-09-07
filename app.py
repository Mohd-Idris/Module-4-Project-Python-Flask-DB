from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and configure secret key for session management
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Configure SQLAlchemy with SQLite database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///developers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the Developer model with id, first_name, last_name, and email fields
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Define the string representation of the Developer model for debugging purposes
    def __repr__(self):
        return f'<Developer {self.first_name} {self.last_name}>'


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
@app.route("/developers", methods=["GET", "POST"])
def add_developer():
  if request.method == "POST":
    # Get form data
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    email = request.form["email"].strip().lower()

    # Validate form data first 
    if not first_name or not last_name or not email:
      flash("❌ All fields are required. Please fill in all fields.", "error") 
      return redirect(url_for("add_developer"))

    # Check if the email already exists in the database
    existing_developer = Developer.query.filter_by(email=email).first()

    # If a developer with the same email exists, flash an error message and redirect back to the add developer page
    if existing_developer:
      flash("❌ A developer with this email already exists. Please use a different email.", "error")
      return redirect(url_for("add_developer"))

    # Create new developer instance
    new_developer = Developer(first_name=first_name, last_name=last_name, email=email)

    # Add to database
    db.session.add(new_developer)
    db.session.commit()
    # Flash a success message and redirect back to the add developer page
    flash("✅ Developer added successfully!", "success")
    return redirect(url_for("add_developer"))

  # Query all developers from the database and pass them to the template for rendering
  developers = Developer.query.all()
  return render_template("developers.html", title="Database Flask Project - Manage Developers Page", developers=developers)

#  Delete Developer route - handles deletion of a developer by ID
@app.route("/delete_developer/<int:developer_id>", methods=["POST"])
def delete_developer(developer_id):
  # Get the developer by ID or return a 404 error if not found
  developer = Developer.query.get_or_404(developer_id)
  db.session.delete(developer)
  db.session.commit()
  # Flash a success message when developer is deleted and redirect back to the add developer page
  flash("✅ Developer deleted successfully!", "success")
  return redirect(url_for("add_developer"))  

# Add Skill page route -loads HTML from templates Folder
@app.route("/skills")
def add_skill():
  return render_template("skills.html", title="Database Flask Project - Skills Page")

if __name__ == "__main__":
  # Runs local server at http://127.0.0.1:5001,
  # once you save changes, it refreshes automatically
  app.run(debug=True, port=5001)