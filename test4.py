import PyPDF2
import sys
import pdfplumber
import win32com.client
import os

filenamelist = ["Amazon music 1112.pdf", "Etsy music 1112.pdf", "Amazon hogwarts 1112.pdf", "Etsy hogwarts 1112.pdf"]

filltext = [[[]],[[]]]
filltextcurrent = [0, 0]

for filename in filenamelist:
    templateselection = 0
    if "hogwarts" in filename:
        templateselection = 1
    if "Amazon" in filename:
        with pdfplumber.open(filename) as currentfile:
            for page in currentfile.pages:
                pagetext = page.extract_text()
                if len(filltext[templateselection][filltextcurrent[templateselection]]) < 12:
                    filltext[templateselection][filltextcurrent[templateselection]] += [pagetext[pagetext.find("(#000000)")+len("Font Color: f (#000)"):pagetext.find("Grand total")]]
                else:
                    filltextcurrent[templateselection] += 1
                    filltext[templateselection].append([])
    else:
        currentfile = PyPDF2.PdfFileReader(open(filename, 'rb'))
        for a in range(0, currentfile.numPages-1):
            pagetext = currentfile.getPage(a).extractText()
            if len(filltext[templateselection][filltextcurrent[templateselection]]) < 6:
                filltext[templateselection][filltextcurrent[templateselection]] += [pagetext[pagetext.find("Personalization:")+len("Personalization:"):pagetext.find("Do the green thing")]]
            else:
                filltextcurrent[templateselection] += 1
                filltext[templateselection].append([])


# Open photoshop
# psApp = win32com.client.Dispatch("Photoshop.Application")

batchcount = 0
for batch in filltext[0]:
    # Open template file
    # psApp.Open(r"C:\Users\dell\Documents\thelasersedge\automation\template.psd")
    # doc = psApp.Application.ActiveDocument
    # Set text for all layers
    for a in range(1, len(batch)):
        # doc.ArtLayers[str(a)].TextItem.contents = batch[a-1]
        print(batch[a-1])
    # Save as a new psd
    # doc.SaveAs(r"C:\Users\dell\Documents\thelasersedge\automation\batch"+str(batchcount)+".psd")
    batchcount += 1

print("")

for batch in filltext[1]:
    # Open template file
    # psApp.Open(r"C:\Users\dell\Documents\thelasersedge\automation\template2.psd")
    # doc = psApp.Application.ActiveDocument
    # Set text for all layers
    for a in range(1, len(batch)):
        # doc.ArtLayers[str(a)].TextItem.contents = batch[a-1]
        print(batch[a-1])
    # Save as a new psd
    #doc.SaveAs(r"C:\Users\dell\Documents\thelasersedge\automation\batch"+str(batchcount)+".psd")
    batchcount += 1
