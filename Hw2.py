################### Import ###############################
# Writing to an excel
import xlwt
from xlwt import Workbook
# Random
import random

import PageRep

#################### main ################################
# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

# Gen data
rangeOfData = 7
data = []
data10 = []
data20 = []
data30 = []
data40 = []
data50 = []

for i in range(10):
    data10.append(random.randrange(rangeOfData))

for i in range(20):
    data20.append(random.randrange(rangeOfData))

for i in range(30):
    data30.append(random.randrange(rangeOfData))

for i in range(40):
    data40.append(random.randrange(rangeOfData))

for i in range(50):
    data50.append(random.randrange(rangeOfData))

random.shuffle(data10)
random.shuffle(data20)
random.shuffle(data30)
random.shuffle(data40)
random.shuffle(data50)
data.append(data10)
data.append(data20)
data.append(data30)
data.append(data40)
data.append(data50)
########################################################

# Write Work book header
for i in range(5):
    sheet1.write(i, 0, "Data "+str(i+1))
    for j in range(len(data[i])):
        sheet1.write(i, j+1, data[i][j])

for x in range(len(data)):
    sheet1.write(6+(x*6), 0, "Data List :" + str(x+1))
    sheet1.write(7+(x*6), 0, "Number of frame")
    sheet1.write(8+(x*6), 0, "FIFO")
    sheet1.write(9+(x*6), 0, "Optimal")
    sheet1.write(10+(x*6), 0, "RLU")
    for i in range(1, 9):
        sheet1.write(7+(x*6), i, str(i))
        sheet1.write(8+(x*6), i, PageRep.FIFO(data[x], i))
        sheet1.write(9+(x*6), i, PageRep.Optimal(data[x], i))
        sheet1.write(10+(x*6), i, PageRep.RLU(data[x], i))

wb.save('page_rep.xls')
