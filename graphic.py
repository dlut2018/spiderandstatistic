import sqlite3
from matplotlib import pyplot as plt
import tools

#显示价格的频数分布直方图 num：数据条数  d: 组距 scope: 价格范围
def priceGraph(num,d,scope):
    prices = tools.getprices(num)
    plt.hist(x=prices, bins=int((max(prices)-min(prices))/d))
    plt.xlim(scope[0],scope[1])
    plt.show()


priceGraph(1000,10,(0,300))
