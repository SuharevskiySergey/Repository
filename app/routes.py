# from datetime import datetime
# from flask import render_template, flash, redirect, url_for, request
# from flask_login import login_user, logout_user, current_user, login_required
# from werkzeug.urls import url_parse
# from app import app, db
# from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, ResetPasswordRequestForm, ResetPasswordForm
# from app.models import User, Post
# from app.email import send_password_reset_email
# from flask_babel import _
# from flask import g
# from flask_babel import get_locale
# from guess_language import guess_language
#
#
# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()
#         g.locale = str(get_locale())
#
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# @login_required
# def index():
#     form = PostForm()
#     if form.validate_on_submit():
#         language = guess_language(form.post.data)
#         if language == "UNKNOWN" or len(language) > 5:
#             language = ''
#         post = Post(body=form.post.data, author=current_user, language=language)
#         db.session.add(post)
#         db.session.commit()
#         flash(_("You post is now live!"))
#         return redirect(url_for('index'))
#     #posts = current_user.followed_posts().all()
#     page = request.args.get('page', 1, type=int)
#     posts = current_user.followed_posts().paginate(
#             page=page,
#             per_page=app.config['POSTS_PER_PAGE'],
#             error_out=False
#         )
#     next_url = url_for('index', page=posts.next_num)\
#         if posts.has_next else None
#     prev_url = url_for('index', page=posts.prev_num) \
#         if posts.has_prev else None
#     return render_template('index.html', title='Home', form=form, posts=posts,
#                            next_url=next_url, prev_url=prev_url)
#
#
# @app.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = [
#         {'author': user, 'body': 'Test post #1'},
#         {'author': user, 'body': 'Test post #2'}
#     ]
#     return render_template('user.html', user=user, posts=posts)
#
#
# @app.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#     form = EditProfileForm(current_user.username)
#     if form.validate_on_submit():
#         current_user.username = form.username.data
#         current_user.about_me = form.about_me.data
#         db.session.commit()
#         flash('Your changes have been saved.')
#         return redirect(url_for('edit_profile'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.about_me.data = current_user.about_me
#     return render_template('edit_profile.html', title='Edit Profile',
#                            form=form)
#
#
# @app.route('/follow/<username>')
# @login_required
# def follow(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash("User {} not found.".format(username))
#         flash(_('User %(username)s not found.', username=username))
#         return redirect(url_for('index'))
#     if user == current_user:
#         flash('You cannot follow yourself')
#         return redirect(url_for('user', username=username))
#     current_user.follow(user)
#     db.session.commit()
#     flash("You following{}!".format(username))
#     return redirect(url_for('user', username=username))
#
#
# @app.route('/unfollow/<username>')
# @login_required
# def unfollow(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash("User {} not found.".format(username))
#         return redirect(url_for('index'))
#     if user == current_user:
#         flash('You cannot unfollow yourself')
#         return redirect(url_for('user', username=username))
#     current_user.unfollow(user)
#     db.session.commit()
#     flash("You not following{}!".format(username))
#     return redirect(url_for('user', username=username))
#
#
# @app.route('/explore')
# @login_required
# def explore():
#     page = request.args.get('page', 1, type=int)
#     posts = Post.query.order_by(Post.timestamp.desc()).paginate(
#         page=page,
#         per_page=app.config['POSTS_PER_PAGE'],
#         error_out=False
#     )
#     next_url = url_for('index', page=posts.next_num) \
#         if posts.has_next else None
#     prev_url = url_for('index', page=posts.prev_num) \
#         if posts.has_prev else None
#     return render_template('index.html', title='Explore', posts=posts.items,
#                            next_url=next_url, prev_url=prev_url)
#
