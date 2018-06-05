from flask import render_template, flash  # redirect, url_for
# from flask_login import login_user, logout_user
from app import app
from app.models.models import Post
from app.models.forms import PostForm


# @lm.user_loader
# def load_user(id):
#     return User.query.filter_by(id=id).first()


@app.route("/index/", methods=["GET", "POST"])
@app.route("/")
def index():
    return render_template('index.html')


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
