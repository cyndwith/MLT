# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cluster.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Cluster_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transcript = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.transcript.setGeometry(QtCore.QRect(10, 428, 531, 163))
        self.transcript.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transcript.sizePolicy().hasHeightForWidth())
        self.transcript.setSizePolicy(sizePolicy)
        self.transcript.setMaximumSize(QtCore.QSize(531, 163))
        self.transcript.setObjectName("transcript")
        self.progressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressbar.setGeometry(QtCore.QRect(12, 395, 781, 23))
        self.progressbar.setMaximumSize(QtCore.QSize(781, 23))
        self.progressbar.setProperty("value", 0)
        self.progressbar.setTextVisible(False)
        self.progressbar.setObjectName("progressbar")
        self.plot = QtWidgets.QLabel(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(14, 25, 770, 341))
        self.plot.setMaximumSize(QtCore.QSize(770, 341))
        self.plot.setText("")
        self.plot.setObjectName("plot")
        self.Load = QtWidgets.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(558, 526, 111, 31))
        self.Load.setMaximumSize(QtCore.QSize(111, 31))
        self.Load.setObjectName("Load")
        self.Regressionmethods = QtWidgets.QLabel(self.centralwidget)
        self.Regressionmethods.setGeometry(QtCore.QRect(555, 431, 241, 71))
        self.Regressionmethods.setMaximumSize(QtCore.QSize(241, 71))
        self.Regressionmethods.setAutoFillBackground(True)
        self.Regressionmethods.setStyleSheet("")
        self.Regressionmethods.setFrameShape(QtWidgets.QFrame.Box)
        self.Regressionmethods.setText("")
        self.Regressionmethods.setObjectName("Regressionmethods")
        self.regheading = QtWidgets.QLabel(self.centralwidget)
        self.regheading.setGeometry(QtCore.QRect(591, 440, 174, 21))
        self.regheading.setMaximumSize(QtCore.QSize(174, 21))
        self.regheading.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.regheading.setObjectName("regheading")
        self.onevariable = QtWidgets.QRadioButton(self.centralwidget)
        self.onevariable.setGeometry(QtCore.QRect(574, 470, 143, 24))
        self.onevariable.setMaximumSize(QtCore.QSize(143, 24))
        self.onevariable.setObjectName("onevariable")
        self.Load_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Load_2.setGeometry(QtCore.QRect(679, 525, 111, 31))
        self.Load_2.setMaximumSize(QtCore.QSize(111, 31))
        self.Load_2.setObjectName("Load_2")
        self.Load_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Load_3.setGeometry(QtCore.QRect(625, 562, 111, 31))
        self.Load_3.setMaximumSize(QtCore.QSize(111, 31))
        self.Load_3.setObjectName("Load_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(713, 472, 56, 22))
        self.comboBox.setMaximumSize(QtCore.QSize(56, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Xlable = QtWidgets.QLabel(self.centralwidget)
        self.Xlable.setGeometry(QtCore.QRect(677, 471, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Xlable.sizePolicy().hasHeightForWidth())
        self.Xlable.setSizePolicy(sizePolicy)
        self.Xlable.setMaximumSize(QtCore.QSize(21, 21))
        self.Xlable.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.Xlable.setObjectName("Xlable")
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
        self.regheading.setText(_translate("MainWindow", "Clustering methods"))
        self.onevariable.setText(_translate("MainWindow", "K-Means"))
        self.Load_2.setText(_translate("MainWindow", "Process"))
        self.Load_3.setText(_translate("MainWindow", "Close"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.Xlable.setText(_translate("MainWindow", "K ="))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_3.setText(_translate("MainWindow", "Open"))
        self.actionExit_3.setText(_translate("MainWindow", "Exit"))
        self.Load.clicked.connect(self.LoadData)
        self.Load_2.clicked.connect(self.ProcessData)
        self.Load_3.clicked.connect(QtWidgets.qApp.quit)
    def LoadData(self):
        global filenameinterp, filename1interp
        filenameinterp, filter = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', r"C:\\" , '*.csv')
        filename1interp = filenameinterp[:-4]
        print(filenameinterp)

    def ProcessData(self):
        #process clusters
        kvalue = self.comboBox.currentText()
        print(kvalue)
        data = pd.read_csv(filenameinterp)
        #labels = pd.read_csv("cluster\\data_labels.csv")
        x = np.array(data['X']).reshape((-1, 1))
        #y = np.array(data['Y'])
        #labels = labels['Labels']

        kmeans = KMeans(n_clusters=4)
        kmeans.fit(x)
        y_km = kmeans.fit_predict(x)
        print("Done!\n")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Cluster_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
