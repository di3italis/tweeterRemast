from flask import Flask, render_template
from .config import Config
from .tweets import tweets as seed_tweets
from .routes.tweet_routes import tweets
import random
# https://docs.python.org/3/library/random.html#examples

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(tweets, url_prefix="/tweets")


@app.route("/")
def home():
    rand_tweet = random.randrange(len(seed_tweets))
    # return tweets[rand_tweet]["tweet"]
    return render_template("index.html", tweet=seed_tweets[rand_tweet])
