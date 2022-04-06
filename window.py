from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
    QGridLayout,
    QMessageBox,
)

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
window.show()

app.exec()
