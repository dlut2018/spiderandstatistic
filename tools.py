import sqlite3

#获取num条价格数据，返回float类型列表
def getprices(num):
    #读取数据库
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "select goodprice from goodsinfo limit 1, " + str(num)
    c.execute(sql)
    prices = c.fetchall()
    conn.close()

    #数据处理
    for i in range(0, len(prices)):
        prices[i] = float(str(prices[i])[2:-3])

    return prices
