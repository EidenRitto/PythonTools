from requests_html import HTMLSession
from urllib.request import urlretrieve
import urllib

# 雀魂表情下载

session = HTMLSession()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# opener = urllib.request.build_opener()
# opener.addheaders = headers
# urllib.request.install_opener(opener)
url = 'https://zh.moegirl.org/雀魂麻将'
csspath = 'div#mw-content-text > div.mw-parser-output > div '
csspath2 = 'div.TabContentText '
html = session.get(url)
result = html.html.find(csspath)
results = result[2].find('img')
for res in results:
    imgurl = res.attrs.get('src')
    imgname = 'pic/' + res.attrs.get('alt') + ".jpg"
    try:
        req = urllib.request.Request(imgurl, headers=headers)
        data = urllib.request.urlopen(req).read()
        with open(imgname, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))
    # urlretrieve(imgurl, imgname)
