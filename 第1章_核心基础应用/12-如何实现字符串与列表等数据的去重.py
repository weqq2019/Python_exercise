# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/4 10:32
# 文件名称 : 12-如何实现字符串与列表等数据的去重.PY
# 开发工具 : PyCharm


#方法1：通过for循环遍历字符串去重
name='李於娟刘泉王建尢树刘泉尢树王建'
newname=''
for char in name:
    if char not in newname:
        newname+=char
print(newname)

#方法2：通过while循环遍历字符串去重
name='李於娟刘泉王建尢树刘泉尢树王建'
newname=''
i=len(name)-1
while True:
    if i>=0:
        if name[i] not in newname:
            newname+=name[i]
        i-=1
    else:
        break
print(newname)

#方法3：使用列表的方法去重
name='李於娟刘泉王建尢树刘泉尢树王建'
myname=set(name)
print(myname)
newname=list(myname)
print(newname)
print(''.join(newname))
newname.sort(key=name.index)
print(newname)
print(''.join(newname))

#方法4：在原字符串直接删除
name='李於娟刘泉王建尢树刘泉尢树王建'
i=len(name)
for s in name:
    if name[0] in name[1:i]:
        name=name[1:i]
    else:
        name=name[1:i]+name[0]
print(name)
#方法5：使用formkey()方法把字符串转成字典
name='李於娟刘泉王建尢树刘泉尢树王建'
zd={}.fromkeys(name)
print(zd)
mylist=list(zd.keys())
print(mylist)
print(''.join(mylist))

#2.列表的去重方法
city=['上海','广州','上海','重庆','重庆','北京','重庆','上海']
#方法1:for 循环语句（不改变原来顺序)
ncity=[]
for item in city:
    if item not in ncity:
        ncity.append(item)
print(ncity)

#方法2：set方法（改变原来顺序)
ncity=list(set(city))
print(ncity)

#方法3:set方法（不改变原来顺序）
ncity=list(set(city))
ncity.sort(key=city.index)
print(ncity)

#方法4:cont()方法统计并删除,需要先排序（改变原来顺序）
city.sort()
print(city)
for x in city:
    while city.count(x)>1:
        del city[city.index(x)]
print(city)

#方法5：把列表转成字典
city=['上海','广州','上海','重庆','重庆','北京','重庆','上海']
mylist=list({}.fromkeys(city).keys())
print(mylist)
