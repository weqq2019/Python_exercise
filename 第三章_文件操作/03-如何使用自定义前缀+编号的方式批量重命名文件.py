# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/7 12:51
# 文件名称 : 03-如何使用自定义前缀+编号的方式批量重命名文件.PY
# 开发工具 : PyCharm
import os  # 导入os模块

while True:  # 循环输入
    path = input('请输入要重命名的文件所在路径：')  # 记录输入的路径
    try:
        list = os.listdir(path)  # 遍历选择的文件夹
        num = 0  # 记录文件数量
        for i in range(0, len(list)):  # 遍历文件列表
            filepath = os.path.join(path, list[i])  # 记录遍历到的文件名
            if os.path.isfile(filepath):  # 判断是否为文件
                filetype = os.path.splitext(filepath)[1]  # 获取获取名
                template = '{:0>3d}'
                # 根据模板、起始编号和增量值生成新文件名
                newfilename = '黑飘' + template.format(num + 1) + filetype
                newfilepath = os.path.join(path, newfilename)  # 新文件名（包括路径）
                os.rename(filepath, newfilepath)  # 重命名文件
                num += 1
        print('批量重命名完成,共处理文件' + str(num) + '个')  # 显示重命名了多少个文件
    except:
        print('请输入一个有效路径......')
