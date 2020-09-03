# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/3 10:33
# 文件名称 : 10-清洗字符串和列表.PY
# 开发工具 : PyCharm

#方法1
username='    明日科技'
print(username.strip())

word='刘 王 李 孙 周 天 郑 王'
word=''.join((i.strip(' ')for i in word))
print(word)

#方法2
word='编号    姓名           性别  年级              学校      奖项'
list=word.split(' ')
print(list)
listnew=[i for i in list if i!='']
print(listnew)
new=' '.join(listnew)
print(new)

#方法3
#使用replace()方法
word='D:\mingrisoft\python\t'
new=word.replace('\t', '')
print(new)

#方法4#
#使用列表推导式
word='刘 王 李 孙 周 天 郑 王'
word=''.join([i for i in word if i!=' '])
print(word)

#方法5
#利用切片删除单个固定位置的字符
name='伦纳德：31.2'
print(name[:3]+name[4:])

#方法6
#去除列表中的空元素
nba='哈登：31.6 伦纳德：31.2      乔治：28.6     库里：27.3      利拉德26.9'
nbanew=nba.split(' ')
nbaone=[i for i in nbanew if i!='']
print(nbaone)

