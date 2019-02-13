import pymysql

# # 打开数据库连接
# db = pymysql.connect("192.168.8.67", "phpdb", "pdb2468", "vcos_lyg")
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# sql = "SELECT sync_tab_name FROM sync"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         tab_name = row[0]
#         # 打印结果
#         print("tab_name=%s" % \
#              (tab_name))
# except:
#     print("Error: unable to fetch data")
# # 关闭数据库连接
# db.close()

#!/usr/bin/python3

# 打开数据库连接
db = pymysql.connect("192.168.8.67", "phpdb", "pdb2468", "vcos_lyg")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询所有表格名
cursor.execute("SELECT sync_tab_name FROM sync")

# 使用 fetchall() 方法获取所有数据.
table_names = cursor.fetchall()

for row in table_names:
    table_name =row[0]
    sql = "SELECT column_name" +\
          " FROM INFORMATION_SCHEMA.`KEY_COLUMN_USAGE`" +\
          " WHERE table_name=\"" + str(table_name) + "\"" +\
          " AND CONSTRAINT_SCHEMA=\"vcos_lyg\"" +\
          " AND constraint_name=\"PRIMARY\""
    # 使用 execute()  方法执行 SQL 查询所有表格主键
    cursor.execute(sql)
    key = cursor.fetchone()[0]
    print("table_name="+str(table_name)+'key='+str(key))



# 关闭数据库连接
db.close()