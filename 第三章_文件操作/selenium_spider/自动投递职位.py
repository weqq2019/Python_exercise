# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/9 21:15
# 文件名称 : 自动投递职位.PY
# 开发工具 : PyCharm

# 导入seleinum的webdriver接口
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

import xlrd
import xlwt
count1=0
count2=0
def readexcel():
    workbook=xlrd.open_workbook(r"E:\02_归零叔\01_必须打造核心竞争力\Python编程锦囊\Python_exercise\第三章_文件操作\spider\Yuanjisong\Yuanjisong\spiders\Excel爬虫最终测试.xls")
    # print(workbook.sheet_names())
    sheet2=workbook.sheet_by_name('爬虫表')
    nrows=sheet2.nrows
    ncols=sheet2.ncols
    # print(nrows,ncols)

    cell_A=sheet2.cell(1,0).value#取出第X行第X列的值
    # print(cell_A)

    clou = sheet2.col_values(0)  # 读取第一列
    # print(clou)
    return clou

#实例化谷歌设置选项
option = webdriver.ChromeOptions()
#添加保持登录的数据路径：安装目录一般在C:\Users\黄\AppData\Local\Google\Chrome\User Data
option.add_argument(r"user-data-dir=C:\Users\Alienware\AppData\Local\Google\Chrome\User Data")

#初始化driver
browser = webdriver.Chrome(options=option)

#获取链接
list=readexcel()
# print(list)

for i in range(1,len(list)):
    # 创建浏览器对象
    browser.get(list[i])
    # time.sleep(5)
    # browser.get('https://www.yuanjisong.com/job/106370')
    try:
        browser.find_element_by_link_text('投递职位').click()
        time.sleep(1)
        browser.find_element_by_link_text('确认投递').click()
        time.sleep(3)
        count1+=1
    except:
        count2+=1
print("投了"+str(count1)+"个")
print("早投了"+str(count2)+"个")
print("共投了",count1+count2)

