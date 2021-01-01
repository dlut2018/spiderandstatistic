from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
#全局变量
num = 0
conn = sqlite3.connect("test.db")
cursor =conn.cursor()

#1、选择谷歌浏览器  2、输入京东网站 4、输入关键字   4、点击回车

def spider(url,keyword,search_info):
    driver = webdriver.Chrome()
    driver.get(url)
    input_tag = driver.find_element_by_id(keyword)
    input_tag.send_keys(search_info)
    input_tag.send_keys(Keys.ENTER)
    time.sleep(5)
    get_goods(driver)

#定位商品的数据并进行抓取
def get_goods(driver):
     global num
     global cursor
     global conn
     goods = driver.find_elements_by_class_name('gl-item')#查找多节点
     for good in goods:
         num = num +1
         name = 'null'
         price = 'null'
         evaluate = 'null'
         shopname = 'null'
         iconstext = 'null'
         link = good.find_element_by_tag_name('a').get_attribute('href')#获取属性
         if is_element_exit('.p-name em',good) !=0 :
             name = good.find_element_by_css_selector('.p-name em').text.replace('\n','')#获取商品名字
         if is_element_exit('.p-price i',good) !=0:
             price = good.find_element_by_css_selector('.p-price i').text#价格
         if is_element_exit('.p-commit a',good) != 0:
             evaluate = good.find_element_by_css_selector('.p-commit a').text#评论数
         if is_element_exit('.p-shop a',good) != 0:
             shopname = good.find_element_by_css_selector('.p-shop a').text#店铺名称
         if is_element_exit('.p-icons i',good) !=0:
             icons = good.find_elements_by_css_selector('.p-icons i')#售后保障 售后保障有多个项目 所以使用‘elements’
         #find_elements 可以返回一个列表（webelements类型）读取.text为所求
             iconstext=''
             for i in icons:
                 iconstext = iconstext+i.text+' '
         print(num)
         msg = '''
            商品：%s
            链接：%s
            价格：%s
            评论数：%s
            店铺名称：%s
            售后保障：%s
         '''%(name,link,price,evaluate,shopname,iconstext)
         print(msg)
         #将爬取到的信息写入数据库
         sql='''insert into goodsinfo 
         values(
         '%s',
         '%s',
         '%s',
         '%s',
         '%s',
         '%s')'''%(name,link,price,evaluate,shopname,iconstext)
         print(sql)
         try:
             cursor.execute(sql)
         except:
             pass
         conn.commit()
     button = driver.find_element_by_partial_link_text('下一页')
     button.click()
     time.sleep(1)
     get_goods(driver)

def is_element_exit(css,driver):
    s=driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        return 0#元素未找到
    elif len(s) == 1:
        return 1#找到一个元素
    else:
        return 2#找到多个元素
try:
    spider('https://www.jd.com/','key','男装')
except:
    print("本词条无法采集")
