<<<<<<< HEAD
print("Hello word first one")
print("Hello world 2")
print("Hello word first one")
print("new")
=======
import sys
from test import MainWindow
from PySide6.QtWidgets import QApplication

#this is a Qwidget

if __name__=="__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()
        

>>>>>>> 5a42a55 (Initial commit)
