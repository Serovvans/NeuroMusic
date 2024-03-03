import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.uic import loadUi
from app.view.resources_rc import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка файла .ui
        loadUi("app/view/ui/mainWindow.ui", self)  # Загрузка интерфейса .ui
        self.timelineLauout = QVBoxLayout(self.timelineContents)
        
        
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
