# from app import app, db
# from app.models import User, Post
# from app import cli
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}

from app import create_app, db, cli
from app.main.models import User, Post, Notification, Message

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}
