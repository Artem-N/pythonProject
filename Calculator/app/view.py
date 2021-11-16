from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from PyQt5.QtCore import Qt


class CalcView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(650, 550)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.main_layout = QVBoxLayout()
        self._central_widget.setLayout(self.main_layout)

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedSize(630, 75)
        self.display.setReadOnly(True)

        self.display.setStyleSheet("font-size: 50pt; color: black")

        self.main_layout.addWidget(self.display)

    def _create_buttons(self):
        self.lbottons = QGridLayout()
        self.button = []

        button_cords = {
            "AC": (0, 0),
            "**": (0, 1),
            "//": (0, 2),
            "/": (0, 3),
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),
            "*": (1, 3),
            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),
            "-": (2, 3),
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "+": (3, 3),
            "0": (4, 0, 1, 3),
            ".": (4, 2),
            "=": (4, 3)
        }

        for text_button, coord in button_cords.items():
            q_button = QPushButton(text_button)
            if text_button == "0":
                q_button.setFixedSize(324, 92)
            else:
                q_button.setFixedSize(167, 92)
            q_button.setStyleSheet("font-size: 26pt; color: rgb(0,0,0);")
            if text_button == "/" or text_button == "*" or text_button == "+" or text_button == "-" or text_button == "=":
                q_button.setStyleSheet("font-size: 25pt; color: rgb(0,0,0); background: rgba(255,140,0,0.8);")
            elif text_button == "**":
                q_button.setToolTip("Performs exponential (power) calculation on operators")
                q_button.resize(q_button.sizeHint())
                q_button.move(50, 50)
            elif text_button == "//":
                q_button.setToolTip("Floor Division")
                q_button.resize(q_button.sizeHint())
                q_button.move(50, 50)

            self.lbottons.addWidget(q_button, *coord)
            self.button.append(q_button)

        self.main_layout.addLayout(self.lbottons)
