#encoding:utf-8
import datetime
import sys
sys.path.append("D:/\Python27/\Lib/\site-packages/\openpyxl")
from openpyxl.
wb = Workbook()
# 激活 worksheet
ws = wb.active
## 数据可以直接分配到单元格中
ws['A1'] = 42
## 可以附加行，从第一列开始附加
ws.append([1, 2, 3])
## Python 类型会被自动转换

ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")
## 保存文件
wb.save("sample.xlsx")

#
# lwb=load_workbook('login_test_data.xlsx')
# sheet=lwb.get_sheet_by_name('login_test_data')
# for i,_ in enumerate(list(sheet.rows)[:-1]):
#     print sheet['C' + str(i+2)].value
#
#     b=sheet['D' + str(2)].value
#     print b
