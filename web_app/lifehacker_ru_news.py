import requests
from bs4 import BeautifulSoup


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
        result_news = []
        for news in all_news:
            title = news.find('h2', class_="flow-post__title").text
            url = news.find('a')['href']
            body = news.find('p', class_="flow-post__excerpt").text
            result_news.append({
                "title": title,
                "url": url,
                "body": body
            })
        return result_news
    return False
