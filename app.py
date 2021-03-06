from flask import Flask, render_template

import data as dt

app = Flask(__name__)
tours = dt.tours
departures = dt.departures


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', departures=departures, tours=tours)


@app.route('/departures/<departure>/')
def departures_view(departure):
    temp = {key: value for key, value in tours.items() if value["departure"] == departure}
    if departure not in departures:
        return render_not_found(404)
    return render_template('departure.html', departures=departures, tours=temp)


@app.route('/tours/<int:id>/')
def tours_view(id):
    if id not in tours:
        return render_not_found(404)
    return render_template('tour.html', departures=departures, tours=tours, id=id)


@app.errorhandler(404)
def render_not_found(error):
    return f"<h1>Ничего не нашлось! Вот неудача, отправляйтесь на главную!</h1><h2>Ошибка {error}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
