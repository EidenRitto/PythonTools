#!/usr/bin/python3

import pymysql

from translate.langconv import Converter

'''
   将sentence中的繁体字转为简体字
   :param sentence: 待转换的句子
   :return: 将句子中繁体字转换为简体字之后的句子
   '''
def Traditional2Simplified(sentence):
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

'''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


# 打开数据库连接
db = pymysql.connect("192.168.8.170", "root", "root", "inxedu_customer_fanwangkeji_wx")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用 execute()  方法执行 SQL 查询所有表格名
# cursor.execute("select table_name from information_schema.tables WHERE table_schema='inxedu_customer_fanwangkeji_wx'")
#
# # 使用 fetchall() 方法获取所有数据.
# table_names = cursor.fetchall()

# 通过表名查询所有字段
cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name = 'edu_address';")
column_names = cursor.fetchall()
# 获取表格主键名称
key_name = column_names[0][0]
# 查询主键所有的值
cursor.execute("SELECT "+key_name+" FROM `edu_address`")
key_values=cursor.fetchall()

for key_value in key_values:
    for i in range(len(column_names)):
        if i != 0:
            sql = "SELECT " + column_names[i][0] + " FROM `edu_address` WHERE " + key_name + " ='" + str(key_value[0]) + "';"
            cursor.execute(sql)
            column_content = cursor.fetchone()[0]
            print("简体：", column_content)
            # 将简体名字转换成繁体
            columnContent = Simplified2Traditional(str(column_content))
            print("繁体：", columnContent)

            # SQL 更新语句
            sql = "UPDATE edu_address SET " + column_names[i][0] + " = '" + columnContent + "' WHERE " + key_name + " = " + str(key_value[0])
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()

#
# 将简体名字转换成繁体
# columnContent = Simplified2Traditional("{'privateKey':'','publicKey':'','merchantNo':''}")
# print(columnContent)
# #将繁体名字转换成简体
# columnContent = Traditional2Simplified(columnContent)
# print(columnContent)
#


# 关闭数据库连接
db.close()
