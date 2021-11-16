import sys

from PyQt5.QtWidgets import QApplication

from app.view import CalcView
from app.controler import CalcController
from app.model import CalcModel


def main():
    app = QApplication(sys.argv)

    view = CalcView()
    model = CalcModel()
    controler = CalcController(view=view, model=model)

    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
