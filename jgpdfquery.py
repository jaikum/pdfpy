# pip3 install pdfquery

from pdfquery import PDFQuery

path="/Users/jay/Downloads/Statement_2024MTH10_457502091.pdf"
pdf = PDFQuery(path)
pdf.load()
for element in pdf.tree.iter():
    print(element.text)
