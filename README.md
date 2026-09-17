# Mohamed Idris - Personal Portfolio Website – Python Project

A complete personal portfolio website built with Flask, using Jinja2 templating for consistent layout across all pages/routes.

# 🎯 Project Overview

The goal of this project is to design and develop a responsive, accessible, and professional website. By using semantic HTML and custom CSS, Python, and Flask as backend framework.

👤 About This Project

Built as an academic assessment — Database-Driven Web Application with Flask
Demonstrates full-stack fundamentals:

• ✅ Python backend & routing

• ✅ Relational database design (many-to-many relationships)

• ✅ CRUD operations (Create, Read, Update, Delete)

• ✅ Form validation & error handling

• ✅ Responsive frontend design

• ✅ Git version control

Built with Flask, SQLAlchemy & CSS

## ✨ Key Features

### Developer Management

- Add new developers — first name, last name, email
- Edit existing developer details
- Delete developers
- Email uniqueness validation — prevents duplicates
- Input validation — shows clear messages; keeps filled values visible

### Skill Management

- Add skills — name, category, description
- Edit skill details
- Remove skills from database
- Predefined categories: Frontend, Backend, Programming Languages, Databases, Tools & DevOps, Design, Other
- `<textarea>` for longer descriptions — easy to read & write

### Skill Assignments — Many-to-Many Relationship

- Assign skills to developers with proficiency level (0–100%)
- Prevent duplicate assignments — same developer+skill cannot be added twice
- Update proficiency — edit page with slider input
- Remove assignments — delete with confirmation prompt
- Clear listing showing developer name, skill name, and percentage

### User Experience & Interface

- Fully responsive design — adapts to mobile, tablet, and desktop screens
- Navigation bar — highlights current active page
- Flash messages — clear success/error feedback
- Dropdown styling — solid backgrounds, high contrast, no transparency issues
- Form validation — all required fields checked before submission
- Pure HTML5 + CSS3 — no JavaScript required for core functionality
- Consistent color scheme — gold accents, clean readable contrast

# Navigation & Sections

The website features a smooth, multi-pages navigation layout including:

- Logo & 5-Link Nav: Quick access to all pages.
- Hero Section: A professional landing introduction.
- About Me: My background and personal story.
- Skills: Technical proficiencies and tools.
- Developers: A showcase of my completed projects.
- DeveloperSkill: Technical proficiencies and tools.
- Footer: Copyrights and social links.

# 🛠️ Technologies & Tools

## Core Stack

- HTML5 - Semantic structure.
- CSS3 - Custom styling and layout.
- Python 3.
- Flask 3.1.3 – Web framework.
- Jinja2 3.1.6 – Templating engine.
- HTML5 & CSS3 – Frontend structure and styling.
- Other required packages: blinker, click, itsdangerous, MarkupSafe, Werkzeug.

# Design Resources

I utilized these professional tools to enhance the UI/UX:

- Google Font: For all textual contents in the website (Poppins Font).
- Font Awesome: For scalable vector icons.
- Flaticon: For high-quality graphic assets.
- Color Hunt: For selecting the professional color palette.

# 📱 Responsive Design (Breakpoints)

The website is optimized for different screen sizes using the following CSS strategy:

- Tablet View: Optimized for screens with a max-width: 768px.
- Mobile View: Optimized for screens with a max-width: 528px.

# 📄 Routes/Pages

- base.html – Reusable layout using Jinja2 inheritance
- index.html – Homepage
- about.html – Personal background and bio
- skills.html – List of technical and professional skills
- portfolio.html – Showcase of work and projects
- contact.html – Contact form information

# 📁 Project Structure

```FLASK-PROJECT/
├── static/ # Static assets
│ ├── css/
│ │ └── style.css # Main stylesheet
│ └── images/ # Website images
├── templates/ # HTML templates
│ ├── base.html # Base template (shared header/footer/nav)
│ ├── index.html # Home page
│ ├── about.html # About Me page
│ ├── skills.html # Skills page
│ ├── portfolio.html # Portfolio/Projects page
│ └── contact.html # Contact page
├── venv/ # Python virtual environment
├── .gitignore # Git ignored files/folders
├── app.py # Main Flask application
└── requirements.txt # Exact package versions
```

# Accessiblity Notes

For Accessibilty, I've tested the accessibilty in terms of:

