from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, validators

choicelist1 = [
    ('muito', 'Muito'),
    ('bastante', 'Bastante'),
    ('razoavel', 'Razoavelmente'),
    ('pouco', 'Pouco'),
    ('nada', 'Nada')
        ]


class PostForm(FlaskForm):
    title = StringField(u'Titulo')
    content = TextAreaField(u'Conteúdo')


class QuestionsForm(FlaskForm):
    criterio1a = RadioField(
        '',
        choices=choicelist1,
        validators=[validators.InputRequired(message='* Campo obrigatório.')])
    criterio1b = RadioField(
        '',
        choices=choicelist1,
        validators=[validators.InputRequired(message='* Campo obrigatório.')])
    criterio1c = RadioField(
        '',
        choices=choicelist1,
        validators=[validators.InputRequired(message='* Campo obrigatório.')])
    justifica1a = TextAreaField(
        '',
        validators=[validators.InputRequired(message='* Campo obrigatório.')])

    justifica1b = TextAreaField()
    justifica1c = TextAreaField()
