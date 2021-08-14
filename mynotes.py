from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys
import datetime

class UI(QWidget):
    def __init__(self):
        super().__init__()
        #this is used for loading ui file
        uic.loadUi("gui.ui", self)

        self.loadNoteItems()        
        
        self.saveNote.clicked.connect(self.saveTheNote)

    def loadNoteItems(self):
        with open("items.txt") as fp:
            Lines = fp.readlines()
            for line in Lines:
                self.noteItem.addItem(line.strip())
        

    def saveTheNote(self):
        print('clicked saveNote')   
        noteItem = self.noteItem.currentText()
        noteText = self.noteText.toPlainText()
        self.noteText.setPlainText("")

        theFile = noteItem + '.txt'
        import os.path
        if not os.path.exists(theFile):
            file1 = open(theFile,"a")
            file1.write("\n")


        with open(theFile, 'r+') as fp:
            lines = fp.readlines()                 
            fp.seek(0)     # file pointer locates at the beginning to write the whole file again

            fp.write(datetime.datetime.now().strftime("%A, %m-%d-%Y %I:%M %p"))
            fp.write("\n")
            fp.writelines(noteText)
            fp.write("\n\n")
        
            fp.writelines(lines) 

        
app = QApplication([])
window = UI()
window.show()
sys.exit(app.exec())