# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/8 13:13
# 文件名称 : 06-如何对读取的文件内容进行分词.PY
# 开发工具 : PyCharm
import jieba
filepath=input("请输入要读取的文件： ")#记录输入的文件路径
with open(filepath,encoding='utf-8') as f:
    words=jieba.lcut(f.read())
    print(words)
