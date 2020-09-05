# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/5 12:17
# 文件名称 : 03-验证用户输入的数据.PY
# 开发工具 : PyCharm

# 对输入数据的判断,如输入数据为零、数字、字母等
def inputbox(showstr, showorder, lengh):
    instr = input(showstr)
    if len(instr) != 0:
        if showorder == 1:
            if str.isdigit(instr):
                if instr == '0':
                    print("\033[1;31;40m 输入为零,请重新输入！！\033[0m")
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法,请重新输入！！\033[0m")
                return "0"
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != 3:
                    print("\033[1;31;40m必须输入三个字母,请重新输入\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法,请重新输入！！\033[0m")
                return "0"
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != lengh:
                    print("\033[1:31:40m必须输入" + str(lengh) + "个数字,请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法,请重新输入!!\033[0m")
                return "0"
    else:
        print("\033[1;31;40m输入为空,请重新输入!!\033[0m")
        return "0"


a = inputbox('请输入数据为零、数字、字母等：', 3,2)
print('返回值为:', a)


#方法2：通过字符的ASCII码进行验证
instr=input('请输入5位数字验证码：').strip(' ')   # 获取输入的5位数字
isgo='go'                                         # 是否登录的标记
if len(instr)!=5:                                 # 如果输入的字符（数字）长度不是5时
    print('输入非5位数字，请重新输入！')
    isgo = 'no'
else:
    for i in instr:
        if ord(i) not in range(ord('1'),ord('8')):         # 如果输入字符的ASCII码值为数字字符时
            print('输入了非数字字符，请重新输入！')
            isgo = 'no'
            break
if isgo =='go':                                             # 验证成功输出登录
    print('正在登录站长之家系统！')
