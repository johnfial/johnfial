# https://www.pythonpool.com/python-text-to-pdf/

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=50)


pdf.cell(200, 10, txt = 'test this',
    ln = 1, align = 'C')

line_2 = ''
for x in range(10):
    line_2 += (str(x) + '\n')
pdf.cell(200, 10, txt = line_2, ln = 2, align = 'C')

pdf.output("test.pdf")
print('finished~~~~~~~~~~~~~')