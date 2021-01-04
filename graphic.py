from matplotlib import pyplot as plt
import tools

#显示价格的频数分布直方图 num：数据条数  d: 组距 scope: 价格范围
def priceGraph(num,d,scope):
    prices = tools.getprices(num)
    plt.hist(x=prices, bins=int((max(prices)-min(prices))/d))
    plt.xlim(scope[0],scope[1])
    plt.show()


#显示价格与销量关系图 --未完成 待数据库结构优化
def price_comm_graph(num,scope):
    data = tools.price_comm_data(num,scope)
    prices = list(data.keys())
    comms = list(data.values())
    plt.plot(prices,comms,'bo')
    plt.show()
