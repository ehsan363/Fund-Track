from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()