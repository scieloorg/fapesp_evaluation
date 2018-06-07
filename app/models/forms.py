# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, validators

choicelist1 = [
    ('muito', 'Muito'),
    ('bastante', 'Bastante'),
    ('razoavel', 'Razoavelmente'),
    ('pouco', 'Pouco'),
    ('nada', 'Nada')
        ]
choicelist2 = [
    ('muito', 'Muito'),
    ('bastante', 'Bastante'),
    ('razoavel', 'Razoavelmente'),
    ('pouco', 'Pouco'),
    ('nada', 'Nada'),
    ('nao_indexado', 'Não indexado')
        ]

# validatorlist1 = [validators.InputRequired(message='* Campo obrigatório.')]
validatorlist1 = [validators.Length(min=0, max=100, message=None)]


class PostForm(FlaskForm):
    title = StringField(u'Titulo')
    content = TextAreaField(u'Conteúdo')


class QuestionsForm(FlaskForm):
    instituicao = StringField('', validators=validatorlist1)
    entidade = StringField('', validators=validatorlist1)
    departamento = StringField('')

    criterio1a = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio1b = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio1c = RadioField('', choices=choicelist1, validators=validatorlist1)
    justifica1a = TextAreaField('', validators=validatorlist1)
    justifica1b = TextAreaField('', validators=validatorlist1)
    justifica1c = TextAreaField('', validators=validatorlist1)

    criterio2a = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio2b = RadioField('', choices=choicelist1, validators=validatorlist1)
    justifica2a = TextAreaField('', validators=validatorlist1)
    justifica2b = TextAreaField('', validators=validatorlist1)

    # criterio3a tem um choice a mais
    criterio3a = RadioField('', choices=choicelist2, validators=validatorlist1)
    criterio3b = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3c = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3d = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3e = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3f = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3g = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3h = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3i = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio3j = RadioField('', choices=choicelist1, validators=validatorlist1)
    justifica3a = TextAreaField('', validators=validatorlist1)
    justifica3b = TextAreaField('', validators=validatorlist1)
    justifica3c = TextAreaField('', validators=validatorlist1)
    justifica3d = TextAreaField('', validators=validatorlist1)
    justifica3e = TextAreaField('', validators=validatorlist1)
    justifica3f = TextAreaField('', validators=validatorlist1)
    justifica3g = TextAreaField('', validators=validatorlist1)
    justifica3h = TextAreaField('', validators=validatorlist1)
    justifica3i = TextAreaField('', validators=validatorlist1)
    justifica3j = TextAreaField('', validators=validatorlist1)

    criterio4a = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio4b = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio4c = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio4d = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio4e = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio4f = RadioField('', choices=choicelist1, validators=validatorlist1)
    criterio4g = RadioField('', choices=choicelist1, validators=validatorlist1)
    justifica4a = TextAreaField('', validators=validatorlist1)
    justifica4b = TextAreaField('', validators=validatorlist1)
    justifica4c = TextAreaField('', validators=validatorlist1)
    justifica4d = TextAreaField('', validators=validatorlist1)
    justifica4e = TextAreaField('', validators=validatorlist1)
    justifica4f = TextAreaField('', validators=validatorlist1)
    justifica4g = TextAreaField('', validators=validatorlist1)

    recomenda = TextAreaField('', validators=validatorlist1)
