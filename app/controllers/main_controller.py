from PyQt5.QtWidgets import QFileDialog
from app.view.audio_widget import AudioWaveWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MainController():
    """Контроллер главного окна, отвечает за динамику и функциональность элементов"""
    def __init__(self, view):
        self.view = view
        self.connect_signals()

        # Инициализируем поля для хранения данных о текущих аудиофайлах
        self.audios = [] # Виджеты открытых ауидофайлов
        self.audio_paths = [] # Проигрыватели для каждого из открытых аудиофайлов
        self.players = [] # Пути до каждого из открытых аудиофайлов
        
    def show(self) -> None:
        """Запускает отображение
        """
        self.view.show()
        
    def connect_signals(self) -> None:
        """Подключаем слоты к сигналам
        """
        self.view.fileBtn.clicked.connect(self.open_new_audio_file)
        self.view.playBtn.clicked.connect(self.play_audio)
        self.view.pauseBtn.clicked.connect(self.stop_audio)
        
    def open_new_audio_file(self) -> None:
        """Окрывает новый аудиофайл, создает виджет и проигрыватель, добавляет созданный виджет в область для отображения
        """
        # Инициализируем файловое диалоговое окно
        file_dialog = QFileDialog(self.view)
        file_dialog.setNameFilter("Audio Files (*.wav *.mp3)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        
        # Если в диалоговом окне выбран файл, то инициализируем виджет и прогрыватель и сохраняем всю информауию о файле
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles() # Получаем список выбранных файлов и открываем каждый из них
            for filename in selected_files:
                # Инициализируем плеер и виджет для отображения аудио
                new_media_player = QMediaPlayer()
                new_audio_widget = AudioWaveWidget(new_media_player)
                new_audio_widget.load_audio_file(filename)
                content = QMediaContent(QUrl.fromLocalFile(filename))
                new_media_player.setMedia(content)
                
                # Сохранияем созданные объекты
                self.audios.append(new_audio_widget)
                self.players.append(new_media_player)
                self.audio_paths.append(filename)
                
                # Добавляем созданный виджет в Scroll Area
                self.view.timelineLauout.addWidget(new_audio_widget)
            

    def play_audio(self) -> None:
        """Запускает проигрыватели всех текущих открытых аудиофайлов
        """
        for i in range(len(self.audios)):
            if self.players[i].state() != QMediaPlayer.PlayingState:
                self.players[i].play()
                self.audios[i].playing_timer.start(50)
                
    def stop_audio(self):
        """Останавливает проигрыватели всех текущих открытых аудофайлов
        """
        for i in range(len(self.audios)):
            if self.players[i].state() == QMediaPlayer.PlayingState:
                self.players[i].stop()
                self.audios[i].playing_timer.stop()
        