from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
app.config['UPLOAD_PATH']='static/uploads'
db=SQLAlchemy(app)

class Slider(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120))
    text=db.Column(db.String(250))
    img=db.Column(db.String(120))
    






# main index
@app.route('/')
def index():
    return render_template('app/index.html')

# admin index
@app.route('/admin')
def admin():
    return render_template('admin/index.html')

# slider index
@app.route('/admin/slider')
def slider():
    return render_template('admin/slider.html')

# add slider index
@app.route('/admin/slider/new')
def add_slider():
    return render_template('admin/add_slider.html')
if __name__ == '__main__':
    app.run(debug=True)