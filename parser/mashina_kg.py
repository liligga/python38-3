import httpx
from parsel import Selector
from pprint import pprint
# from bs4 import BeautifulSoup


MAIN_URL = "https://www.mashina.kg/search/all/"
BASE_URL = "https://www.mashina.kg"

def get_html(url):
    response = httpx.get(url)
    # return response.text
    return Selector(response.text)

def get_title(html):
    title = html.css("title::text").get()
    return title

def get_car_links(html):
    cars = html.css(".list-item a::attr(href)").getall()
    links = list(map(lambda x: BASE_URL + x, cars))
    return links

if __name__ == "__main__":
    html = get_html(MAIN_URL)
    # print(html[:400])
    title = get_title(html)
    # print(title)
    links = get_car_links(html)
    pprint(links)

