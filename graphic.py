from matplotlib import pyplot as plt
import tools
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#显示价格的频数分布直方图 num：数据条数  d: 组距  scope: 价格范围
def price_graph(scope,d=30,num=None):
    prices = tools.getprices(num)
    plt.hist(x=prices, bins=int((max(prices)-min(prices))/d))
    plt.xlim(scope[0],scope[1])
    plt.show()


#显示价格与评论数关系图 scope:价格范围  num:数据条数
def price_comm_graph(scope,num=None):
    data = tools.price_comm_data(scope,num)
    prices = list(data.keys())
    comms = list(data.values())
    plt.plot(prices,comms,'bo')
    plt.show()

#绘制各个优惠政策店铺个数柱状图 num:数据条数
def clause_num_graph(num=None):
    clauses = tools.clause_num(num)
    plt.bar([tools.clause_dict[i] for i in range(7)],clauses)
    plt.show()

