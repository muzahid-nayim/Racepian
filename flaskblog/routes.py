
from flask import  render_template , url_for,flash,redirect
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User, Post
from flaskblog import app

posts  = [
    {'title':'How to make?','author':'Muzahid','content':'first post contentfirst pofirst post contentst content','date_posted':'april 1'},
    {'title':'Why you loser','author':'Nayim','content':'second post first post contentfirst post contentcontent','date_posted':'March 2'}
]

@app.route("/")
@app.route("/home")#this is second route to go home page 
def home():
    return render_template('home.html', posts = posts, title = 'Home') #sending arguments
 

@app.route("/about")
def about():
    return render_template('about.html',title = 'About')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register', form = form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'loser':
            flash('You have been logged in !','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful,please check username or password','danger')
    return render_template('login.html',title = 'Login', form = form)

