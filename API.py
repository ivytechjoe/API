from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)

if __name__ == '__main__':
    app.run(debug=True)
