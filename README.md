Sweetney Inventory Management System 📦

A Flask-based web application to manage inventory efficiently.

Sweetney lets you track products, manage stock movements, and maintain an organized inventory with a clean and cozy interface.

Features 

Add, update, and delete products

Track product quantities and movements

Search and filter products easily

User-friendly UI built with Flask and Jinja2

Optional reports and data export

Demo

Live demo (if deployed):
[Insert your deployed app link here]

Installation ⚡

Clone the repository:

git clone <YOUR_GITHUB_REPO_URL>
cd sweetney


Create a virtual environment:

python -m venv venv

Activate the environment:

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Set environment variables (if needed):

# Example for Flask
export FLASK_APP=app.py
export FLASK_ENV=development

Run the application:

flask run

Open your browser at http://127.0.0.1:5000

Project Structure
sweetney/
│
├─ app.py                  # Main Flask app
├─ requirements.txt        # Python dependencies
├─ templates/              # HTML templates
├─ static/                 # CSS, JS, images
├─ forms.py                # Flask-WTF forms
├─ models.py               # Database models
├─ routes.py               # Flask routes (if separated)
└─ ...

Dependencies

Flask

Flask-WTF

WTForms

Flask-SQLAlchemy (or any DB ORM you are using)

Other packages as listed in requirements.txt

Contributing

Feel free to fork the project, suggest features, or submit pull requests. Keep inventory management simple and cozy!
