import csv

rows = [{'a':123, 'b':123, 'c':'aa'},{'a2':123, 'b':123, 'c':'aa'},{'a3':123, 'b':123, 'c':'aa'},{'a4':123, 'b':123, 'c':'aa'}]
lst_item=[]
lst2_item=[]
for i in range(len(rows)):
    for i in range(len(rows)):
        lst = list(rows[i])
        lst2 = list(rows[i].values())
        lst_item.append(lst)
        lst2_item.append(lst2)

import xlwt
work_book=xlwt.Workbook(encoding='utf-8')
sheet=work_book.add_sheet('爬虫表')
for i in range(len(lst_item[0])):
    print(lst_item[0])
    sheet.write(0,i,lst_item[0][i])

for i in range(len(lst2_item)):
    for j in range(len(lst2_item[0])):
        sheet.write(i + 1, j, lst2_item[i][j])
# aaa = [1, 2, 3]
# for i in range(len(aaa)):
#     sheet.write(0, i, aaa[i])
# sheet.write(0, 0, '第一行第一列')
# sheet.write(0, 1, '第一行第二列')
work_book.save('Excel爬虫最终测试1.xls')

# >>>seq = ['one', 'two', 'three']
# >>> for i, element in enumerate(seq):
# ...     print i, element
# ...
# 0 one
# 1 two
# 2 three


work_book.save('Excel爬虫测试9.xls')