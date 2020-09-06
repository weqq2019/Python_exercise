# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/6 12:53
# 文件名称 : 06-如何按照拼音顺序对中文汉字进行排序.PY
# 开发工具 : PyCharm
from xpinyin import Pinyin
def my_sort(wordlist):
    pin=Pinyin()
    temp=[]
    for item in wordlist:
        temp.append((pin.get_pinyin(item),item))
    temp.sort()
    result=[]
    for i in range(len(temp)):
        result.append(temp[i][1])
    return result

print(my_sort(['华为','小米','苹果','三星','阿里']))