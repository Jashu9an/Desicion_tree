import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QPushButton, QSpacerItem, QSizePolicy, QGridLayout, QScrollArea

class ResultWindow(QWidget):
    def __init__(self, conclusion, disease_id, comment):
        super().__init__()

        self.setWindowTitle("Результаты")
        self.setGeometry(200, 100, 700, 800)

        layout = QVBoxLayout()

        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        id_label = QLabel(f"ID заболевания: {disease_id}")
        conclusion_label = QLabel(f"Заключение: {conclusion}")
        comment_label = QLabel(f"Комментарий: {comment}")

        font_size = 16
        font = QFont("Arial", font_size)  # Укажите шрифт и размер
        id_label.setFont(font)
        conclusion_label.setFont(font)
        comment_label.setFont(font)

        id_label.setWordWrap(True)
        id_label.adjustSize()
        conclusion_label.setWordWrap(True)
        conclusion_label.adjustSize()
        comment_label.setWordWrap(True)
        comment_label.adjustSize()

        layout.addWidget(id_label)
        layout.addWidget(conclusion_label)
        layout.addWidget(comment_label)

        self.setLayout(layout)
        self.setWindowIcon(QIcon('window_icon.png'))