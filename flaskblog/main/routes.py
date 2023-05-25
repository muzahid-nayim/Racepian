from flask import Blueprint
from PIL import Image
from flask import  render_template , url_for,flash,redirect,request,abort
from flaskblog.models import User, Post
from flaskblog import app,db,bcrypt

main = Blueprint('main',__name__)



# ========================================================
# =====================HOME ROUTES========================
# ========================================================
@main.route("/")
# @main.route("/home")#this is second route to go home page 
def home():
    # posts = Post.query.all()
    page = request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('home.html', posts = posts, title = 'Home') #sending arguments
 

# ========================================================
# ====================ABOUT ROUTES========================
# ========================================================
@app.route("/about")
def about():
    return render_template('about.html',title = 'About')

