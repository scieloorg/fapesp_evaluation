# coding: utf-8
import json

from app import app
from app.models.models import Question
from app.models.forms import QuestionsForm

from flask import render_template, flash, redirect, url_for, request


@app.route('/<issn>', methods=('GET', 'POST'))
def issn(issn):

    journal = Question.objects.get_or_404(issn=issn)

    form = QuestionsForm(**json.loads(journal.to_json()))
                            # ** um dict de journal
    if form.validate_on_submit():

        form.populate_obj(journal)

        if request.method == "POST" and form.validate():
            question = Question(
                criterio1a=form.data['criterio1a'],
                criterio1b=form.data['criterio1b'],
                criterio1c=form.data['criterio1c'],
                justifica1a=form.data['justifica1a'],
                justifica1b=form.data['justifica1b'],
                justifica1c=form.data['justifica1c']
                )
                # **form.data
        mdata = json.loads(question.to_json())
        journal.update(**mdata)

        flash(u'form salvo com sucesso!', 'success')
        return redirect(url_for('thanks'))

    elif form.errors:
        flash(u'Temos algum erro no formulario.', 'error')

    context = {'form': form, 'journal': journal}

    return render_template("form.html", **context)


@app.route("/thanks/")
def thanks():
    return render_template('thanks.html')


@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')
