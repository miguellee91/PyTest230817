import xlwt
import csv
import os

csvFileList = ["C:/PyTest2023/PyTest230817/homework/230822_smlee/001.csv", "C:/PyTest2023/PyTest230817/homework/230822_smlee/002.csv",
               "C:/PyTest2023/PyTest230817/homework/230822_smlee/003.csv"]
outWorkbook = xlwt.Workbook()

for csvFileName in csvFileList:
    rowCount = 0
    with open(csvFileName, "r") as inFp:
        csvReader = csv.reader(inFp)
        header_list = next(csvReader)
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
        for col in range(len(header_list)):
            outSheet.write(rowCount, col, header_list[col])
        for row_list in csvReader:
            rowCount += 1
            for col in range(len(row_list)):
                if row_list[col].isnumeric():
                    outSheet.write(rowCount, col, float(row_list[col]))
                else:
                    outSheet.write(rowCount, col, row_list[col])

outWorkbook.save(
    'C:/PyTest2023/PyTest230817/homework/230822_smlee/smlee_Code0707_CSV230822.xls')
print("Save. OK~")
