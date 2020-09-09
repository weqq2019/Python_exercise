import xlrd
import xlwt

def readexcel():
    workbook=xlrd.open_workbook(r"E:\02_归零叔\01_必须打造核心竞争力\Python编程锦囊\Python_exercise\第三章_文件操作\spider\Yuanjisong\Yuanjisong\spiders\Excel爬虫最终测试.xls")
    print(workbook.sheet_names())
    sheet2=workbook.sheet_by_name('爬虫表')
    nrows=sheet2.nrows
    ncols=sheet2.ncols
    # print(nrows,ncols)

    cell_A=sheet2.cell(1,0).value#取出第X行第X列的值
    # print(cell_A)

    clou = sheet2.col_values(0)  # 读取第一列
    # print(clou)
    return clou

if __name__ == '__main__':

    list=readexcel()
    print(list)