# NeuroMusic

В этом проекте реализовано декстопное приложение для редактирование аудиофайлов с дополнительной возможностью генерации аудио с помощью нейронной сети

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/Serovvans/NeuroMusic.git
    ```

2. **Создайте и активируйте виртуальное окружение Anaconda в дириктории проекта:**

    ```bash
    conda create --name .conda python=3.8
    conda activate .conda
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

## Запуск

```bash
python main.py
```

## Структура

* app - модуль со всеми частями приложения
    + __init__.py
    + controllers - модуль с классами-контроллерами различных частей приложения
        - main_controller.py - содержит класс-контроллер главного окна редактора
        - start_controller.py - содержит класс-контроллер стартового окна
        - __init__.py
    + view - модуль
        - audio_widget.py - содержит класс-отображение виджета аудиофайла с оторбражением в виде волны
        - main_window.py - содержит класс-отображение главного окна редактора
        - resources_rc.py - содержит сокомпилированные ресурсы, использующиеся в интерфейсе
        - start_window.py - содержит класс-отображение стартового окна приложения
        - __init__.py
        - ui - каталог с файлами интерфейса различных окон
        -resources - католог с ресурсами, использующимися в интерфейсе
* main.py - файл, в котором настраивается и запускается приложение
* .gitignore
* README.md
* requirements.txt - файла, в котором перечисленны все необходимые зависимости
