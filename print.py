from PyPDF2 import PdfReader
path="/Users/jay/Downloads/tutorial-example.pdf"
reader = PdfReader(path)
meta = reader.metadata
print("Total Pages: ", len(reader.pages))
# All of the following could be None!
print("Author: ", meta.author)
print("Creator: ", meta.creator)
print("Producer: ", meta.producer)
print("Subject: ", meta.subject)
print("Title: ", meta.title)
page = reader.pages[0]
print(page.extract_text())