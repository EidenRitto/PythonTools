from requests_html import HTMLSession
import re


def geturl(cpage,lpage):
    session = HTMLSession()
    download_links = []
    while cpage <= lpage:
        url = 'http://51mtf.club/index.php/page/' + str(cpage)
        r = session.get(url)
        links = r.html.absolute_links
        for i in links:
            if re.search('filemarkets', i):
                download_links.append(i)
        cpage += 1
    return download_links


link_list = geturl(121, 121)
for j in link_list:
    print(j)
