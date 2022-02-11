from . import main
from flask import render_template, url_for, abort, request, redirect
from flask_login import login_required, current_user
from ..models import User, Post, Like, Dislike, Comment
from .. import db, photos
from .forms import PostForm,CommentForm,UpdateForm

@main.route('/')
def index():
    pitches = Post.query.all()
    return render_template("index.html",pitches=pitches)


@main.route('/profile/<my_name>')
@login_required
def profile(my_name):
    title = "Flask Profile"
    user = User.query.filter_by(username=my_name).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user, title=title)


@main.route('/update/<my_name>', methods=['GET', 'POST'])
@login_required
def edit_profile(my_name):
    title = "Edit profile"
    user = User.query.filter_by(username=my_name).first()
    if user is None:
        abort(404)
    update_form = UpdateForm()
    if update_form.validate_on_submit():
        user.biography = update_form.biography.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', my_name=user.username))

    return render_template("profile/update.html", update_form=update_form, title=title)


@main.route('/updateImage/<my_name>', methods=['POST'])
@login_required
def update_image(my_name):
    title = "Update image"
    user = User.query.filter_by(username=my_name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
    return redirect(url_for('main.profile', my_name=my_name, title=title))


@main.route('/new-post/<id>', methods=['GET', 'POST'])
@login_required
def post(id):
    """New Post function"""
    title = "New Post"
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        post = form.post.data

        new_post = Post(title=title, category=category, post=post, user=current_user)

        new_post.save_post()
        return redirect(url_for('.index'))

    return render_template('post.html', form=form, title=title)


@main.route('/Like/<id>', methods=['GET', 'POST'])
@login_required
def Like(id):
    votes = Like.get_Likes(id)
    output = f'{current_user.id}:{id}'
    for vote in votes:
        result = f'{vote}'
        if output == result:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_Like = Like(user=current_user, Post_id=id)
    new_Like.save()
    return redirect(url_for('main.index', id=id))


@main.route('/Dislike/<id>', methods=['GET', 'POST'])
@login_required
def Dislike(id):
    votes = Dislike.get_Dislikes(id)
    output = f'{current_user.id}:{id}'
    for vote in votes:
        result = f'{vote}'
        if output == result:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_Dislike = Dislike(user=current_user, Post_id=id)
    new_Dislike.save()
    return redirect(url_for('main.index', id=id))


@main.route('/comment/<id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    post = Post.query.get(id)
    fetch_all_comments = Comment.query.filter_by(Post_id=id).all()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        Post_id = id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, Post_id=Post_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', id=Post_id))
    return render_template('comments.html', comment_form=comment_form, Post=Post, all_comments=fetch_all_comments)


@main.route('/pickup')
def pickup():
    # Postes = Post.query.all()
    title="Pickup Line Post"
    pickup = Post.query.filter_by(category='pickup').all()
    return render_template('category/pickup.html', all_Postes=pickup,title=title)

@main.route('/interview')
def interview():
    # Postes = Post.query.all()
    title="Interview Post"
    interview = Post.query.filter_by(category='interview').all()
    return render_template('category/interview.html', all_Postes=interview,title=title)

@main.route('/product')
def product():
    # Postes = Post.query.all()
    title="Product Post"
    product = Post.query.filter_by(category='product').all()
    return render_template('category/product.html', all_Postes=product,title=title)

@main.route('/promotion')
def promotion():
    # Postes = Post.query.all()
    title="Promotion Post"
    promotion = Post.query.filter_by(category='promotion').all()
    print(promotion)

