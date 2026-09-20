# Mohamed Idris - Portfolio Hub — Flask Database Web Application

A database-driven web application built with **Python**, **Flask**, **SQLAlchemy ORM**, and **SQLite**. Designed as a fully functional system to manage developers, skills, and skill-proficiency assignments — with clean, responsive styling.

# 🎯 Project Overview

The goal of this project is to design and develop a responsive, accessible, and professional website. By using semantic HTML and custom CSS, Python, Flask, and Database.

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
- Clear listing showing developer name, and skill name with proficiency level (percentage)

### User Experience & Interface

- Fully responsive design — adapts to mobile, tablet, and desktop screens
- Navigation bar — highlights current active page
- Flash messages — clear success/error feedback
- Form validation — all required fields checked before submission
- Pure HTML5 + CSS3 — no JavaScript required for core functionality
- Consistent color scheme — gold accents, clean readable contrast

# Navigation & Sections

The website features a smooth, multi-pages navigation layout including:

- Logo & 5-Link Nav: Quick access to all pages.
- Hero Section: A professional landing introduction.
- About Me: My background and personal story.
- Developers: Manage developer records ——— add, view, edit, and delete.
- Skills: Manage skill entries ——— add, view, edit, and delete.
- Assign Skills: Link developers to skills as well as set proficiency level for each developer skill.
- Footer: Copyrights and social links.

# 🛠️ Technologies & Tools

## Core Stack

| Technology           | Purpose                             |
| -------------------- | ----------------------------------- |
| **HTML5**            | Page structure & templates (Jinja2) |
| **CSS3**             | Styling, layout, responsiveness     |
| **JavaScript**       | Adding Interactivity                |
| **Python 3**         | Backend programming language        |
| **Flask**            | Lightweight web framework           |
| **Flask-SQLAlchemy** | ORM — database models & queries     |
| **SQLite**           | Local file-based database           |
| **Jinja2**           | Templating engine                   |
| **Others**           | Python dependencies.                |
| **Git / GitHub**     | Version control & project hosting   |

## 📊 Database Design — ERD Summary

![`ERD Diagram`](![ERD Diagram](static/css/images/ERD.png))

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

# Design Resources

I utilized these professional tools to enhance the UI/UX:

- Google Font: For all textual contents in the website (Poppins Font).
- Font Awesome: For scalable vector icons.
- Flaticon: For high-quality graphic assets.
- Color Hunt: For selecting the professional color palette.
- draw.io - For designing the ERD diagram with relationship

# 📱 Responsive Design (Breakpoints)

The website is optimized for different screen sizes using the following CSS strategy:

- Tablet View: Optimized for screens with a max-width: 768px.
- Mobile View: Optimized for screens with a max-width: 528px.

# 📄 Routes/Pages

- base.html – Reusable layout using Jinja2 inheritance
- index.html – Homepage
- about.html – Personal background and bio
- skills.html – Adds & Shows skills
- developers.html – Adds & Shows developers
- Assign Skills - Assigns skills to developers

# 📁 Project Structure

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

- On this module, we learned how to connect a website to an actual database. previously, we had not done this —— we were working with dummy data, and then we used `Browser` LocalStorage to store data directly in the browser. Now we've learned to build and use a proper database, so our info is stored securely and we never need to worry about losing data.<br>

- When I started building this project, I was extending and rebuilding the foundation I created for `Project NO #2`. My main question was `how do I integrate a real database into what I had built before`? After learning the fundamentals ——— how to design tables, create a database, and connect entities through relationships —— here is my project journey:

### Phase #1: Database Design

- Used `draw.io` to design the `ERD Diagram` with three core entities (tables)
- Defined the data types and constraints for each attribute (field)
- Established relationship between entities (tables), including the junction table for many-to-many connections.

### Phase #2: Environment & Foundation

Start building the core / structure of the project such as:

1. Created local `Git` Repo and then connected it to `GitHub`
2. Built the shared `base template` —— with shared navigation, header, and footer
3. Set up Flask App & configured `Flask-Alchemy` with `SQLite`
4. Established `CSS` basic structure and color scheme

### Phase #3: Core Features

#### Developers

- Built `Developers` page : add form and full listing displayed side-by-side
- Implemented input validation & prevented duplicate email entries
- Values preserved in the form if an error occurs —— no need to re-type everything

#### Edit Developers

- Created `Edit Developers` page : form pre-fills the existing data, update the record
- Save updates and return to the Developers List
- Added `Delete` functionality with confirmation message
- Implemented email validation to prevent duplication

#### Skills

