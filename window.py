from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
    QGridLayout,
    QMessageBox,
)

import pydub

from PyQt6 import QtCore

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("TRILL AUDIO | we ❤️ music | alpha")
window.setGeometry(100, 100, 500, 500)
window.setFixedSize(500, 500)
window.setStyleSheet("background-color: #1f1f1f;")
# add text
text = QLabel("TRILL AUDIO", window)
text.setStyleSheet("color: #ffffff; font-size: 30px;")
text.move(150, 10)
text.setFixedSize(200, 50)
text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
text.show()
# take user input
input_path = QLineEdit()
# take user input for output path
output_path = QLineEdit()
input_path.setPlaceholderText("Enter input path")
output_path.setPlaceholderText("Enter output path")
input_path.setFixedWidth(300)
output_path.setFixedWidth(300)
input_path.setFixedHeight(30)
output_path.setFixedHeight(30)
input_path.setStyleSheet("background-color: white;")
output_path.setStyleSheet("background-color: white;")
input_path.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
output_path.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
input_path.show()
output_path.show()
window.show()

app.exec()