Keyboard Access: ensured that all the ineractive elements are working fine.
Visual Design and Imagery: Checked the (Alt Text) attribute to make sure the Screen Reader (VoiceOver) is working perfectly.
Color Contrast: I confirmed the minimum contrast ratio is met for my website.
Form Validation: I tested that the form inputs have linked with lables, and for error checking all form inputs that have required field to be validated.

# Tests

To ensure that my code meets the requirements of cleaning and has no any kind of errors and unused code, I ran some tests to my code to review and clean my code is clear , I used the following tools:

# For Reviewing and Cleaning:

- VS Code feature: to clear and format indentation to look good.
- Developer Tools: to ensure your code is 100% utalizied.
- Validator.w3.org website: to validate your code is clean for HTML file.
- Jigsaw.w3.org website: to validate your code is clean for CSS file.

# For Accessibilty Test :

- Axe Devtools: to ensure the code has no errors.

# General Notes / Developer Logs

Before I started buindling this website, I was worried about bringing an idea for this project because Python and Flask cocepts were not well known for me, becuase of that I've encountered some issues took me some time to be able to understand python and especially Flask. Then I began my journey with Flask, although I had an idea to build another website I decided to go and develop/enhance my previous project I built just to apply all the concept that I have been learning throughout the course. During building the project I encountered lots of error messages from Flask as expected but later on I managed to fix them all by watching the recoreded classes and searching on Developers forum or so, and then I started to enjoy after understanding all the concepts and fixing errors to build my website by using these new tools Python and Flask. At the end I would say, taking what you learnt already and then add what you just learnt it's really something, I started to feel that I am growing a bit by bit every project that we built and we will build, will add a fragment to your experience as developer a junior one.

# 📦 Requirements (requirements.txt)

- blinker==1.9.0
- click==8.4.1
- Flask==3.1.3
- gunicorn==26.0.0
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.3
- packaging==26.2
- Werkzeug==3.1.8

# 🚫 .gitignore Contents

- venv
- .idea/
- .vscode/
- pycache/
- dist/
- .coverage\*
- htmlcov/
- .tox/
  d- ocs/\_build/
- .DS_Store

# 🚀 How to Run

1. Activate Virtual Environment

## For Windows

1. venv\Scripts\activate
2. Install Dependencies : pip install -r requirements.txt
3. Run the App by writing python app.py
4. View in Browser : http://localhost:5000

## For macOS / Linux

1. source venv/bin/activate
2. Install Dependencies : pip install -r requirements.txt
3. Run the App by writing python app.py
4. View in Browser : Go to: http://localhost:5000

# How to View

- Copy the below link.
- Paste the link on the browser.
- Then you will be able to see the whole project on your browser.
- The link: https://

### GitHub Repo Link

- https://github.com/Mohd-Idris/

### Live Website Link

- https://.onrender.com

#####################################################
README

# 🖥️ Skills & Portfolio Hub — Flask Database Web Application

A database-driven web application built with **Python**, **Flask**, **SQLAlchemy ORM**, and **SQLite**. Designed as a fully functional system to manage developers, skills, and skill-proficiency assignments — with clean, responsive styling and zero JavaScript required.

---

## ✨ Key Features

### Developer Management

- ✅ Add new developers — first name, last name, email
- ✅ Edit existing developer details
- ✅ Delete developers
- ✅ Email uniqueness validation — prevents duplicates
- ✅ Input validation — shows clear messages; keeps filled values visible

### Skill Management

- ✅ Add skills — name, category, description
- ✅ Edit skill details
- ✅ Remove skills from database
- ✅ Predefined categories: Frontend, Backend, Programming Languages, Databases, Tools & DevOps, Design, Other
- ✅ `<textarea>` for longer descriptions — easy to read & write

### Skill Assignments — Many-to-Many Relationship

- ✅ Assign skills to developers with proficiency level (0–100%)
- ✅ Prevent duplicate assignments — same developer+skill cannot be added twice
- ✅ Update proficiency — edit page with slider input
- ✅ Remove assignments — delete with confirmation prompt
- ✅ Clear listing showing developer name, skill name, and percentage

### User Experience & Interface