- Built `Skills` page : add form and full listing displayed side-by-side
- Implemented input validation for all required fields

#### Edit Skills

- created `Edit Skills` page : updates all the field dynamically
- Added `Delete` functionality with confirmation message

### Phase #4: Relationships (Assign Skills)

- Built `Assign Skills` page —— connects developers to skills with proficiency level slider
- Refined slider display : real-time percentage display the value
- Cascade `Delete` logic —— removing a developer or skill automatically removes all their associated assignments

### Phase #5: Testing

- Tested what I've built to make sure everything is working fine
- Tested all pages, routes, and forms to confirm everything works fine
- Verified accessibility - all contrast ratios meet the minimum 4.5:1 standard
- Ensured responsive layout works across the mobile and tablet screens

### Summary

Through this module (`Database Module`), I have built a complete, working database-driven web application. Having learned `HTML`, `CSS`, `JavaScript`, `Python`, and now `Database`. I feel myself growing into a real developer. I know I am still at the beginning, but I can see how all these pieces fit together. I am excited to keep learning, practicing, and mastering these tools one day —— so I can build beautiful, powerful, and user-friendly websites in the near future.

# 📌 Future Development

```
• User authentication & secure login system

• PostgreSQL integration (replace SQLite)

• Search and filter functionality

• Profile image upload

• Pagination for large datasets

• Password protection for edit/delete actions

• Make an account for each developer to be able to create his profile

• Improve the `Assign Skills` to hold more than skills for a certain developer

• Improve website User Experience to be better by adding some interactivity
```

# 📦 Requirements (requirements.txt)

- blinker==1.9.0
- click==8.4.1
- Flask==3.1.3
- Flask-SQLAlchemy==3.1.1
- gunicorn==26.0.0
- psycopg2-binary
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.3
- packaging==26.2
- Werkzeug==3.1.8

# 🚫 .gitignore Contents

### ── System / Hidden / Auto-generated ──

- .DS_Store
- .DS_Store?
- .\_\*
- .Spotlight-V100
- .Trashes
- ehthumbs.db
- Thumbs.db

### ── Editor / Vim / IDE files/folders ──

- .vim/
- \*.swp
- \*.swo
- \*~
- .vscode/
- .idea/
- \*.log
- \*.iml

### ── Python / Flask / Virtual Env ──

- .venv/
- venv/
- env/
- **pycache**/
- \*.pyc
- \*.pyo
- \*.pyd
- .env
- .flaskenv

### ── Database / SQLite / Temp ──

- \*.db
- \*.sqlite
- \*.sqlite3
- \*.log
- \*.tmp
- .cache
- instance/

# 🚀 How to Run

1. Activate Virtual Environment

## For Windows

1. venv\Scripts\activate
2. Install Dependencies : pip install -r requirements.txt
3. Run the App by writing python app.py
4. View in Browser : http://localhost:5001

## For macOS / Linux

1. source venv/bin/activate
2. Install Dependencies : pip install -r requirements.txt
3. Run the App by writing python app.py
4. View in Browser : Go to: http://localhost:5001

## 🚀 How to Run This Project

### 1. Install Dependencies

```bash
pip install flask flask-sqlalchemy
```

### 2. Start the application

```bash
python app.py
```

### 3. Open in Your Browser

```
http://127.0.0.1:5001
```

The SQLite database (developers.db) will be created automatically on first launch.

# 📝 User Guide

1. Add Developers → Go to "Developers" → Fill form → Submit

2. Add Skills → Go to "Skills" → Enter name, select category, write description → Submit

3. Assign Skills → Go to "Assign Skills" → Select developer + skill → Set proficiency → Submit

4. Edit or Delete → Use buttons next to each entry in the lists

5. On Mobile → Layout adapts automatically — inputs become full-width, columns stack vertically

## Validation & Safety

• All fields marked required must be filled

• Values remain in form if error occurs — no re-typing everything

• Duplicate emails are blocked

• Proficiency restricted to 0–100 range

• Confirmation prompt appears before deleting

## 🔄 Version Control — Git

• Repository hosted on GitHub

• Regular commits with clear descriptive messages

• .gitignore excludes: virtual environment, database files, system auto-generated files

# 🖥️ How to View

- Copy the below link.
- Paste the link on the browser.
- Then you will be able to see the whole project on your browser.
- The link: [https://module-4-project-python-flask-db.onrender.com/]()

### GitHub Repo Link

- https://github.com/Mohd-Idris/Module-4-Project-Python-Flask-DB

### Live Website Link

- https://module-4-project-python-flask-db.onrender.com/
