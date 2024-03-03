from PyQt5.QtWidgets import QFileDialog
from app.view.audio_widget import AudioWaveWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MainController():
    def __init__(self, view):
        self.view = view
        self.connect_signals()

        self.audios = []
        self.audio_paths = []
        self.players = []
        
    def show(self):
        """Запускает отображение
        """
        self.view.show()
        
    def connect_signals(self):
        """Подключаем слоты к сигналам
        """
        self.view.fileBtn.clicked.connect(self.open_new_audio_file)
        self.view.playBtn.clicked.connect(self.play_audio)
        self.view.pauseBtn.clicked.connect(self.stop_audio)
        
    def open_new_audio_file(self):
        file_dialog = QFileDialog(self.view)
        file_dialog.setNameFilter("Audio Files (*.wav *.mp3)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                filename = selected_files[0]
                new_media_player = QMediaPlayer()
                new_audio_widget = AudioWaveWidget(new_media_player)
                new_audio_widget.load_audio_file(filename)
                content = QMediaContent(QUrl.fromLocalFile(filename))
                new_media_player.setMedia(content)
                
                self.audios.append(new_audio_widget)
                self.players.append(new_media_player)
                self.audio_paths.append(filename)
                
                self.view.timelineLauout.addWidget(new_audio_widget)
            

    def play_audio(self):
        for i in range(len(self.audios)):
            if self.players[i].state() != QMediaPlayer.PlayingState:
                self.players[i].play()
                self.audios[i].playing_timer.start(50)
                
    def stop_audio(self):
        for i in range(len(self.audios)):
            if self.players[i].state() == QMediaPlayer.PlayingState:
                self.players[i].stop()
                self.audios[i].playing_timer.stop()
        