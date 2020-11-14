import PyPDF2
import sys

filenamelist = sys.argv[1:]

filenamelist = ["etsy.pdf", "amazon.pdf"]


for filename in filenamelist:
    currentfile = PyPDF2.PdfFileReader(open(filename, 'rb'))
    firstpage = currentfile.getPage(2).extractText()
    if len(firstpage) > 0:
        if firstpage.split(" ")[0] == "Order":
            pdftype = "etsy"
        elif firstpage.split(" ")[0] == "Ship":
            pdftype = "amazon"
        else:
            pdftype = "error"
        print(firstpage)
    else:
        print(firstpage)
    
