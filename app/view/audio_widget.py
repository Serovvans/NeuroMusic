from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
import numpy as np
import pyqtgraph as pg
import librosa

class AudioWaveWidget(QWidget):
    """Класс отображения аудиофайла в виде волны"""
    def __init__(self, media_player, parent=None):
        # Базовая настройка виджета
        super().__init__(parent)
        self.setMinimumSize(800, 200)
        
        # Создаем поля для данных об аудиофайле и бегунке проигрывателя
        self.audio_data = None
        self.playing = False
        self.current_position = 0

        # Настройки графика волны
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground(QColor("#444444"))
        self.plot_widget.setLabel('left', 'Amplitude')
        self.plot_widget.setLabel('bottom', 'Time')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.plot_widget)
        self.setLayout(self.layout)

        # Создаем и настраиваем проигрыватель
        self.media_player = media_player
        self.playing_timer = QTimer(self)
        self.playing_timer.timeout.connect(self.update_position)

    def load_audio_file(self, filename: str) -> None:
        """Загружает аудиофайл из указанного пути и созраняет все данные в соответствующие поля класса

        Args:
            filename (str): Путь к аудофайлу
        """
        self.audio_data, self.sample_rate = librosa.load(filename, sr=None)
        
        # Получаем длительность аудио для корректоного отображения
        self.duration = librosa.get_duration(y=self.audio_data, sr=self.sample_rate)
        
        # Инициализируем отображение
        self.plot_waveform()
        self.current_position = 0
        self.playing = False

    def plot_waveform(self) -> None:
        """Отрисовывает график аудиоволны
        """
        if self.audio_data is not None:
            time = np.linspace(0, self.duration, len(self.audio_data))
            self.plot_widget.clear()
            self.plot_widget.plot(time, self.audio_data, pen=pg.mkPen(color=(255, 165, 0), width=1))
            self.plot_widget.setMouseEnabled(x=False, y=False)

    def update_position(self) -> None:
        """Обновляет положение бегунка проигрывателя
        """
        self.current_position = self.media_player.position() / 1000  # переводим в секунды
        self.plot_widget.clear()
        self.plot_waveform()
        self.plot_widget.plot([self.current_position, self.current_position], [-1, 1], pen=pg.mkPen(color='r', width=2))
