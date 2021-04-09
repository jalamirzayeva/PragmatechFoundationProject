from flask import Flask,render_template
app = Flask(__name__)
indexContent='<h1>Website</h1>'
# homeContent='Home page'
title='Welcome to Home page!'
aboutContent='About us'
contactContent='Contact us'
@app.route('/')
def index():
    return indexContent
@app.route('/home')
def home():
    return render_template('index.html',data=title)
@app.route('/about')
def about():
    return aboutContent
@app.route('/contact')
def contact():
    return contactContent
if __name__=='__main__':
    app.run(debug=True)
