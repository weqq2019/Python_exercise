# 编程锦囊

![Image text](https://raw.githubusercontent.com/weqq2019/Python_exercise/master/index.png)





## 第1章 核心基础应用

### 01-调用字符映射表输入特殊符号

- 解决方案：运行charmap

### 02-利用字符编码输入特殊符号

-     解决方案：查看HTML特殊字符编码对照表

### 03.实现日间、星期客流高峰提示

- 解决方案：采用各时间段业务同时除以某个基数，然后向上取整来量化数据。

### 03-2电信营业厅周业务分析的实现

### 04-模拟界面菜单功能中的方向键

- 解决方案：
通过正则表达式进行提取

### 05-动态循环输出数字

- 解决方案：
    sys.stdout.write("\r")        # 让光标回到行首
    sys.stdout.flush()            # 缓冲区d数据全部输出

### 05-2动态循环输出文字

###  06-如何实现多国语言文字输出

- 解决方案：根据各国语言文字与英语文字编码的关系，通过编程建立对应关联。

### 07-检索敏感词并描红输出

- 解决方案：通过使用count()方法进行查找与统计

### 08-采用自定义规则对列表进行顺序

- 解决方案：sort()方法进行顺序

### 09-利用lambda表达式简化编程

- 解决方案：lamdba表达式是起到一个函数速写的作用。

### 10-清洗字符串和列表

- 解决方案：使用strip()、lstrip()、rstrip()

### 11-拼接字符串、列表和字典

- 解决方案：
方法1："+"，
方法2："，"再join 
方法3：直接连接字符串
方法4：通过"%"

### 12-如何实现字符串与列表等数据的去重

- 解决方案：
方法1：通过for循环遍历字符串去重
方法2：通过while循环遍历字符串去重
方法3：使用列表的方法去重
方法4：在原字符串直接删除
方法5：使用formkey()方法把字符串转成字典

### 13-利用条形图显示分析数据

- 解决方案：
1.用字符作为图案输出横向条形图
2.用字符作为图案输出纵向条形图

## 第2章 字符串处理

### 01-中英文混排时对齐

- 解决方案：
处理公式：｛：<|>|^ x｝

### 02-实现数据编号的几种方法

- 解决方案：
1.利用zfill()
2.利用format()
3.

### 03-验证用户输入的数据

- 1.利用字符串的isalnum(),isalpha()等方法进行验证
2.通过字符的ASCII码进行验证

### 04-使用python逆序输出字符串

- 1.使用range(函数）
2.使用reversed()函数
3.倒序打印输出

### 05-如何生成虚拟姓名

- 解决方案：
首先要建立姓氏库、名字库

### 06-如何按照拼音顺序对中文汉字进行排序

- 默认按汉字的Unicode编码进行排序,需要借助第三方模拟xpinyin

### 07-如何生成高考填报志愿时的姓名区位码

- 解决方案：
使用encode()方法对汉字进行GB2312编码

### 08-如何使用MD5或SHA1等算法对用户密码进行加密

- 解决方案：
使用hashlib模块

### 09-比较两种字符串的拼接方法哪个更省时

- 从0开始的数字转换为字符串并依次连接,共循环10000次,然后计算其所用时间.

## 第3章_文件操作

