import requests
from datetime import datetime
from bs4 import BeautifulSoup
from web_app.db import db
from web_app.news.models import News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Ошибка!")
        return False


def get_news():
    html = get_html("https://lifehacker.ru/topics/news/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.findAll('div', class_='flow-post')
        for news in all_news:
            title = news.find('h2', class_="flow-post__title").text
            url = news.find('a')['href']
            text = news.find('p', class_="flow-post__excerpt").text
            now = datetime.now().strftime('%Y-%m-%d')
            published = datetime.strptime(now, '%Y-%m-%d')
            save_news(title, url, published, text)


def save_news(title, url, published, text):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published, text=text)
        db.session.add(new_news)
        db.session.commit()
