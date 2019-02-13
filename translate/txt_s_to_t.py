from translate.langconv import Converter


# 将sentence中的繁体字转为简体字
# :param sentence: 待转换的句子
# :return: 将句子中繁体字转换为简体字之后的句子

def Traditional2Simplified(sentence):
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

# 将sentence中的简体字转为繁体字
# :param sentence: 待转换的句子
# :return: 将句子中简体字转换为繁体字之后的句子

def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


with open("./zh-cn.js", 'r', encoding='UTF-8') as rf:
    lines = rf.readlines()

with open('./zh-tw.js', 'w', encoding='UTF-8') as wf:
    for line in lines:
        wf.write(Simplified2Traditional(line))
