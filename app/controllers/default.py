from flask import render_template, flash  # redirect, url_for
# from flask_login import login_user, logout_user
from app import app
from app.models.models import Post, Question
from app.models.forms import PostForm, QuestionsForm
import json

# @lm.user_loader
# def load_user(id):
#     return User.query.filter_by(id=id).first()


@app.route("/index/", methods=["GET", "POST"])
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<issn>', methods=('GET', 'POST'))
def issn(issn):
    form = QuestionsForm()
    if form.validate_on_submit():

        journal = Question.objects.get_or_404(issn=issn)

        question = Question(
            criterio1a=form.data['criterio1a'],
            justifica1a=form.data['justifica1a'],
            )

        mdata = json.loads(question.to_json())

        journal.update(**mdata)
        flash(u'form salvo com sucesso!', 'success')
    elif form.errors:
        flash(u'Temos algum erro no formulario.', 'error')
    journal = Question.objects.get_or_404(issn=issn)
    context = {
        'form': form,
        'journal': journal,
    }
    # print(journal.title)
    return render_template("issn.html", **context)


@app.route('/home', methods=('GET', 'POST'))
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.data['title'],
            content=form.data['content'])
        post.save()
        flash(u'form salvo com sucesso!', 'success')
    elif form.errors:
        flash(u'Temos algum erro no form', 'error')

    posts = Post.objects.all()
    context = {
        'form': form,
        'posts': posts,
    }
    print(posts)
    return render_template("home.html", **context)


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         print(user)
#         if user and user.password == form.password.data:
#             login_user(user)
#             flash("Logged In")
#             return redirect(url_for("index"))
#         else:
#             flash("Invalid Login")

#     return render_template('login.html', form=form)


# @app.route("/logout")
# def logout():
#     logout_user()
#     flash("Logged out.")
#     return redirect(url_for("index"))


# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info": None})
# def teste(info):
#     r = User.query.filter_by(username="juliarizza").first()
#     # db.session.delete(r)
#     # db.session.commit()
#     print(r)
#     return "Ok"

# @app.route("/test", defaults={'name': None})
# @app.route("/test/<name>")
# def test(name=None):
#     if name:
#         return "Ola, %s!" % name
#     else:
#         return "Olá, usuário!"
