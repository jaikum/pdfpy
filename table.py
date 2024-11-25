# pip3 install tabula-py

import tabula
path="/Users/jay/Downloads/Statement_2024MTH10_457502091.pdf"
tables = tabula.read_pdf(path, pages='all')
for i, table in enumerate(tables, start=1):
    print(f"Table {i}:")
    print(table)
    print("-----------------------")
