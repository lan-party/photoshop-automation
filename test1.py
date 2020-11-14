import win32com.client
import os

# Open photoshop
psApp = win32com.client.Dispatch("Photoshop.Application")

# Open template file
psApp.Open(r"C:\Users\dell\Documents\thelasersedge\automation\template.psd")
doc = psApp.Application.ActiveDocument

# Set the text on the first lid
layer1 = doc.ArtLayers["1"]
layer1.TextItem.contents = "test"

# Save as a new psd
doc.SaveAs(r"C:\Users\dell\Documents\thelasersedge\automation\batch1.psd")
