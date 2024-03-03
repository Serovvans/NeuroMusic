import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QColor
import numpy as np
import pyqtgraph as pg
import librosa

class AudioWaveWidget(QWidget):
    def __init__(self, media_player, parent=None):
        super().__init__(parent)
        self.setMinimumSize(800, 200)
        self.audio_data = None
        self.playing = False
        self.current_position = 0

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground(QColor("#444444"))
        self.plot_widget.setLabel('left', 'Amplitude')
        self.plot_widget.setLabel('bottom', 'Time')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.plot_widget)
        self.setLayout(self.layout)

        self.media_player = media_player
        self.playing_timer = QTimer(self)
        self.playing_timer.timeout.connect(self.update_position)

    def load_audio_file(self, filename):
        self.audio_data, self.sample_rate = librosa.load(filename, sr=None)
        self.duration = librosa.get_duration(y=self.audio_data, sr=self.sample_rate)
        self.plot_waveform()
        self.current_position = 0
        self.playing = False

    def plot_waveform(self):
        if self.audio_data is not None:
            time = np.linspace(0, self.duration, len(self.audio_data))
            self.plot_widget.clear()
            self.plot_widget.plot(time, self.audio_data, pen=pg.mkPen(color=(255, 165, 0), width=1))
            self.plot_widget.setMouseEnabled(x=False, y=False)

    def update_position(self):
        self.current_position = self.media_player.position() / 1000  # convert ms to seconds
        self.plot_widget.clear()
        self.plot_waveform()
        self.plot_widget.plot([self.current_position, self.current_position], [-1, 1], pen=pg.mkPen(color='r', width=2))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Wave Player")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.media_player = QMediaPlayer(self)
        self.media_player.setVolume(50)

        self.audio_wave_widget = AudioWaveWidget(self.media_player)
        self.layout.addWidget(self.audio_wave_widget)

        self.open_button = QPushButton("Open Audio File")
        self.open_button.clicked.connect(self.open_audio_file)
        self.layout.addWidget(self.open_button)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_audio)
        self.layout.addWidget(self.play_button)

    def open_audio_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3)")
        if filename:
            self.audio_wave_widget.load_audio_file(filename)
            content = QMediaContent(QUrl.fromLocalFile(filename))
            self.media_player.setMedia(content)

    def play_audio(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.stop()
            self.play_button.setText("Play")
            self.audio_wave_widget.playing_timer.stop()
        else:
            self.media_player.play()
            self.play_button.setText("Stop")
            self.audio_wave_widget.playing_timer.start(50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
