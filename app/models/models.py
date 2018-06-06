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
    # issn = db.StringField()
    # title = db.StringField()
    criterio1a = db.StringField(
        choices=[('muito', 'Bom'), ('razoavel', 'Razoavel')])
        # required=True,
        # validators=[validators.InputRequired(message=u'Seleção ausente.')])
    criterio1b = db.StringField()
        # required=True,
        # validators=[validators.InputRequired(message=u'Seleção ausente.')])
    criterio1c = db.StringField()
        # required=True,
        # validators=[validators.InputRequired(message=u'Seleção ausente.')])
    justifica1a = db.StringField(max_length=4000, required=True)
    justifica1b = db.StringField(max_length=4000, required=True)
    justifica1c = db.StringField(max_length=4000, required=True)
    example = db.StringField()

    def __unicode__(self):
        return self.title


class Post2(db.Document):
    body = db.StringField(required=True)
    author = db.StringField(verbose_name="Author", max_length=255, required=True)
    escolha = db.StringField(
        choices=[('muito', 'Bom'), ('razoavel', 'Razoavel'), ('no', 'No')],
        required=True)
