import sys

from PyQt5.QtWidgets import QApplication

from app_calc.view import CalcView
from app_calc.controler import CalcController
from app_calc.model import CalcModel


def main():
    app = QApplication(sys.argv)

    view = CalcView()
    model = CalcModel()
    controler = CalcController(view=view, model=model)

    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
