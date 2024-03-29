# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd


class Interp_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(800, 598))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transcript = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.transcript.setEnabled(False)
        self.transcript.setGeometry(QtCore.QRect(10, 326, 517, 265))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transcript.sizePolicy().hasHeightForWidth())
        self.transcript.setSizePolicy(sizePolicy)
        self.transcript.setMaximumSize(QtCore.QSize(517, 265))
        self.transcript.setStyleSheet("font: 12pt \"Arial\";")
        self.transcript.setObjectName("transcript")
        self.progressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressbar.setGeometry(QtCore.QRect(10, 280, 518, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar.sizePolicy().hasHeightForWidth())
        self.progressbar.setSizePolicy(sizePolicy)
        self.progressbar.setMaximumSize(QtCore.QSize(518, 23))
        self.progressbar.setProperty("value", 0)
        self.progressbar.setTextVisible(False)
        self.progressbar.setObjectName("progressbar")
        self.plot = QtWidgets.QLabel(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(14, 25, 511, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setText("")
        self.plot.setObjectName("plot")
        self.Load = QtWidgets.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(549, 165, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load.sizePolicy().hasHeightForWidth())
        self.Load.setSizePolicy(sizePolicy)
        self.Load.setMaximumSize(QtCore.QSize(111, 31))
        self.Load.setStyleSheet("font: 8pt \"Arial\";")
        self.Load.setObjectName("Load")
        self.Testlabel = QtWidgets.QLabel(self.centralwidget)
        self.Testlabel.setGeometry(QtCore.QRect(550, 208, 241, 344))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Testlabel.sizePolicy().hasHeightForWidth())
        self.Testlabel.setSizePolicy(sizePolicy)
        self.Testlabel.setMaximumSize(QtCore.QSize(241, 344))
        self.Testlabel.setAutoFillBackground(True)
        self.Testlabel.setStyleSheet("")
        self.Testlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.Testlabel.setText("")
        self.Testlabel.setObjectName("Testlabel")
        self.Testlabelheading = QtWidgets.QLabel(self.centralwidget)
        self.Testlabelheading.setGeometry(QtCore.QRect(620, 220, 106, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Testlabelheading.sizePolicy().hasHeightForWidth())
        self.Testlabelheading.setSizePolicy(sizePolicy)
        self.Testlabelheading.setMaximumSize(QtCore.QSize(106, 21))
        self.Testlabelheading.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Testlabelheading.setObjectName("Testlabelheading")
        self.Xlable = QtWidgets.QLabel(self.centralwidget)
        self.Xlable.setGeometry(QtCore.QRect(560, 260, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Xlable.sizePolicy().hasHeightForWidth())
        self.Xlable.setSizePolicy(sizePolicy)
        self.Xlable.setMaximumSize(QtCore.QSize(21, 21))
        self.Xlable.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"Arial\";")
        self.Xlable.setObjectName("Xlable")
        self.Ylable = QtWidgets.QLabel(self.centralwidget)
        self.Ylable.setGeometry(QtCore.QRect(560, 330, 21, 21))
        self.Ylable.setMaximumSize(QtCore.QSize(21, 21))
        self.Ylable.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"Arial\";")
        self.Ylable.setObjectName("Ylable")
        self.Xnote = QtWidgets.QLabel(self.centralwidget)
        self.Xnote.setGeometry(QtCore.QRect(555, 295, 230, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Xnote.sizePolicy().hasHeightForWidth())
        self.Xnote.setSizePolicy(sizePolicy)
        self.Xnote.setMaximumSize(QtCore.QSize(230, 21))
        self.Xnote.setStyleSheet("text-decoration: underline;\n"
"font: 8pt \"Arial\";\n"
"")
        self.Xnote.setObjectName("Xnote")
        self.Ynote = QtWidgets.QLabel(self.centralwidget)
        self.Ynote.setGeometry(QtCore.QRect(558, 363, 230, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ynote.sizePolicy().hasHeightForWidth())
        self.Ynote.setSizePolicy(sizePolicy)
        self.Ynote.setMaximumSize(QtCore.QSize(230, 21))
        self.Ynote.setStyleSheet("text-decoration: underline;\n"
"font: 8pt \"Arial\";\n"
"")
        self.Ynote.setObjectName("Ynote")
        self.resultoutput = QtWidgets.QTextEdit(self.centralwidget)
        self.resultoutput.setGeometry(QtCore.QRect(560, 451, 223, 90))
        self.resultoutput.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultoutput.sizePolicy().hasHeightForWidth())
        self.resultoutput.setSizePolicy(sizePolicy)
        self.resultoutput.setMaximumSize(QtCore.QSize(223, 90))
        self.resultoutput.setAutoFillBackground(False)
        self.resultoutput.setStyleSheet("")
        self.resultoutput.setFrameShape(QtWidgets.QFrame.Box)
        self.resultoutput.setMidLineWidth(0)
        self.resultoutput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultoutput.setObjectName("resultoutput")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(650, 430, 79, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        self.result.setMaximumSize(QtCore.QSize(79, 21))
        self.result.setStyleSheet("font: 75 10pt \"Arial\";\n"
"text-decoration: underline;")
        self.result.setObjectName("result")
        self.Regressionmethods = QtWidgets.QLabel(self.centralwidget)
        self.Regressionmethods.setGeometry(QtCore.QRect(550, 20, 241, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Regressionmethods.sizePolicy().hasHeightForWidth())
        self.Regressionmethods.setSizePolicy(sizePolicy)
        self.Regressionmethods.setMaximumSize(QtCore.QSize(241, 131))
        self.Regressionmethods.setAutoFillBackground(True)
        self.Regressionmethods.setStyleSheet("")
        self.Regressionmethods.setFrameShape(QtWidgets.QFrame.Box)
        self.Regressionmethods.setText("")
        self.Regressionmethods.setObjectName("Regressionmethods")
        self.regheading = QtWidgets.QLabel(self.centralwidget)
        self.regheading.setGeometry(QtCore.QRect(586, 30, 174, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regheading.sizePolicy().hasHeightForWidth())
        self.regheading.setSizePolicy(sizePolicy)
        self.regheading.setMaximumSize(QtCore.QSize(174, 21))
        self.regheading.setStyleSheet("font: 75 10pt \"Arial\";")
        self.regheading.setObjectName("regheading")
        self.onevariable = QtWidgets.QRadioButton(self.centralwidget)
        self.onevariable.setGeometry(QtCore.QRect(570, 60, 143, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onevariable.sizePolicy().hasHeightForWidth())
        self.onevariable.setSizePolicy(sizePolicy)
        self.onevariable.setMaximumSize(QtCore.QSize(143, 24))
        self.onevariable.setStyleSheet("font: 8pt \"Arial\";")
        self.onevariable.setObjectName("onevariable")
        self.multivariable = QtWidgets.QRadioButton(self.centralwidget)
        self.multivariable.setGeometry(QtCore.QRect(570, 90, 197, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multivariable.sizePolicy().hasHeightForWidth())
        self.multivariable.setSizePolicy(sizePolicy)
        self.multivariable.setMaximumSize(QtCore.QSize(197, 24))
        self.multivariable.setStyleSheet("font: 8pt \"Arial\";")
        self.multivariable.setObjectName("multivariable")
        self.poly = QtWidgets.QRadioButton(self.centralwidget)
        self.poly.setGeometry(QtCore.QRect(570, 120, 175, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.poly.sizePolicy().hasHeightForWidth())
        self.poly.setSizePolicy(sizePolicy)
        self.poly.setMaximumSize(QtCore.QSize(175, 24))
        self.poly.setStyleSheet("font: 8pt \"Arial\";")
        self.poly.setObjectName("poly")
        self.Load_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Load_2.setGeometry(QtCore.QRect(678, 164, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load_2.sizePolicy().hasHeightForWidth())
        self.Load_2.setSizePolicy(sizePolicy)
        self.Load_2.setMaximumSize(QtCore.QSize(111, 31))
        self.Load_2.setStyleSheet("font: 8pt \"Arial\";")
        self.Load_2.setObjectName("Load_2")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(620, 390, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calculate.sizePolicy().hasHeightForWidth())
        self.Calculate.setSizePolicy(sizePolicy)
        self.Calculate.setMaximumSize(QtCore.QSize(93, 28))
        self.Calculate.setStyleSheet("font: 75 10pt \"Arial\";")
        self.Calculate.setObjectName("Calculate")
        self.Load_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Load_3.setGeometry(QtCore.QRect(616, 565, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load_3.sizePolicy().hasHeightForWidth())
        self.Load_3.setSizePolicy(sizePolicy)
        self.Load_3.setMaximumSize(QtCore.QSize(111, 31))
        self.Load_3.setStyleSheet("font: 8pt \"Arial\";")
        self.Load_3.setObjectName("Load_3")
        self.Xvalues = QtWidgets.QLineEdit(self.centralwidget)
        self.Xvalues.setGeometry(QtCore.QRect(587, 259, 182, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Xvalues.sizePolicy().hasHeightForWidth())
        self.Xvalues.setSizePolicy(sizePolicy)
        self.Xvalues.setMaximumSize(QtCore.QSize(182, 31))
        self.Xvalues.setObjectName("Xvalues")
        self.Yvalues = QtWidgets.QLineEdit(self.centralwidget)
        self.Yvalues.setGeometry(QtCore.QRect(587, 326, 182, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Yvalues.sizePolicy().hasHeightForWidth())
        self.Yvalues.setSizePolicy(sizePolicy)
        self.Yvalues.setMaximumSize(QtCore.QSize(182, 31))
        self.Yvalues.setObjectName("Yvalues")
        self.Testlabel.raise_()
        self.resultoutput.raise_()
        self.transcript.raise_()
        self.progressbar.raise_()
        self.plot.raise_()
        self.Load.raise_()
        self.Testlabelheading.raise_()
        self.Xlable.raise_()
        self.Ylable.raise_()
        self.Xnote.raise_()
        self.Ynote.raise_()
        self.result.raise_()
        self.Regressionmethods.raise_()
        self.regheading.raise_()
        self.onevariable.raise_()
        self.multivariable.raise_()
        self.poly.raise_()
        self.Load_2.raise_()
        self.Calculate.raise_()
        self.Load_3.raise_()
        self.Xvalues.raise_()
        self.Yvalues.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionOpen_3 = QtWidgets.QAction(MainWindow)
        self.actionOpen_3.setObjectName("actionOpen_3")
        self.actionExit_3 = QtWidgets.QAction(MainWindow)
        self.actionExit_3.setObjectName("actionExit_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Load.setText(_translate("MainWindow", "Load"))
        self.Testlabelheading.setText(_translate("MainWindow", "Test Zone"))
        self.Xlable.setText(_translate("MainWindow", "X"))
        self.Ylable.setText(_translate("MainWindow", "Y"))
        self.Xnote.setText(_translate("MainWindow", "Note: Seperate multiple X by comma"))
        self.Ynote.setText(_translate("MainWindow", "Note: Expected Y value [Optional]"))
        self.result.setText(_translate("MainWindow", "Result"))
        self.regheading.setText(_translate("MainWindow", "Regression methods"))
        self.onevariable.setText(_translate("MainWindow", "One-variable Linear"))
        self.multivariable.setText(_translate("MainWindow", "Multi-variable Linear"))
        self.poly.setText(_translate("MainWindow", "Higher Order Polynomial"))
        self.Load_2.setText(_translate("MainWindow", "Process"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.Load_3.setText(_translate("MainWindow", "Close"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_3.setText(_translate("MainWindow", "Open"))
        self.actionExit_3.setText(_translate("MainWindow", "Exit"))
        self.Load.clicked.connect(self.LoadData)
        self.Load_2.clicked.connect(self.ProcessData)
        self.Calculate.clicked.connect(self.Calculatevalues)
        self.Load_3.clicked.connect(QtWidgets.qApp.quit)
        self.transcript.setPlainText("Hello")
    def LoadData(self):
        global filenameinterp, filename1interp
        filenameinterp, filter = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', r"C:\\" , '*.csv')
        filename1interp = filenameinterp[:-4]
        print(filenameinterp)

    def ProcessData(self):
        global model
#write csv import code
        if self.onevariable.isChecked():
            #read csv import code
            data = pd.read_csv(filenameinterp)
            x = np.array(data['X']).reshape((-1,1))
            y = np.array(data['Y'])
            model = LinearRegression()
            model.fit(x,y)
            print('slope:', model.coef_)
            print('intercept:', model.intercept_)
        if self.multivariable.isChecked():
            data = pd.read_csv(filenameinterp)
            x1 = np.array(data['X1']).reshape((-1,1))
            x2 = np.array(data['X2']).reshape((-1,1))
            x = np.concatenate((x1, x2), axis=1)
            y = np.array(data['Y'])
            model = LinearRegression().fit(x,y)
            model.fit(x,y)
            print('coefficients:', model.coef_)
            print('intercept:', model.intercept_)
        if self.poly.isChecked():
            data = pd.read_csv(filenameinterp)
            x = np.array(data['X']).reshape((-1, 1))
            y = np.array(data['Y'])
            transformer = PolynomialFeatures(degree=2, include_bias=False)
            transformer.fit(x)
            x_trans = transformer.transform(x)
            model = LinearRegression().fit(x_trans, y)
            print('coefficients:', model.coef_)
            print('intercept:', model.intercept_)
    def Calculatevalues(self):
#predict new values
        Xdata = self.Xvalues.text()
        print(Xdata)
        Xdata_values = Xdata.split()
        print(Xdata_values)
        Ydata = self.Yvalues.text()
        Ydata_values = Ydata.split()
        #x = np.array(Xdata).reshape((-1, 1))
        x = np.array(Xdata_values)
        x = x.astype(np.float)
        x = x.reshape((-1,1))
        print(x)
        Y_pred = model.predict(x)
        print(Y_pred)
        y = np.array(Ydata_values)
        y = y.astype(np.float)
        y = y.reshape((-1, 1))
        error = np.subtract(y, Y_pred) # * 100 / Ydata
        print(error)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Interp_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

