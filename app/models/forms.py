from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField


class PostForm(FlaskForm):
    title = StringField(u'Titulo')
    content = TextAreaField(u'Conteúdo')


class QuestionsForm(FlaskForm):
    criterio1a = StringField(u'Criterio 1a')
    justifica1a = StringField(u'Justifique suas escolhas')
