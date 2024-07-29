# tweet_routes.py
from flask import Blueprint, render_template, redirect
from ..tweets import tweets as seed_tweets
from ..form.form import Form
from datetime import datetime
from random import randint

tweets = Blueprint("tweets", __name__)


@tweets.route("/feed")
def tweet_feed():
    # get all tweets
    # to log to browser console, pass message to template, and render in template
    message = f"last tweet: {seed_tweets[-2]}"
    print("HEEEEEYYYY")
    return render_template("feed.html", tweets=reversed(seed_tweets), message=message)


@tweets.route("/new", methods=["GET", "POST"])
def new_tweet():
    form = Form()

    if form.validate_on_submit():
        new_tweet = {
            "id": len(seed_tweets),
            "author": form.data["author"],
            "tweet": form.data["tweet"],
            "likes": randint(1, 5_000),
            # "date": date.today(),
            "date": datetime.now().strftime("%-m/%-d/%y"),
        }
        seed_tweets.append(new_tweet)
        print(new_tweet)
        return redirect("/tweets/feed")

    if form.errors:
        print("form error", form.errors)
        return render_template("new_tweet_form.html", form=form, errors=form.errors)

    return render_template("new_tweet_form.html", form=form, errors=None)
