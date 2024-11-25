# Decrypt password-protected PDF in Python.
# 
# Requirements:
# pip install PyPDF2



from PyPDF2 import PdfReader, PdfWriter

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfReader(input_file)
    reader.decrypt(password)

    writer = PdfWriter()

    for i in range(len(reader.pages)):
      writer.add_page(reader.pages[i])

    writer.write(output_file)

if __name__ == '__main__':
  # example usage:
  source="/Users/jay/Downloads/Statement_2024MTH10_45750209.pdf"
  target="/Users/jay/Downloads/Statement_2024MTH10_457502091.pdf"
  password="jaya1410"
  decrypt_pdf(source, target, password)