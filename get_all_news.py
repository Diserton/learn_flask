from web_app import create_app
from web_app.lifehacker_ru_news import get_news

app = create_app()
with app.app_context():
    get_news()