- ✅ Fully responsive design — adapts to mobile, tablet, and desktop screens
- ✅ Navigation bar — highlights current active page
- ✅ Flash messages — clear success/error feedback
- ✅ Dropdown styling — solid backgrounds, high contrast, no transparency issues
- ✅ Form validation — all required fields checked before submission
- ✅ Pure HTML5 + CSS3 — no JavaScript required for core functionality
- ✅ Consistent color scheme — gold accents, clean readable contrast

---

## 🛠️ Technologies Used

| Technology           | Purpose                             |
| -------------------- | ----------------------------------- |
| **Python 3**         | Backend programming language        |
| **Flask**            | Lightweight web framework           |
| **Flask-SQLAlchemy** | ORM — database models & queries     |
| **SQLite**           | Local file-based database           |
| **HTML5**            | Page structure & templates (Jinja2) |
| **CSS3**             | Styling, layout, responsiveness     |
| **Git / GitHub**     | Version control & project hosting   |

---

## 📊 Database Design — ERD Summary

### Relationship Overview

- **Developer** ←→ **DeveloperSkill** ←→ **Skill**
- Junction table: `DeveloperSkill` handles **many-to-many** relationship
- One developer can have many skills
- One skill can be assigned to many developers
- Each assignment stores its own proficiency percentage

### Developer Table

| Field        | Type        | Constraint       |
| ------------ | ----------- | ---------------- |
| `id`         | Integer     | Primary Key      |
| `first_name` | String(50)  | Required         |
| `last_name`  | String(50)  | Required         |
| `email`      | String(100) | Unique, Required |

### Skill Table

| Field         | Type       | Constraint  |
| ------------- | ---------- | ----------- |
| `id`          | Integer    | Primary Key |
| `name`        | String(50) | Required    |
| `category`    | String(50) | Required    |
| `description` | Text       | Required    |

### DeveloperSkill Junction Table

| Field               | Type    | Constraint                 |
| ------------------- | ------- | -------------------------- |
| `id`                | Integer | Primary Key                |
| `developer_id`      | Integer | Foreign Key → Developer.id |
| `skill_id`          | Integer | Foreign Key → Skill.id     |
| `proficiency_level` | Integer | 0–100, Required            |

**Cascading Delete:** Removing a developer or skill automatically removes all their associated assignments.

---

## 📂 Project Structure

```
Database Project/
├── venv/                   # Python virtual environment
│
├── instance/
│   └── developers.db       # SQLite database (auto-created)
│
├── static/                 # Static assets
│ ├── css/
│ │ └── style.css           # Main stylesheet
│ └── images/               # Website images
│
├── templates/              # HTML templates
├── base.html               # Base template (shared header/footer/nav)
├── index.html              # Home / landing page
├── about.html              # About / About Me page
├── developers.html         # Add developer + list all developers
├── edit-developers.html    # Edit existing developer
├── skills.html             # Add skill + list all skills
├── edit-skills.html        # Edit existing skill
├── developer-skills.html   # Assign skills to developers
└── edit-dev-skills.html    # Update proficiency level
│
├── .gitignore              # Git ignored files/folders
├── app.py                  # Main Flask app, models, all routes
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies

```

---

## 🚀 How to Run This Project

### 1. Install Dependencies

```bash
pip install flask flask-sqlalchemy
###2. Start the application
python app.py
### 3. Open in Your Browser

http://127.0.0.1:5001

The SQLite database (developers.db) will be created automatically on first launch.
```

📝 Usage Guide

Getting Started

1. Add Developers → Go to "Developers" → Fill form → Submit

2. Add Skills → Go to "Skills" → Enter name, select category, write description → Submit

3. Assign Skills → Go to "Assign Skills" → Select developer + skill → Set proficiency → Submit

4. Edit or Delete → Use buttons next to each entry in the lists

5. On Mobile → Layout adapts automatically — inputs become full-width, columns stack vertically

Validation & Safety

• All fields marked required must be filled

• Values remain in form if error occurs — no re-typing everything

• Duplicate emails and duplicate assignments are blocked

• Proficiency restricted to 0–100 range

• Confirmation prompt appears before deleting

🔄 Version Control — Git

• Repository hosted on GitHub

• Regular commits with clear descriptive messages

• .gitignore excludes: virtual environment, database files, system auto-generated files

📌 Future Enhancements

• User authentication & secure login system

• PostgreSQL integration (replace SQLite)

• Search and filter functionality

• Profile image upload

• Pagination for large datasets

• Password protection for edit/delete actions

```

```
