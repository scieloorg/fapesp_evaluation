from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField


class PostForm(FlaskForm):
    title = StringField(u'Titulo')
    content = TextAreaField(u'Conteúdo')


class QuestionsForm(FlaskForm):
    criterio1a = StringField()
    criterio1b = StringField()
    criterio1c = StringField()
    justifica1a = TextAreaField()
    justifica1b = TextAreaField()
    justifica1c = TextAreaField()
    example = RadioField(choices=[('value1', 'Bom'), ('value2', 'Médio')])
