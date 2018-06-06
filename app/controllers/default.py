from flask import render_template, flash, redirect, url_for
from app import app
from app.models.models import Question
from app.models.forms import QuestionsForm
import json

from flask import request


@app.route('/<issn>', methods=('GET', 'POST'))
def issn(issn):

    journal = Question.objects.get_or_404(issn=issn)

    form = QuestionsForm(**json.loads(journal.to_json()))

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

        mdata = json.loads(question.to_json())
        journal.update(**mdata)

        flash(u'form salvo com sucesso!', 'success')
        return redirect(url_for('thanks'))

    elif form.errors:
        flash(u'Temos algum erro no formulario.', 'error')

    journal = Question.objects.get_or_404(issn=issn)
    context = {
        'form': form,
        'journal': journal,
    }
    print(form.errors)
    return render_template("form.html", **context)


@app.route("/thanks/")
def thanks():
    return render_template('thanks.html')


@app.route("/index/", methods=["GET", "POST"])
@app.route("/")
def index():
    return render_template('index.html')
