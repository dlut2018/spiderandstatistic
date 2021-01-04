import sqlite3

clause_dict = {0:'包邮', 1:'折扣', 2: '京东物流', 3: '满减',
               4: '优惠券', 5: '自营', 6: '新品'}


#获取单列数据
def getDatas(label,num=None):
    sql = "select " + str(label) + " from goodsinfo"
    if num != None:
        sql = sql + " limit 1," + str(num)
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    print(sql)
    c.execute(sql)
    data = c.fetchall()
    conn.close()
    return data

#获取num条价格数据，返回float类型列表
def getprices(num=None):
    prices = getDatas('goodprice',num)
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

#获取评论数列表 返回整数列表 --- 待优化
def getComms(num):
    comms = getDatas('goodevnum',num)
    # 数据处理
    for i in range(0, len(comms)):
        comms[i] = handleComm(comms[i])
    return comms

#获得价格与评论数字典
def price_comm_data(scope,num=None):
    data = {}
    prices = getprices(num)
    comms = getComms(num)

    for i in range(0,len(prices)):
        if prices[i]>=scope[0] and prices[i]<=scope[1]:
            data[prices[i]] = data.get(prices[i],0) + comms[i]
    return data


#获取一些优惠对应的店铺数
def clause_num(num=None):
    icons = getDatas('goodicons',num)
    clauses = [0,0,0,0,0,0,0]
    for i in range(len(icons)):
        if str(icons[i]).find('邮') != -1:
            clauses[0] = clauses[0] + 1
        if str(icons[i]).find('折') != -1:
            clauses[1] = clauses[1] + 1
        if str(icons[i]).find('京东') != -1:
            clauses[2] = clauses[2] + 1
        if str(icons[i]).find('满') != -1:
            clauses[3] = clauses[3] + 1
        if str(icons[i]).find('券') != -1:
            clauses[4] = clauses[4] + 1
        if str(icons[i]).find('自营') != -1:
            clauses[5] = clauses[5] + 1
        if str(icons[i]).find('新品') != -1:
            clauses[6] = clauses[6] + 1
    return clauses

