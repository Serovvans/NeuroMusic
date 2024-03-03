from app.controllers.main_controller import MainController
from app.controllers.start_controller import StartController

from app.view.start_window import StartWindow
from app.view.main_window import MainWindow

from PyQt5.QtWidgets import QApplication


def setup():
    main_window = MainWindow()
    hello_window = StartWindow()
    
    main_controller = MainController(main_window)
    start_controller = StartController(view=hello_window, main_controller=main_controller)
    return start_controller

if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    
    start_controller = setup()
    start_controller.show()
    
    sys.exit(app.exec())
