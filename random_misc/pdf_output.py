# https://www.pythonpool.com/python-text-to-pdf/

from fpdf import FPDF
# docs @  https://pyfpdf.readthedocs.io/en/latest/reference/cell/index.html

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# make the first object/file
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=50)
pdf.cell(200, 10, txt = 'test this',
    ln = 1, align = 'C', border=1)

line_2 = ''
for x in range(12):
    line_2 += (str(x) + '\n')
pdf.cell(200, 10, txt = line_2, ln = 2, align = 'C')

pdf.output("test.pdf")
print('finished 1~~~~~~~~~~~~~')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # print a 2nd object/file
pdf2 = FPDF()
pdf2.add_page()
pdf2.set_font("Arial", size=50)
pdf2.cell(200, 10, txt = 'page2',
    ln = 1, align = 'C')

line_2 = ''
for x in range(5):
    line_2 += (str(x) + 'xxx ')
pdf2.cell(200, 10, txt = line_2, ln = 2, align = 'C')

pdf2.output("test2.pdf")
print('finished 2~~~~~~~~~~~~~')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# now let's try to edit the first and output again
import time
time.sleep(1) # change this 

# pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=50)
pdf.cell(300, 200, txt = 'this is test 3',
    ln = 1, align = 'C', border=1)

line_2 = ''
for x in range(50):
    line_2 += (str(x) + 'CCCCC')
pdf.cell(200, 10, txt = line_2, ln = 2, align = 'C')

pdf.output("test.pdf")
print('finished 3~~~~~~~~~~~~~')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 