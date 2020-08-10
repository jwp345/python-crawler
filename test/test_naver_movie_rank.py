from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    response = urlopen(request)
    html = response.read().decode('cp949')
    print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)

    for index, div in enumerate(divs):
        print(index, div.a.text, div.a['href'], sep=':')


# def proc_error(e):
#     print('crawling error', e)

def proc_naver_movie_rank(data):
    pass


def ex02():
    html = crawler.crawling(
        url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949')

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)

    for index, div in enumerate(divs):
        print(index, div.a.text, div.a['href'], sep=':')


if __name__ == '__main__':
    # ex01()
    ex02()
