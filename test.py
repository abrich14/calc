'''
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton,QDialogButtonBox,QVBoxLayout,QLabel
'''

'''class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        self.setCentralWidget(button)
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        dlg=CustomDialog()
        dlg.setWindowTitle("What is this")

        dlg.exec()

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        Qbtn=(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox=QDialogButtonBox(Qbtn)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.rejected.connect(self.accept)

        layout=QVBoxLayout()
        message= QLabel("Someting happened, are you ok")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
'''

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")

app = QApplication(sys.argv)

window = loader.load("but.ui", None)

window.pushButton.clicked.connect(arv)

def arv(self):
    print("clicked")

mainwindow_setup(window)
window.show()
app.exec()