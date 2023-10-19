from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Assuming your Python script is inside the IlyaWebsite directory
root_directory = os.path.abspath(os.path.dirname(__file__))

# Construct the relative path
db_path = os.path.join(root_directory, "Databases", "referrals.db")
connection_string = f"sqlite:///{db_path}"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SECRET_KEY'] = 'supersecretkey'  # Set a secret key for flashing messages

db = SQLAlchemy(app)

class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website_name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)


@app.route('/')
def index():
    referrals = Referral.query.all()
    return render_template('index.html', codes=referrals)

@app.route('/add_referral', methods=['POST'])
def add_referral():
    if request.method == 'POST':
        website_name = request.form.get('website-name-input')
        url = request.form.get('url-input')

        # Basic Data Validation
        if not website_name or not url:
            flash('All fields are required!', 'error')
            return redirect('/')

        referral = Referral(website_name=website_name, url=url)

        try:
            db.session.add(referral)
            db.session.commit()
            flash('Referral added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Failed to add referral. It might already exist.', 'error')

        return redirect('/')


    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
