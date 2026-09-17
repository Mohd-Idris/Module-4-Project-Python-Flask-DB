import os
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and configure secret key for session management
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

database_url = os.environ.get('DATABASE_URL', 'sqlite:///developers.db')

# Configure SQLAlchemy with SQLite database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)


# ============================================================================================================
# Define the Developer model with id, first_name, last_name, and email fields
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Define the Relationship between Entities (Developer & Skill)
    skill_asssigned = db.relationship('DeveloperSkill', backref='developer', cascade='all, delete-orphan')
  

    # Define the string representation of the Developer model for debugging purposes
    def __repr__(self):
        return f'<Developer {self.first_name} {self.last_name}>'
# ============================================================================================================


# ============================================================================================================
# Define the Skills model with id, name, category, percentage, and description fields
class Skill(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  category = db.Column(db.String(50), nullable=False)
  description = db.Column(db.Text, nullable=False)

  # Define the Relationship between Entities (Developer & Skill)
  developer_asssigned = db.relationship('DeveloperSkill', backref='skill', cascade='all, delete-orphan')

  # Define the string representation of the Skill model for debugging purposes
  def __repr__(self):
      return f'<Skill {self.name}>'
# ============================================================================================================


# ============================================================================================================
# Define the Developer-Skills model with id, dev_id, skill_id, and proficiency_level fields
class DeveloperSkill(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'), nullable=False)
  skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
  proficiency_level = db.Column(db.Integer, nullable=False)

  # Define the Relationship between Entities (Developer & Skill)
  # developer = db.relationship('Developer', backref=db.backref('skills_assigned', cascade='all, delete-orphan'))
  # skill = db.relationship('Skill', backref=db.backref('developers_assigned', cascade='all, delete-orphan'))

  def __repr__(self):
    return f'<DeveloperSkill Developer:{self.developer_id} Skill:{self.skill_id}'
# ============================================================================================================



# Home page route -loads HTML from templates Folder
@app.route("/")
@app.route("/home")
def home():
  return render_template("index.html", title="Database Flask Project - Home Page")

# About page route -loads HTML from templates Folder
@app.route("/about")
def about():
  return render_template("about.html", title="Database Flask Project - About Page")

# ============================================================================================================
# Add Developer page route -loads HTML from templates Folder
@app.route("/developers", methods=["GET", "POST"])
def add_developer():
  if request.method == "POST":
    # Get form data
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    email = request.form["email"].strip().lower()

    # Track errors
    errors = []
    
    firstNameInput = first_name
    lastNameInput = last_name
    emailInput = email
    
    if not  first_name:
      errors.append("* First Name is Required.")
    if not last_name:
       errors.append("* Last Name is Required.")
    if not email:
      errors.append("* Email is Required.")

    # Check if the email already exists in the database
    existing_developer = Developer.query.filter_by(email=email).first()
    if existing_developer:
      errors.append("❌ A developer with this email already exists. Please use a different email.")
  
    
    if errors:
      error_message = "❌ Missing Fields: \n" + "\n".join(errors)
      flash(error_message, "error")
      return render_template("developers.html",
                              title="Database Flask Project - Manage Developers Page",
                              developers=Developer.query.all(),
                              firstNameInput=first_name,
                              lastNameInput=last_name,
                              emailInput=email
                              ) 

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
# =========================================================================================================================


# =========================================================================================================================
@app.route("/edit_developer/<int:developer_id>", methods=["GET", "POST"])
def edit_developer(developer_id):
  developer = Developer.query.get_or_404(developer_id)

  # Handle form submission for editing developer details
  if request.method == "POST":
    # Get form data
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    email = request.form["email"].strip().lower()

    # # Commit changes to the database
    # db.session.commit()

    # # Flash a success message and redirect back to the add developer page
    # flash("✅ Developer updated successfully!", "success")
    # return redirect(url_for("add_developer"))

    # Validate form data
    if not first_name or not last_name or not email:
      flash("❌ All fields are required. Please fill in all fields.", "error")
      return redirect(url_for("edit_developer", developer_id=developer_id))

    # Check if the email already exists in the database for a different developer
    existing_developer = Developer.query.filter_by(email=email).first()
    # If a developer with the same email exists and it's not the current developer being edited, flash an error message and redirect back to the edit developer page
    if existing_developer and existing_developer.id != developer.id:
      flash("❌ A developer with this email already exists. Please use a different email.", "error")
      return redirect(url_for("edit_developer", developer_id=developer_id))

    # Update developer details
    developer.first_name = first_name
    developer.last_name = last_name
    developer.email = email

    # Commit changes to the database
    db.session.commit()
    # Flash a success message and redirect back to the add developer page
    flash("✅ Developer updated successfully!", "success")
    return redirect(url_for("add_developer"))
  
  return render_template("edit-developers.html", title="Database Flask Project - Edit Developer Page", developer=developer)
# =========================================================================================================================


# =========================================================================================================================
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
# ==========================================================================================================================


# ==========================================================================================================================
# Manage Skills 
# Add Skill page route -loads HTML from templates Folder
@app.route("/skills", methods=["GET", "POST"])
def add_skill():
  if request.method == "POST":
      # Get form data
      name = request.form["skill_name"].strip()
      category = request.form["category"].strip()
      # percentage = request.form["percentage"].strip()
      description = request.form["description"].strip()


      # Track errors
      errors = []

      nameInput = name
      categoryInput = category
      descriptionInput = description

      if not name:
        errors.append("* Skill Name is Required.")
      if not category:
        errors.append("* Skill Category is Required.")
      if not description:
        errors.append("* Skill Description is Required.")

      if errors:
        error_message = "❌ Missing Fields: \n" + "\n".join(errors)
        flash(error_message, "error")
        return render_template("skills.html",
                               title="Database Flask Project - Manage Skills Page",
                               skills=Skill.query.all(),
                               nameInput=name,
                               categoryInput=category,
                               descriptionInput=description
                               )
  
      # Validate form data first 
      # if not name or not category or not description:
      #   flash("❌ All fields are required. Please fill in all fields.", "error") 
      #   return redirect(url_for("add_skill"))
  
      # Create new developer instance
      new_skill = Skill(name=name, category=category, description=description)
  
      # Add to database
      db.session.add(new_skill)
      db.session.commit()
      # Flash a success message and redirect back to the add skill page
      flash("✅ Skill added successfully!", "success")
      return redirect(url_for("add_skill"))
  
  # Query all skills from the database and pass them to the template for rendering
  skills = Skill.query.all()
  
  return render_template("skills.html", title="Database Flask Project - Manage Skills Page", skills=skills)

# ==========================================================================================================================


# ==========================================================================================================================
@app.route("/edit_skill/<int:skill_id>", methods=["GET", "POST"])
def edit_skill(skill_id):
  skill = Skill.query.get_or_404(skill_id)

  # Handle form submission for editing skill details
  if request.method == "POST":
    # Get form data
    name = request.form["name"].strip()
    category = request.form["category"].strip()
    # percentage = request.form["percentage"].strip()
    description = request.form["description"].strip()

    # Validate form data
    if not name or not category or not description:
      flash("❌ All fields are required. Please fill in all fields.", "error") 
      return redirect(url_for("edit_skill", skill_id=skill_id))

    # Update developer details
    skill.name = name
    skill.category = category
    # skill.percentage = percentage
    skill.description = description

    # Commit changes to the database
    db.session.commit()
    # Flash a success message and redirect back to the add developer page
    flash("✅ Skill updated successfully!", "success")
    return redirect(url_for("add_skill"))
  
  return render_template("edit-skills.html", title="Database Flask Project - Edit Developer Page", skill=skill)
# ==========================================================================================================================


# ==========================================================================================================================
#  Delete Skill route - handles deletion of a skill by ID
@app.route("/delete_skill/<int:skill_id>", methods=["POST"])
def delete_skill(skill_id):
  # Get the developer by ID or return a 404 error if not found
  skill = Skill.query.get_or_404(skill_id)
  db.session.delete(skill)
  db.session.commit()
  # Flash a success message when developer is deleted and redirect back to the add developer page
  flash("✅ Skill deleted successfully!", "success")
  return redirect(url_for("add_skill"))  
# ==========================================================================================================================


# ==========================================================================================================================
# Assign Skills to Developers 
# Add DeveloperSkill page route -loads HTML from templates Folder
@app.route("/developer-skills", methods=["GET", "POST"])
def assign_skill():
  if request.method == "POST":
     # Get form data
     dev_id = request.form["developer_id"].strip()
     skill_id = request.form["skill_id"].strip()
     pro_level = request.form["skill-proficiency"].strip()


     # Track errors
     errors = []
      
     if not dev_id or dev_id == "":
        errors.append("* Developer must be selected first.")
     if not skill_id or skill_id == "":
        errors.append("* Skill must be selected first.")
     if not pro_level:
        errors.append("* Skill Proficiency must be determined.")
      
     if errors:
        error_message = "❌ Missing Fields: \n" + "\n".join(errors)
        flash(error_message, "error")
        return render_template("developer-skills.html",
                                     title="Database Flask Project - Manage Assigning Developers Skills Page",
                                     developers = Developer.query.all(),
                                     skills=Skill.query.all(),
                                     assignments=DeveloperSkill.query.all() #comeback later
                                    )
     # Check if developer has the same skill
     dev_skill_exist = DeveloperSkill.query.filter_by(developer_id = int(dev_id), skill_id = int(skill_id)).first()
     if dev_skill_exist:
        flash("This Skill is already assigned to this developer","error")
        return redirect(url_for("assign_skill"))

     # Create new developer-skill instances
     developer_id = int(dev_id)
     skill_id = int(skill_id)
     proficiency_level = int(pro_level)

     new_dev_skill = DeveloperSkill(developer_id=developer_id, skill_id=skill_id, proficiency_level=proficiency_level) #proficiency_level
     
     # Add to database
     db.session.add(new_dev_skill)
     db.session.commit()
     # Flash a success message and redirect back to the add skill page
     flash("✅ Skill added successfully to a Developer!", "success")
     return redirect(url_for("assign_skill"))


  # Query all skills from the database and pass them to the template for rendering
  developers = Developer.query.all()
  skills = Skill.query.all()
  assignments = DeveloperSkill.query.all()
  return render_template("developer-skills.html", title="Database Flask Project - Manage Skills Assigning", developers=developers,skills=skills, assignments=assignments)
# =======================================================================================================================================================================


# =======================================================================================================================================================================
@app.route("/edit-assign/<int:assign_id>", methods=["GET", "POST"])
def edit_assign(assign_id):
  assignment = DeveloperSkill.query.get_or_404(assign_id)
  if request.method == "POST":
    proficiency_value = request.form.get("proficiency_level").strip()

    # Validate form data
    if not proficiency_value :
      flash("❌ All fields are required. Please fill in all fields.", "error") 
      return redirect(url_for("edit_assign"))
    
    
    
    assignment.proficiency_level = int(proficiency_value)
    db.session.commit()
    # Flash a success message and redirect back to the add skill page
    flash("✅ Proficiency updated successfully!", "success")
    return redirect(url_for("assign_skill"))
  return render_template("edit-dev-skills.html", title="Database Flask Project - Edit Developer's Skills Page", assignment=assignment)

# =======================================================================================================================================================================

# =======================================================================================================================================================================
@app.route("/delete-assign/<int:assign_id>", methods=["GET", "POST"])
def delete_assign(assign_id):
  assignment = DeveloperSkill.query.get_or_404(assign_id)
  db.session.delete(assignment)
  db.session.commit()
  # Flash a success message and redirect back to the add skill page
  flash("✅ Skill Assigned has been removed successfully!", "success")
  return redirect(url_for("assign_skill"))
# =======================================================================================================================================================================

with app.app_context():
  # Create the database tables based on the defined models
  db.create_all()
   
if __name__ == "__main__":
  # Runs local server at http://127.0.0.1:5001,
  # once you save changes, it refreshes automatically
  app.run(debug=True, port=5001)