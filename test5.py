from appJar import gui

app = gui()

def press(button):
    if button == "Select Files":
        print(app.openBox(multiple=True))
    else:
        print("RUN!")

app.addButtons(["Select Files", "Run"], press)

app.go()
