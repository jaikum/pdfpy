# pip3 install pdfplumber

import pdfplumber

path="/Users/jay/Downloads/Statement_2024MTH10_457502091.pdf"

print('----------------------------------------')
pdf = pdfplumber.open(path)
for page in pdf.pages:
    #text = page.extract_text()
    #textlines = text.split('\n')
    tablelines = page.extract_table(table_settings=\
            {"vertical_strategy": "text", \
                "horizontal_strategy": "text", \
                "snap_tolerance":5}) # snap_tolernace 4 - 9 works
    for i in range(len(tablelines)):
        print(i, tablelines[i])