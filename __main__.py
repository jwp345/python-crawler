from itertools import count

from bs4 import BeautifulSoup

from collection import crawler

import pandas as pd


def crawling_pelicana():
    results = []

    for page in count(start=1, step=1):
        url = 'http://www.pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': ['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[0:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)
            # print(name, address, sep=':')

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gigun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)


def crawling_nene():
    url = 'https://nenechicken.com/17_new/sub_shop01.asp?ex_select=1&ex_select2=&IndexSword=&GUBUN=A&page=1'
    html = crawler.crawling(url)
    print(html)


def crawling_goobne():
    pass


def crawling_kyochon():
    results = []

    for sido1 in range(1, 18):
        for sido2 in count(start=1, step=1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)
            html = crawler.crawling(url)

            if html is None:
                break

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})
            tags_span = tag_ul.findAll('span', attrs={'class': 'store_item'})

            for tag_span in tags_span:
                strings = list(tag_span.strings)

                name = strings[1]
                address = strings[3].strip('\r\n\t')
                sidogu = address.split()[0:2]

                t = (name, address) + tuple(sidogu)
                results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gigun'])
    table.to_csv('results/kyochon.csv', encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':
    # pelicana
    # crawling_pelicana()

    # nene
    # crawling_nene()

    # kyochon
    crawling_kyochon()

    # goobne
