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

#处理从数据库中读取的评论数字符串 返回整数
def handleComm(comm_str):
    target = str(comm_str)

    if len(target) == 0:
        return 0

    #去掉前后的无关符号
    target = target[2:-3]

    #去加号
    if target.find('+') != -1:
        target = target[:-1]

    #处理'万'
    if target.find('万') != -1:
        target = target[:-1]
        return int(float(target)*10000)

    if target =='':
        return 0

    return int(float(target))

#获取评论数列表 --- 待优化
def getComms(num):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "select goodevnum from goodsinfo limit 1," + str(num)
    c.execute(sql)
    comms = c.fetchall()
    conn.close()
    # 数据处理
    for i in range(0, len(comms)):
        comms[i] = handleComm(comms[i])
    return comms

#获得价格与评论数字典
def price_comm_data(num,scope):
    data = {}
    prices = getprices(num)
    comms = getComms(num)

    for i in range(0,len(prices)):
        if prices[i]>=scope[0] and prices[i]<=scope[1]:
            data[prices[i]] = data.get(prices[i],0) + comms[i]
    return data
