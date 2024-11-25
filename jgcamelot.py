# pip3 install "camelot-py[base]"

import camelot
path="/Users/jay/Downloads/Statement_2024MTH10_457502091.pdf"


tables = camelot.read_pdf(path)
for table in tables:
    print(table.df)