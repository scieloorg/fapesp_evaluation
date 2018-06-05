from app import db
from wtforms import validators


class Post(db.Document):
    title = db.StringField(
        max_length=120,
        required=True,
        validators=[validators.InputRequired(message=u'Missing title.'), ])
    content = db.StringField()

    def __unicode__(self):
        return self.title


class Question(db.DynamicDocument):
    issn = db.StringField()
    title = db.StringField()
    criterio1a = db.StringField(
        required=True,
        validators=[validators.InputRequired(message=u'Seleção ausente.'), ])
    justifica1a = db.StringField(required=True)

    def __unicode__(self):
        return self.title
