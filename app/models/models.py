# coding: utf-8
from app import db


class Question(db.DynamicDocument):
    # issn = db.StringField()
    # title = db.StringField()
    criterio1a = db.StringField()
    criterio1b = db.StringField()
    criterio1c = db.StringField()
    justifica1a = db.StringField(max_length=4000, required=True)
    justifica1b = db.StringField(max_length=4000, required=True)
    justifica1c = db.StringField(max_length=4000, required=True)

    def __unicode__(self):
        return self.title
