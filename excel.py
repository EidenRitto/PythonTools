from requests_html import HTMLSession
import re
import pandas as pd
from pandas import Series


def geturl(cpage,lpage):
    session = HTMLSession()
    data = []
    while cpage <= lpage:
        url = 'http://51mtf.club/index.php/page/' + str(cpage)
        results = session.get(url).html.find('body > div#wrapper > div#content > div > div.entry > p ')
        for result in results:
            try:
                mytext = re.search('(【资源名称】.*)\n', result.text).group(1)
            except:
                mytext = ''
            linklist = result.absolute_links
            if len(linklist) == 0:
                mylink = ''
            else:
                mylink = []
            for link in linklist:
                if re.search('filemarkets', link):
                    mylink.append(link)
            if mytext != '':
                data.append(mytext)
                # print(mytext)
            if mylink != '':
                data.append(mylink)
                # print(mylink)
        cpage += 1
        print("加载第"+str(cpage)+"页数据中……请稍后")
    return data


pf = pd.DataFrame(Series(geturl(101, 200)))
# pf.columns = ['标题', '地址']
pf.to_csv('output101-200.csv', encoding='utf-8', index=False)
# /html/body/div[3]/div[1]/div[1]/div[3]/p/br[1]
# /html/body/div[3]/div[1]/div[2]/div[3]/p/br[1]
