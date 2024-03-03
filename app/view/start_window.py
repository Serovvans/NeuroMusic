import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from app.view.resources_rc import *


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка файла .ui
        loadUi("app/view/ui/startWindow.ui", self)  # Загрузка интерфейса .ui
        
        # Подгружаем все элементы
        self.newBtn = self.findChild(QPushButton, "newBtn")
        self.openBtn = self.findChild(QPushButton, "openBtn")
        
        
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
