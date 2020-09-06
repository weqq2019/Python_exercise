# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/6 13:22
# 文件名称 : 08-如何使用MD5或SHA1等算法对用户密码进行加密.PY
# 开发工具 : PyCharm

import hashlib
str2=input("请输入要加密的字符串：")
#MD5加密（返回32位十六进制字符串）
md5=hashlib.md5()
md5.update(str2.encode('utf-8'))
print('MD5加密：',md5.hexdigest())
print(str(len(md5.hexdigest()))+'位')