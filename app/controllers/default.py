# coding: utf-8
import json
import datetime
from app import app
from app.models.models import Question
from app.models.forms import QuestionsForm

from flask import render_template, flash, redirect, url_for, request


@app.route('/<issn>', methods=('GET', 'POST'))
def issn(issn):

    journal = Question.objects.get_or_404(issn=issn)

    form = QuestionsForm(**json.loads(journal.to_json()))

    if form.validate_on_submit():

        form.populate_obj(journal)

        if request.method == "POST" and form.validate():

            result = request.form.to_dict()
            result['update_date'] = datetime.datetime.now()
            result['accessed'] = 1

        journal.update(**result)

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
