from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'aqlite:///shop.db'
db = SQLAlchemy


class Item(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer(100), nullable=False)
    isActive = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/task')
def task():
    return render_template('task.html')

if __name__ =='__main__':
    app.run(debug=True)