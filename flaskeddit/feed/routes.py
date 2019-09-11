from flask import render_template, request
from flask_login import current_user

from flaskeddit.feed import feed_blueprint, feed_service


@feed_blueprint.route("/")
@feed_blueprint.route("/feed")
def feed():
    """Route for list of posts from joined communities sorted by date created."""
    page = int(request.args.get("page", 1))
    if current_user.is_authenticated:
        posts = feed_service.get_feed(current_user, page, False)
        return render_template("feed.jinja2", tab="recent", posts=posts)
    else:
        return render_template("feed.jinja2", tab="recent", posts=None)


@feed_blueprint.route("/feed/top")
def top_feed():
    """Route for list of posts from joined communities sorted by upvotes."""
    page = int(request.args.get("page", 1))
    if current_user.is_authenticated:
        posts = feed_service.get_feed(current_user, page, True)
        return render_template("feed.jinja2", tab="top", posts=posts)
    else:
        return render_template("feed.jinja2", tab="top", posts=None)
