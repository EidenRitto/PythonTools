import replace_translate_java_file as rt
import re


with open(
        "C:\\Users\\30371\\IdeaProjects\\lyg_card_system\\lygMakeCard\\src\\config\\language\\zh_CN.properties"
        , 'r', encoding='UTF-8') as f:
    lines = f.readlines()
with open(
            "C:\\Users\\30371\\IdeaProjects\\lyg_card_system\\lygMakeCard\\src\\config\\language\\zh_CN_Ko.properties"
        , 'w', encoding='utf-8')as nf:
    for line in lines:
        try:
            enline = re.search('^(.+)=', line).group(0)
            cnline = re.search('=(.+)', line).groups()[0]
            koline = rt.translate(cnline, 'zh', 'kor')[0]['dst']
            nf.write(enline + koline + '\n')
        except Exception as e:
            print(e)

