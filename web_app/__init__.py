from flask import Flask, render_template

from web_app.weather import weather_by_city
from web_app.lifehacker_ru_news import get_news


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    @app.route('/')
    def index():
        title = 'Новости'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = get_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    return app
