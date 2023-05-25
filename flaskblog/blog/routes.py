from flask import Blueprint
from PIL import Image
from flask import  render_template , url_for,flash,redirect,request,abort
from .forms import PostForm
from flaskblog.models import User, Post
from flaskblog import app,db,bcrypt
from flask_login import login_user, current_user,logout_user,login_required
import secrets,os

posts = Blueprint('posts',__name__)


# ========================================================
# ====================BLOG ROUTES========================
# ========================================================
@posts.route("/blog")
def blog():
    page = request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('blog.html',title ='Blog',posts=posts)



# ========================================================
# =====================NEW POST ROUTES====================
# ========================================================
@posts.route("/post/new",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('posts.blog'))
    image_file = url_for('static', filename='profilePic/' + current_user.image_file)
    return render_template('create_post.html',title = 'New Post',form=form, legend='New Post', image_file=image_file,sider="let's create  a new post ")

   
# ========================================================
# =====================POST <> ROUTES=====================
# ========================================================
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)#get post by id but if it is not possible return 404
    return render_template('post.html',title=post.title, post=post)


# ========================================================
# ====================UPDATE POSTS ROUTES=================
# ========================================================
@posts.route("/post/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Post has been updated !','success')
        return redirect(url_for('posts.post',post_id=post.id))
    else :
        form.title.data = post.title
        form.content.data = post.content
    image_file = url_for('static', filename='profilePic/' + current_user.image_file)
    return render_template('create_post.html',title = 'Update Post',form=form, legend='Update Post' , sider="Let's update the post",image_file=image_file)


# ========================================================
# ===================DELETE POST ROUTES===================
# ========================================================
@posts.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted !','success')
    return redirect(url_for('posts.blog'))


