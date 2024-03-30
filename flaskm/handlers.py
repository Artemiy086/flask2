from flask import render_template, redirect, Blueprint


bp = Blueprint("users", __name__, url_prefix="")


@bp.route("/")
def index():
    return render_template("index.html", title="Главная")


@bp.route("/choice/<planet_name>")
def planet_name(planet_name):
    params = {"марс": [{"class": "bg-successful", "title": "Эта планета близка к Земле;"}, {"class": "bg-danger", "title": "На ней много необходимых ресурсов;"},
                       {"class": "bg-warning", "title": "На ней есть вода и атмосфера;"}, {"class": "bg-primary", "title": "На ней есть небольшое магнитное поле;"}]}
    params = params.get(planet_name.lower().strip())
    if params is None:
        params = [{"class": None, "title": "На введенную планету нет экспедиций"}]

    return render_template("choice.html", title="Выбор", params=params, planet_name=planet_name.capitalize())
