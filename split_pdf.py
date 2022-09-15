# pip install pypdf2

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"C:\Users\scriptdocuchm_ktm.pdf"
path = r"C:\Users\cools\Downloads\machine-learning-bookcamp-build-a-portfolio-of-real-life-projects.pdf"

pdf = PdfFileReader(path, "rb")
pdflist = []
pdf_writer = PdfFileWriter()

for page in range(66,70):
    pdflist.append(page)
    pdf_writer.addPage(pdf.getPage(page))

print(pdflist)

output_filename = "split.pdf"

with open(output_filename, 'wb') as out:
    pdf_writer.write(out)

print ("pdf file has been split")