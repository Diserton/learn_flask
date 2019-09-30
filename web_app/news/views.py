from flask import Blueprint, current_app, render_template

from web_app.news.models import News
from web_app.weather import weather_by_city


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'Новости'
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=title, weather=weather, news_list=news_list)
