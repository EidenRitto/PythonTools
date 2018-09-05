import os
import re
import http.client
import hashlib
from urllib import parse
import random


def translate(text, f, t):
    appid = '20180904000202604'
    secretKey = 'kd5oAvzy683SfamH8CtY'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = text
    fromLang = f
    toLang = t
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        string = response.read().decode('utf-8')
        string = eval(string)
        for line in string['trans_result']:
            print(line['dst'] + '\n')
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return string['trans_result']


rootdir = 'C:\\Users\\30371\\IdeaProjects\\lyg_card_system\\lygMakeCard\\src\\com\\bs\\myJPanel'
listdir = os.listdir(rootdir)
conf = open("Chinese.properties", 'w', encoding='UTF-8')
listword = []
for i in range(0, len(listdir)):
    path = os.path.join(rootdir, listdir[i])
    if os.path.isfile(path):
        with open(path, 'r', encoding='UTF-8') as r:
            rline = r.readlines()
        with open(path, 'w', encoding='UTF-8') as w:
            for line in rline:
                try:
                    oldword = re.search('"[\u4e00-\u9fa5]+\"', line).group(0)
                except Exception as e:
                    oldword = ''
                if oldword != '':
                    newword = translate(oldword, 'zh', 'en')[0]['dst']
                    newword = newword.replace('.', '')
                    newword = newword.replace(' ', '_')
                    javaword = 'MyLanguageConfig.getInfo('+newword+')'
                    w.write(line.replace(oldword, javaword))
                    if oldword not in listword:
                        listword.append(oldword)
                        try:
                            conf.write(eval(newword) + "=" + eval(oldword) + "\n")
                        except Exception as e:
                            print(e)
                else:
                    w.write(line)
conf.close()
