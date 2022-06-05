from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.model import db, News

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    return app


    """ Запустим сервер
Раньше для запуска сервер нам нужно было просто запустить файл server.py. Теперь процедура запуска немного изменилась. Мы будем запускать немного сложнее:

Linux и Mac: export FLASK_APP=webapp && export FLASK_ENV=development
            && flask run
Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run """