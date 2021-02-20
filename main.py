# import for work sys.exit(app.exec())
import sys
# import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
# import for icon window
from PyQt5.QtGui import QIcon
# import design app(ui->py)
from ConvectorCurrency import Ui_MainWindow
# my class for convert currency
import Convector
# class inherit parents class <QtWidgets.QMainWindow>
class CurrencyConvert(QtWidgets.QMainWindow):
    # constructor
    def __init__(self):
        super(CurrencyConvert, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    # name window and icon window
    def init_UI(self):
        # set title window
        self.setWindowTitle("ConvectorCurrency")
        # set window ico
        self.setWindowIcon(QIcon("img/exchange.ico"))
        # init event for btn
        self.ui.exchangeBtn.clicked.connect(self.converter)

    # create dialog window for messages
    def createDialog(self, icon=0, text="TEXT", informativeText="infoText", windowTitle="Title",
                     detailedText="detalText", detailedTextAdd=False, typeBtn=0):
        # create window for messageBox <msg>
        msg = QtWidgets.QMessageBox()
        # choose icon
        # value 0 -> NoIcon
        # value 1 -> Information
        # value 2 -> Warning
        # value 3 -> Critical
        # value 4 -> Question
        if icon == 0:
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
        elif icon == 1:
            msg.setIcon(QtWidgets.QMessageBox.Information)
        elif icon == 2:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
        elif icon == 3:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
        elif icon == 4:
            msg.setIcon(QtWidgets.QMessageBox.Question)
        else:
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
        # set text window
        msg.setText(text)
        # set additional text
        msg.setInformativeText(informativeText)
        # set window title
        msg.setWindowTitle(windowTitle)
        # set configuration buttons
        if detailedTextAdd == True:
            msg.setDetailedText(detailedText)
        if typeBtn == 1:
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        elif typeBtn == 2:
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        # display messagebox
        msg.show()
        # for close messagebox
        msg.exec_()

    # logic program
    def converter(self):
        # dialog window for show a status changed
        # get text from in variable through text()
        inputCurrency = self.ui.inputCurrency.text()
        outputCurrency = self.ui.outputCurrency.text()
        inputAmount = self.ui.inputAmount.text()
        # if the variable is empty, then if converted to boolean value, it will be False
        if (bool(inputCurrency) == False or inputCurrency.isdigit()) or \
                (bool(outputCurrency) == False or outputCurrency.isdigit()) or \
                (bool(inputAmount) == False or inputAmount.isalpha()):
            # zeroing inputs
            inputCurrency = 'USD'
            self.ui.inputCurrency.setText('USD')
            outputCurrency = 'UAH'
            self.ui.outputCurrency.setText('UAH')
            inputAmount = 100
            self.ui.inputAmount.setText(str(inputAmount))
            # create dialog WARNING!
            self.createDialog(3, 'Warning!\nIncorrect data in input\nRetry enter', '', 'Incorrect data in input')
        # init my class <Convert> for exchange currency
        body = Convector.Convector(inputCurrency, outputCurrency)
        # using method class <Convert> convector()
        outputAmount = round(body.convector(float(inputAmount)), 3)
        # create dialog SUCCESS!
        self.createDialog(1, f'Succes convert!\nFROM:{inputCurrency} amount -->{inputAmount}'
                             f'\nTO: {outputCurrency}  amount --> {outputAmount}',
                             f'Check information in Google: {body.getURL()}', 'Success!')
        # display <outputAmount>
        self.ui.outputAmount.setText(str(outputAmount))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = CurrencyConvert()
    application.show()
    sys.exit(app.exec())
