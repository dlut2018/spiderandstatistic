import statistics
import sqlite3
import matplotlib
import numpy as np
import pylab as p
import pandas as pa
import jieba
import string
#全局变量声明列表类型
ans = []
#函数声明-------------------------------------------------------------------------
#处理商品名称字符串 提取商品名称字符串中的词，返回一个汉语词语的列表
def sps_1(str_in):
    str_out = list(jieba.cut(str_in))
    return str_out
#处理价格字符串 将字符串类型的价格转化为float类型
def sps_2(str_in):
    float_out = float(str_in)
    return float_out
#处理评论数字符串 将字符串类型的评论数转化为int类型
def sps_3(str_in):
    target = str(str_in)
    #第一步判断字符串是否为空
    if len(target) == 0:
        return 0
    #第二步先去加号
    if target.find('+') == -1:
        pass
    else:
        str_in = str_in[:-1]
    #第三步处理字符串中的万
    if target.find('万') == -1:
        return int(str_in)
    else:
        str_in = str_in[:-1]
        temp = float(str_in)
        return int(temp*10000)
#处理店铺名称字符串
def sps_4(str_in):
    return str_in

#处理服务条款字符串 将字符串类型的服务条款转化为服务条款列表
def sps_5(str_in):
    return str(str_in).split(' ')


#连接数据库，并将数据从数据库导入到datalist中------------------------------------
conn = sqlite3.connect("test.db")
couser = conn.cursor()
sql = "select * from goodsinfo"
couser.execute(sql)
conn.commit()
datalist = couser.fetchall()


#数据的预处理--------------------------------------------------------------------


datalist_s = []
for i in datalist:
    datalist_temp=[]
    datalist_temp.append(sps_1(i[0]))
    datalist_temp.append(sps_2(i[2]))
    datalist_temp.append(sps_3(i[3]))
    datalist_temp.append(sps_4(i[4]))
    datalist_temp.append(sps_5(i[5]))
    datalist_s.append(datalist_temp)

for i in datalist_s:
    print(i)

#进行统计--------------------------------------------------------------------

#词频统计 统计十大高频词 以及高频词出现频率的直方图 （出现频率高于2000次则为高频词) 绘制前十名高频词的饼图和高频词出现的频率分布直方图
dict = {}
for i in datalist_s:
    for j in i[0]:
        if dict.get(j,"null") == "null":
            temp = { j : 1}
            dict.update(temp)
        else:
            dict[j] = dict[j]+1

temp_1 = dict.items()
temp_2 =[]
for i in temp_1:
    if i[1] > 2000 and i[0] != " " and i[0] != "（" and i[0] != "）":
        temp_2.append(i)
print(temp_2)
temp_3 = []
#获取前十名的高频词
for i in temp_2:
    if len(temp_3) < 10:
        temp_3.append(i)
    else:
        temp_4 = ('',-1)
        for j in range(10):
            #先对temp_3进行冒泡排序
            for k in range(9-j):
                if temp_3[k][1] < temp_3[k+1][1] :
                    temp_4 = temp_3[k]
                    temp_3[k] = temp_3[k+1]
                    temp_3[k+1] = temp_4
            #如果当前的元组>temp_3中元组最小值 则把最小值替换掉
            if i[1] > temp_3[9][1] :
                temp_3[9] = i
#画图


#对价格进行统计分析 计算价格的平均数，绘制价格的频率分布直方图




#为了分析价格和销量（评论数）的关系，绘制价格评论数曲线




#对店铺信息进行统计，统计十佳店铺，并且画出销售额饼图




#对服务条款（icons）进行统计，画出每个服务条款条款对应的店铺数

#aaa




