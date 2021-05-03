import PyPDF2
from tkinter.filedialog import askopenfile 

file = askopenfile(mode ='r', filetypes =[('PDF files', '*.pdf')]) 
if file is not None: 
    fileObj = open(file,"rb")
else:
    exit()

pdfReader = PyPDF2.PdfFileReader(fileObj)
print(f"No. of pages: {pdfReader.numPages}")

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

fileObj.close()