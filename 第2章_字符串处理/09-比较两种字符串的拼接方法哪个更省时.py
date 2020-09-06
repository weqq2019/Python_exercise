# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/6 13:34
# 文件名称 : 09-比较两种字符串的拼接方法哪个更省时.PY
# 开发工具 : PyCharm
import datetime
#测试方法一的执行时间
st=datetime.datetime.now()
#"开始字符串拼接"
s=''
for i in range(0,10000):
    s+=str(i)
#"结束字符串拼接"
et=datetime.datetime.now()
print(et-st)

#测试方法二
st2=datetime.datetime.now()
s=[]
for i in range(1,10000):
    s.append(str(i))
"".join(s)
et2=datetime.datetime.now()
print(et2-st2)

print("运行结果中可以看出：方法二的用时更少,所以推荐使用方法2进行字符串的拼接")