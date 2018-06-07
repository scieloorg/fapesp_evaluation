# coding: utf-8
from app import db
import datetime


class Question(db.DynamicDocument):
    creation_date = db.DateTimeField(default=datetime.datetime.now)
    acceced = db.IntField(min_value=0, default=0)

    def __unicode__(self):
        return self.title
