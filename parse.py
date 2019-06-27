from multiprocessing import Pool
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def get_html(url):
	headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    response = requests.get(url, headers = headers)
    return response.text


def text_before_word(text, word):
    line = text.split(word)[0].strip()
    return line


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = text_before_word(soup.find('search_results_item   search_results_item--media').text, 'price')
    except:
        name = ''
    data = {'name': name}
    return data


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name']))
        print(data['name'], 'parsed')


def main():
    start = datetime.now()
    url = 'https://www.kommersant.ru/search/results?places=&categories=&datestart=12.05.2018&dateend=12.06.2019&sort_type=1&regions=&results_count=&page=1&search_query=ооо+газпром'
    # all_links = get_all_links(get_html(url))
    html = get_html(url)
	data = get_page_data(html)
	write_csv(data)
    end = datetime.now()
    total = end - start
    print(str(total))


if __name__ == '__main__':
    main()





