class StartController():
    def __init__(self, view, main_controller):
        self.view = view
        self.main = main_controller
        
        self.connect_signals()
        
    def show(self):
        """Запускает отображение
        """
        self.view.show()
        
    def connect_signals(self):
        """Подключаем слоты к сигналам
        """
        self.view.createBtn.clicked.connect(self.open_main_window)
        self.view.openBtn.clicked.connect(self.open_image_in_main_window)
         
    def open_main_window(self):
        """Слот для открытия главного окна
        """
        self.main.show()
        self.view.close()
        
    def open_image_in_main_window(self):
        """Слот для открытия изображения в главном окне
        """
        self.main.show()
        self.view.close()
        self.main.open_new_audio_file()
