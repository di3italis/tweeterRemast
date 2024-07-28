from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

AUTHOR_CHOICES = ["Elon Musk", "Jono", "Markus", "Bitxos"]


class Form(FlaskForm):
    # validators must be in a List, and invoked if built-in, not for custom
    # Length takes min and/or max
    author = SelectField("Tweet Author", choices=AUTHOR_CHOICES)
    tweet = StringField(
        "Tweet",
        validators=[
            DataRequired(),
            Length(min=5, max=140, message="Tweet must be at least 5 characters."),
        ],
    )
    submit = SubmitField("Create Tweet")
