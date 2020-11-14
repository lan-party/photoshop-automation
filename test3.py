import pdfplumber
import sys
import win32com.client
import os

filenamelist = sys.argv[1:]

filenamelist = ["etsy.pdf", "amazon.pdf"]

filltext = [[]]
filltextcurrent = 0
for filename in filenamelist:
    with pdfplumber.open(filename) as currentfile:
        firstpage = currentfile.pages[2].extract_text()
        if firstpage != "":
            if firstpage.split(" ")[0] == "Order":
                pdftype = "etsy"
                startstr = "Personalization:"
                endstr = "Shop"
            elif firstpage.split(" ")[0] == "Ship":
                pdftype = "amazon"
                
            else:
                pdftype = "error"
            for page in currentfile.pages:
                pagetext = page.extract_text()
                if len(filltext[filltextcurrent]) < 12:
                    if pdftype == "amazon":
                        filltext[filltextcurrent] += [pagetext[pagetext.find("Font Color: font (#000)")+len("Font Color: f (#000)"):pagetext.find("Grand total")]]
                    elif pdftype == "etsy":
                        filltext[filltextcurrent] += [pagetext[pagetext.find("Personalization:")+len("Personalization:"):pagetext.find("Do the green thing")]]
                    else:
                        filltext[filltextcurrent] += [""]
                else:
                    filltextcurrent += 1
                    filltext.append([])
                    filltext[filltextcurrent] += ["test"]
        else:
            print("error 0")

print(filltext[0])
input()

# Open photoshop
psApp = win32com.client.Dispatch("Photoshop.Application")

batchcount = 0
for batch in filltext:
    # Open template file
    psApp.Open(r"C:\Users\dell\Documents\thelasersedge\automation\template.psd")
    doc = psApp.Application.ActiveDocument
    # Set text for all layers
    for a in range(1, len(batch)):
        doc.ArtLayers[str(a)].TextItem.contents = batch[a-1]
    # Save as a new psd
    doc.SaveAs(r"C:\Users\dell\Documents\thelasersedge\automation\batch"+str(batchcount)+".psd")
