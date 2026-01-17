from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the SQLite database
app.config['SECRET_KEY'] = 'a_very_secret_key_change_this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:quizapp123@localhost:5432/quiz_app_db'
db = SQLAlchemy(app)

# Define your database models (tables)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    quizzes = db.relationship('Quiz', backref='creator', lazy=True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_code = db.Column(db.String(10), unique=True, nullable=False)
    quiz_data = db.Column(db.Text, nullable=False) # Store quiz JSON here
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def index():
    return index_try.html

# Run this once to create the database file
#with app.app_context():
#    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
