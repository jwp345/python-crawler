from bs4 import BeautifulSoup

html = '''
<td class="title black">
    <div class="tit3 white" data-no='10'>
        <a href="/movie/bi/mi/basic.nhn?code=189069" title="다만 악에서 구하소서">다만 악에서 구하소서</a>
    </div>
</td>
'''


# 1. tag 조회
def ex01():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)

    tag_td = bs.td
    # print(tagTd)

    # tag_a = bs.a
    tag_a = tag_td.a
    # print(tag_a)

    # None
    tag_h4 = bs.td.h4
    print(tag_h4)


# 2. attribute 값 가져오기
def ex02():
    bs = BeautifulSoup(html, 'html.parser')

    tag_td = bs.td
    print(tag_td['class'])

    tag_div = bs.div
    # error
    # print(tag_div['id'])
    print(tag_div.attrs)


# 3. attribute로 조회하기
def ex03():
    bs = BeautifulSoup(html, 'html.parser')
    tag_td = bs.find('td', attrs={'class': ['title', 'black']})
    print(tag_td)

    tag_div = bs.find(attrs={'data-no': '10', 'class': 'tit3'})
    print(tag_div)


if __name__ == '__main__':
    # ex01()
    # ex02()
    ex03()
