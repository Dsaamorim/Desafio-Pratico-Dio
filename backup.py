from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

from PyQt5.QtWidgets import QMessageBox, QComboBox, QPushButton, QLabel

_translate = QtCore.QCoreApplication.translate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.moeda = QtWidgets.QLabel(self.centralwidget)
        self.moeda.setGeometry(QtCore.QRect(10, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.moeda.setFont(font)
        self.moeda.setObjectName("moeda")
        self.entrada_moedas = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_moedas.setGeometry(QtCore.QRect(140, 67, 113, 20))
        self.entrada_moedas.setObjectName("entrada_moedas")
        self.moeda_2 = QtWidgets.QLabel(self.centralwidget)
        self.moeda_2.setGeometry(QtCore.QRect(11, 109, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.moeda_2.setFont(font)
        self.moeda_2.setObjectName("moeda_2")
        self.tipos_moedas = QtWidgets.QComboBox(self.centralwidget)
        self.tipos_moedas.setGeometry(QtCore.QRect(190, 116, 69, 22))
        self.tipos_moedas.setObjectName("tipos_moedas")
        self.tipos_moedas.addItem("")
        self.tipos_moedas.addItem("")
        self.tipos_moedas.addItem("")
        self.tipos_moedas.addItem("")
        self.tipos_moedas.addItem("")
        self.moeda_3 = QtWidgets.QLabel(self.centralwidget)
        self.moeda_3.setGeometry(QtCore.QRect(10, 149, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.moeda_3.setFont(font)
        self.moeda_3.setObjectName("moeda_3")
        self.tipos_moedas_2 = QtWidgets.QComboBox(self.centralwidget)
        self.tipos_moedas_2.setGeometry(QtCore.QRect(206, 156, 69, 22))
        self.tipos_moedas_2.setObjectName("tipos_moedas_2")
        self.tipos_moedas_2.addItem("")
        self.tipos_moedas_2.addItem("")
        self.tipos_moedas_2.addItem("")
        self.tipos_moedas_2.addItem("")
        self.tipos_moedas_2.addItem("")
        self.botao_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_converter.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.botao_converter.setObjectName("botao_converter")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(99, 240, 75, 23))
        self.botao_sair.setObjectName("botao_sair")
        self.entrada_moedas_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_moedas_2.setGeometry(QtCore.QRect(73, 208, 113, 20))
        self.entrada_moedas_2.setObjectName("entrada_moedas_2")
        self.moeda_4 = QtWidgets.QLabel(self.centralwidget)
        self.moeda_4.setGeometry(QtCore.QRect(10, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.moeda_4.setFont(font)
        self.moeda_4.setObjectName("moeda_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.botao_converter.clicked.connect(self.converte)

        self.retranslateUi(MainWindow)
        self.botao_sair.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.moeda.setText(_translate("MainWindow", "Insira o valor: "))
        self.moeda_2.setText(_translate("MainWindow", "O tipo de moeda inserida: "))
        self.tipos_moedas.setItemText(0, _translate("MainWindow", "Real"))
        self.tipos_moedas.setItemText(1, _translate("MainWindow", "Dólar"))
        self.tipos_moedas.setItemText(2, _translate("MainWindow", "Euro"))
        self.tipos_moedas.setItemText(3, _translate("MainWindow", "Peso"))
        self.moeda_3.setText(_translate("MainWindow", "O tipo de moeda convertida: "))
        self.tipos_moedas_2.setItemText(0, _translate("MainWindow", "Real"))
        self.tipos_moedas_2.setItemText(1, _translate("MainWindow", "Dólar"))
        self.tipos_moedas_2.setItemText(2, _translate("MainWindow", "Euro"))
        self.tipos_moedas_2.setItemText(3, _translate("MainWindow", "Peso"))
        self.botao_converter.setText(_translate("MainWindow", "Converter"))
        self.botao_sair.setText(_translate("MainWindow", "Saída"))
        self.moeda_4.setText(_translate("MainWindow", "Saída:"))

    def converte(self):

        # captura o valor do campo "inserir valor"
        valEntrada = float(self.entrada_moedas.text())
        resultado = valEntrada
        # captura o valor do combo box selecionado da moeda inserida
        tipomodDe = self.tipos_moedas.currentText()
        # captura o valor do combo box selecionado da moeda a ser convertida
        tipomodTo = self.tipos_moedas_2.currentText()

        ####################### QUANDO FOR SELECIONADO DE REAL (1º COMBO) ###################3333
        if tipomodDe == 'Real':
            # busca  o usd e euro transformado em real
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,ARS-BRL")
            cotacoes_dic = getJsonMoeda.json()
            # CONVERTE DOLAR EM REAL
            if tipomodTo == 'Dólar':
                valcotacao = float(cotacoes_dic['USDBRL']['bid'])
                resultado = valEntrada * valcotacao
            elif tipomodTo == 'Euro':
                valcotacao = float(cotacoes_dic['EURBRL']['bid'])
                resultado = valEntrada * valcotacao
            elif tipomodTo == 'Peso':
                valcotacao = float(cotacoes_dic['ARSBRL']['bid'])
                resultado = valEntrada * valcotacao
        ####################### QUANDO FOR SELECIONADO DE DÓLAR (1º COMBO) ###################3333
        if tipomodDe == 'Dólar':
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/BRL-USD,EUR-USD,ARS-USD")
            cotacoes_dic = getJsonMoeda.json()
            # CONVERTE REAL em DOLAR
            if tipomodTo == 'Real':
                valcotacao = float(cotacoes_dic['BRLUSD']['bid'])
                resultado = valEntrada * valcotacao
            # CONVERTE EURO EM DOLAR
            elif tipomodTo == 'Euro':
                valcotacao = float(cotacoes_dic['EURUSD']['bid'])
                resultado = valEntrada * valcotacao
                # CONVERTE PESO EM DÒLAR
            elif tipomodTo == 'Peso':
                valcotacao = float(cotacoes_dic['ARSUSD']['bid'])
                resultado = valEntrada * valcotacao
        ####################### QUANDO FOR SELECIONADO EURO (1º COMBO) ###################3333
        if tipomodDe == 'EURO':
            # busca  o usd e euro transformado em real
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/BRL-EUR,USD-EUR,ARS-EUR")
            cotacoes_dic = getJsonMoeda.json()
            # CONVERTE REAL em EURO
            if tipomodTo == 'Real':
                valcotacao = float(cotacoes_dic['BRLEUR']['bid'])
                resultado = valEntrada * valcotacao
            # CONVERTE  DOLAR EM EURO
            elif tipomodTo == 'Dólar':
                valcotacao = float(cotacoes_dic['USDEUR']['bid'])
                resultado = valEntrada * valcotacao
                # CONVERTE PESO EM EURO
            elif tipomodTo == 'Peso':
                valcotacao = float(cotacoes_dic['ARSEUR']['bid'])
                resultado = valEntrada * valcotacao
        ####################### QUANDO FOR SELECIONADO PESO (1º COMBO) ###################3333
        if tipomodDe == 'Peso':
            getJsonMoeda = requests.get("https://economia.awesomeapi.com.br/json/last/BRL-ARS,USD-ARS,EUR-ARS")
            cotacoes_dic = getJsonMoeda.json()
            # CONVERTE REAL em PESO
            if tipomodTo == 'Real':
                valcotacao = float(cotacoes_dic['BRLARS']['bid'])
                resultado = valEntrada * valcotacao
            # CONVERTE  DOLAR EM EURO
            elif tipomodTo == 'Dólar':
                valcotacao = float(cotacoes_dic['USDARS']['bid'])
                resultado = valEntrada * valcotacao
                # CONVERTE PESO EM EURO
            elif tipomodTo == 'Euro':
                valcotacao = float(cotacoes_dic['EURARS']['bid'])
                resultado = valEntrada * valcotacao

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso")
        resultado = round(resultado, 4)
        msg.setText("Resultado é : " + str(resultado))
        msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi((Principal))
    Principal.show()
    sys.exit(app.exec_())