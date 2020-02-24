# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pandas as pd
import re
from Plotter import *
import scrape_imdb as imdb
import sys


# loop through all csv files in the current directory (Why :( ) and concatenate all the csv files
def create_big_df():
    first = True
    df = None
    for filename in os.listdir(os.curdir):
        if re.match(r'.*\.csv$', filename) is not None:
            if first:
                df = pd.read_csv(filename)
                first = False
            else:
                df = pd.concat([df, pd.read_csv(filename)])
    return df


# If there are no csv files, or scrape is calles as an argument, scrape
if (len(sys.argv) > 1 and sys.argv[1] == 'scrape') or create_big_df() is None:
    for filename in os.listdir(os.curdir):
        if re.match(r'.*\.csv$', filename) is not None:
            os.remove(filename)
    imdb.imdb_scrape_top('imdb_data')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plot_button = QtWidgets.QPushButton(self.centralwidget)
        self.plot_button.setGeometry(QtCore.QRect(330, 400, 141, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.plot_button.setPalette(palette)
        self.plot_button.setObjectName("plot_button")

        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(50, 20, 671, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.main_label.setFont(font)
        self.main_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_label.setObjectName("main_label")
        self.variables_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.variables_comboBox.setGeometry(QtCore.QRect(330, 290, 141, 25))
        self.variables_comboBox.setObjectName("variables_comboBox")
        self.variables_comboBox.addItem("Genres")
        self.variables_comboBox.addItem("Release Date")
        self.variables_comboBox.addItem("Ratings")
        self.variables_comboBox.addItem("Number of Ratings")
        self.variables_comboBox.addItem("World Wide Gross")

        self.explanatory_label = QtWidgets.QLabel(self.centralwidget)
        self.explanatory_label.setGeometry(QtCore.QRect(330, 265, 200, 20))
        self.explanatory_label.setObjectName("explanatory_label")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 151, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 141, 27))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 67, 17))
        self.label_5.setObjectName("label_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 280, 256, 192))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 90, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 90, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 130, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 130, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 170, 113, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 170, 113, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 210, 113, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(350, 210, 113, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 90, 21, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 130, 21, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 170, 21, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 210, 21, 17))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.data_frame = create_big_df()
        self.create_genre_list(self.data_frame['Genres'])

        self.plot_button.clicked.connect(self.plot_graph)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOVIEGOERS"))
        self.plot_button.setText(_translate("MainWindow", "Plot"))
        self.main_label.setText(_translate("MainWindow", "MOVIEGOERS"))
        self.label.setText(_translate("MainWindow", "Gross Range"))
        self.label_2.setText(_translate("MainWindow", "Rating Range"))
        self.label_3.setText(_translate("MainWindow", "Review Count Range"))
        self.label_4.setText(_translate("MainWindow", "Release Date Range\n(years)"))
        self.label_5.setText(_translate("MainWindow", "Genres"))
        self.label_6.setText(_translate("MainWindow", "to"))
        self.label_7.setText(_translate("MainWindow", "to"))
        self.label_8.setText(_translate("MainWindow", "to"))
        self.label_9.setText(_translate("MainWindow", "to"))
        self.explanatory_label.setText(_translate('MainWindow', 'Choose Explanatory Variable'))

    # Create a list of possible genres from all seen genres
    def create_genre_list(self, genres):
        seen = set()
        for genre_list in genres:
            for genre in genre_list.split(' '):
                seen.add(genre)
        for genre in seen:
            self.listWidget.addItem(genre)

    # Plot the graph based on inputted filters
    def plot_graph(self):

        try:
            min_gross = float(self.lineEdit.text())
        except:
            min_gross = None

        try:
            max_gross = float(self.lineEdit_2.text())
        except:
            max_gross = None

        try:
            min_rating = float(self.lineEdit_3.text())
        except:
            min_rating = None

        try:
            max_rating = float(self.lineEdit_4.text())
        except:
            max_rating = None

        try:
            min_count = float(self.lineEdit_5.text())
        except:
            min_count = None

        try:
            max_count = float(self.lineEdit_6.text())
        except:
            max_count = None

        try:
            oldest = float(self.lineEdit_7.text())
        except:
            oldest = None

        try:
            newest = float(self.lineEdit_10.text())
        except:
            newest = None

        accepted_genres = [str(self.listWidget.selectedItems()[i].text()) for i in
                           range(len(self.listWidget.selectedItems()))]
        if accepted_genres == []:
            accepted_genres = None
        else:
            accepted_genres = ' '.join(accepted_genres)

        plotter(self.data_frame).plot(str(self.variables_comboBox.currentText()), max_gross, min_gross,
                                      max_rating, min_rating, max_count, min_count, oldest, newest, accepted_genres)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
