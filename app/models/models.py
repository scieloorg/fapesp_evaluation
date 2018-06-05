from app import db
from wtforms import validators


class Post(db.Document):
    title = db.StringField(max_length=120, required=True, validators=[validators.InputRequired(message=u'Missing title.'), ])
    content = db.StringField()

    def __unicode__(self):
        return self.title
