from app import db


class Question(db.DynamicDocument):
    # issn = db.StringField()
    # title = db.StringField()
    criterio1a = db.StringField()
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

    def __unicode__(self):
        return self.title
