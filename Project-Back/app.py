from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['UPLOAD_PATH']='static/uploads'
db = SQLAlchemy(app) 
migrate=Migrate(app,db, render_as_batch=True)

# All models

class Slider(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120))
    desc=db.Column(db.String(120))
    img=db.Column(db.String(120))

class Teachers(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(100))
    name=db.Column(db.String(100))
    title=db.Column(db.String(120))
    desc=db.Column(db.Text)
    phone=db.Column(db.Integer)
    
class Courses(db.Model): 
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(100))
    title=db.Column(db.String(100))
    desc=db.Column(db.Text)


class Cities(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(100))
    title=db.Column(db.String(100))
    desc=db.Column(db.Text)
    

class Messages(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    content=db.Column(db.Text)


# All App Routes
@app.route('/')
def index():
    slider=Slider.query.all()
    return render_template("app/index.html",slider=slider)

@app.route('/about')
def about():
    teachers=Teachers.query.all()
    return render_template("app/about.html",teachers=teachers)

@app.route('/courses')
def courses():
    courses=Courses.query.all()
    return render_template("app/courses.html",courses=courses)

@app.route('/education-abroad')
def education_abroad():
    cities=Cities.query.all()
    return render_template("app/education-abroad.html",cities=cities)




@app.route('/contact',methods=['GET','POST'])
def contact():
    messages=Messages()
    if request.method=='POST':
        messages=Messages(
            name=request.form['name'],
            email=request.form['email'],
            content=request.form['content']
        )
        db.session.add(messages)
        db.session.commit()
        return redirect(url_for('messages'))
    return render_template("app/contact.html",messages=messages)


# All Admin Routes

@app.route("/admin/")
def admin():
    return render_template("admin/index.html")

@app.route("/admin/slider/",methods=['GET','POST'])
def slider():
    sliders=Slider.query.all()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        slider=Slider(
            title=request.form['title'],
            desc=request.form['desc'],
            img=filename
        )
        db.session.add(slider)
        db.session.commit()
        return redirect('/admin/slider/')
    return render_template("admin/slider.html",sliders=sliders)


@app.route("/admin/teachers/",methods=['GET','POST'])
def teachers():
    teachers=Teachers.query.all()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        teachers=Teachers(
            name=request.form['name'],
            title=request.form['title'],
            desc=request.form['desc'],
            phone=request.form['phone'],
            img=filename
        )
        db.session.add(teachers)
        db.session.commit()
        return redirect('/admin/teachers/')
    return render_template("admin/teachers.html",teachers=teachers)

@app.route("/admin/courses/",methods=['GET','POST'])
def add_course():
    courses=Courses.query.all()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        courses=Courses(
            title=request.form['title'],
            desc=request.form['desc'],
            img=filename
        )
        db.session.add(courses)
        db.session.commit()
        return redirect('/admin/courses/')
    return render_template("admin/courses.html",courses=courses)



@app.route("/admin/cities/",methods=['GET','POST'])
def add_city():
    cities=Cities.query.all()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        city=Cities(
            title=request.form['title'],
            desc=request.form['desc'],
            img=filename
        )
        db.session.add(city)
        db.session.commit()
        return redirect('/admin/cities/')
    return render_template("admin/cities.html",cities=cities)


@app.route('/admin/messages/')
def messages():
    messages=Messages.query.all()
    return render_template("admin/messages.html",messages=messages)





#Delete

@app.route('/admin/slider/delete/<id>')
def delete_slider(id):
    deleteSlider=Slider.query.get(id)
    db.session.delete(deleteSlider)
    db.session.commit()
    return redirect("/admin/slider")


@app.route('/admin/teachers/delete/<id>')
def delete_teacher(id):
    deleteTeachers=Teachers.query.get(id)
    db.session.delete(deleteTeachers)
    db.session.commit()
    return redirect("/admin/teachers")

@app.route('/admin/courses/delete/<id>')
def delete_course(id):
    deleteCourses=Courses.query.get(id)
    db.session.delete(deleteCourses)
    db.session.commit()
    return redirect("/admin/courses")

@app.route('/admin/cities/delete/<id>')
def delete_city(id):
    deleteCities=Cities.query.get(id)
    db.session.delete(deleteCities)
    db.session.commit()
    return redirect("/admin/cities")

@app.route('/admin/messages/delete/<id>')
def delete_message(id):
    deleteMessages=Messages.query.get(id)
    db.session.delete(deleteMessages)
    db.session.commit()
    return redirect("/admin/messages")

#Update
@app.route('/admin/slider/update/<id>', methods=['GET','POST'])
def update_slider(id):
    sliderUpdate=Slider.query.get(id)
    if request.method=='POST':
        if request.files['img']:
            file=request.files['img']
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            sliderUpdate.img=filename
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        title=request.form['title']
        desc=request.form['desc']
        sliderUpdate.title=title
        sliderUpdate.desc=desc
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('admin/update_slider.html',update=sliderUpdate)



@app.route('/admin/teachers/update/<id>', methods=['GET','POST'])
def update_teacher(id):
    teachersUpdate=Teachers.query.get(id)
    if request.method=='POST':
        if request.files['img']:
            file=request.files['img']
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            teachersUpdate.img=filename
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        title=request.form['title']
        desc=request.form['desc']
        teachersUpdate.title=title
        teachersUpdate.desc=desc
        db.session.commit()
        return redirect('/admin/teachers')
    return render_template('admin/update_teacher.html',update=teachersUpdate)


@app.route('/admin/courses/update/<id>', methods=['GET','POST'])
def update_course(id):
    coursesUpdate=Courses.query.get(id)
    if request.method=='POST':
        if request.files['img']:
            file=request.files['img']
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            coursesUpdate.img=filename
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        title=request.form['title']
        desc=request.form['desc']
        coursesUpdate.title=title
        coursesUpdate.desc=desc
        db.session.commit()
        return redirect('/admin/courses')
    return render_template('admin/update_course.html',update=coursesUpdate)


@app.route('/admin/cities/update/<id>', methods=['GET','POST'])
def update_city(id):
    citiesUpdate=Cities.query.get(id)
    if request.method=='POST':
        if request.files['img']:
            file=request.files['img']
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            citiesUpdate.img=filename
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        title=request.form['title']
        desc=request.form['desc']
        citiesUpdate.title=title
        citiesUpdate.desc=desc
        db.session.commit()
        return redirect('/admin/cities')
    return render_template('admin/update_city.html',update=citiesUpdate)


#Detail

@app.route('/admin/slider/detail/<id>')
def sliderDetail(id):
    sliderdetail=Slider.query.get(id)
    return render_template('admin/slider_detail.html',sliderdetail=sliderdetail)

@app.route('/admin/teachers/detail/<id>')
def teachersDetail(id):
    teachersdetail=Teachers.query.get(id)
    return render_template('admin/teacher_detail.html',teachersdetail=teachersdetail)

@app.route('/admin/courses/detail/<id>')
def coursesDetail(id):
    coursesdetail=Courses.query.get(id)
    return render_template('admin/course_detail.html',coursesdetail=coursesdetail)

@app.route('/admin/cities/detail/<id>')
def citiesDetail(id):
    citiesdetail=Cities.query.get(id)
    return render_template('admin/city_detail.html',citiesdetail=citiesdetail)


@app.route('/admin/messages/detail/<id>')
def messagesDetail(id):
    messagesdetail=Messages.query.get(id)
    return render_template('admin/message_detail.html',messagesdetail=messagesdetail)



if (__name__)=='__main__':
    app.run(debug=True)
    manager.run()
    
    
    
    