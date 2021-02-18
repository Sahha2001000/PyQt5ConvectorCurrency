import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QIcon
from ConvectorCurrency import Ui_MainWindow
from currency_converter.currency_converter import CurrencyConverter
class CurrencyConvert(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConvert,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = CurrencyConvert()
    application.show()
    sys.exit(app.exec())



