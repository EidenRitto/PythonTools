from requests_html import HTMLSession
import re

# /79/79313/8381675.html 79/79100/8362760.html
# /86/86996/8985228.html 9/9208/652276.html
# 76/76118/8125422.html
session = HTMLSession()
data = ''
page = 1
url_before = 'https://www.toptxtb.com/toptxt/76/76118/'
url_mid = '8125422.html'
while True:

    url = url_before + url_mid
    # results = session.get(url).html.find('body > div#wrapper > div#content > div > div.entry > p ')

    next_url = session.get(url).html.find('body > div#wp.wp > div#content > div.novel_head > div.novel_bottom > a')[2].links
    for key in next_url:
        url_mid = key

    results = session.get(url).html.find('body > div#wp.wp > div#content > div#novel_content')
    for result in results:
        # try:
        #     print(result.text)
        #     # mytext = re.search('(【资源名称】.*)\n', result.text).group(1)
        # except:
        #     mytext = ''

        data += result.text
    print("加载第"+str(page)+"页数据中……请稍后")
    page = page + 1
    if url_mid == './':
        break

# print("加载第"+str+"页数据中……请稍后")
with open('白.txt', 'w', encoding='utf-8') as f:
    f.write(data)
