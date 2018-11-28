#!/usr/bin/python3
#_*_ coding: utf-8 _*_


import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,
                             QTextEdit, QGridLayout, QApplication, QFrame,QDialog,
                             QPushButton, QMainWindow, QDesktopWidget, QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QColor, QPixmap, QPolygonF, QPainter
from PyQt5.QtChart import QChart, QChartView, QLineSeries
import numpy as np


def series_to_polyline(xdata, ydata):
    """Convert series data to QPolygon(F) polyline
    
    This code is derived from PythonQwt's function named 
    `qwt.plot_curve.series_to_polyline`"""
    size = len(xdata)
    polyline = QPolygonF(size)
    pointer = polyline.data()
    dtype, tinfo = np.float, np.finfo  # integers: = np.int, np.iinfo
    pointer.setsize(2*polyline.size()*tinfo(dtype).dtype.itemsize)
    memory = np.frombuffer(pointer, dtype)
    memory[:(size-1)*2+1:2] = xdata
    memory[1:(size-1)*2+2:2] = ydata
    return polyline

class RelatoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        self.setGeometry(300,300,400,400)
        self.setWindowTitle("Gerar relatório")
        self.show()


class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.initUI()
    def initUI(self):
        #responsável pelo grafico
        self.ncurves = 0
        self.chart = QChart()
        self.chart.legend().hide()
        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        #self.setCentralWidget(self.view)

        npoints = 500000
        xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ydata = [3, 2, 5, 6, 4, 6, 5, 1, 2, 6]
        self.add_data(xdata, ydata, color=Qt.red)
        self.set_title("Simple example with %d curves of %d points "
                     "(OpenGL Accelerated Series)"
                     % (self.ncurves, npoints))
        
        
       
    
        label2 = QLabel()
        image2 = QPixmap("images/blue.png")       
        label2.setPixmap(image2)


        label3 = QLabel()
        image3 = QPixmap("images/green.png")       
        label3.setPixmap(image3)

        top_hBox = QHBoxLayout()#cria layout horizontal superior
        top_hBox.addWidget(self.view)#adiciona o grafico nele
        
        vBox_labels = QVBoxLayout()#cria layout interno superior para informaçoes deping
        text_ping = QLabel("Ping")
        text_send_packages = QLabel("Pacotes enviados")
        text_receive_packages = QLabel("Pacotes recebidos")
        result_ping = QLabel("0")
        result_send_packages = QLabel("0")
        result_receive_packages = QLabel("0")

        vBox_labels.addWidget(text_ping)
        vBox_labels.addWidget(result_ping)
        vBox_labels.addWidget(text_send_packages)
        vBox_labels.addWidget(result_send_packages)
        vBox_labels.addWidget(text_receive_packages)
        vBox_labels.addWidget(result_receive_packages)
        
        top_hBox.addLayout(vBox_labels)
        
        bottom_hBox = QHBoxLayout()
       
        grid = QGridLayout()

        label_mode = QLabel("Modo")
        combo_mode = QComboBox()
        combo_mode.addItem("Server")
        combo_mode.addItem("Client")

        label_conexion = QLabel("Conexão")
        combo_conexion = QComboBox()
        combo_conexion.addItem("TCP")
        combo_conexion.addItem("UDP")

        label_unit = QLabel("Unidade")
        combo_unit = QComboBox()
        combo_unit.addItem("GBits")
        combo_unit.addItem("MBits")

        

        label_ipServer = QLabel("Ip Server")
        edit_ipServer = QLineEdit("127.0.0.1")
        
        label_conexions = QLabel("Conexões paralelas")
        combo_conexions = QComboBox()
        combo_conexions.addItem("1")
        combo_conexions.addItem("2")
        combo_conexions.addItem("3")
        combo_conexions.addItem("4")
        combo_conexions.addItem("5")
        combo_conexions.addItem("6")
        combo_conexions.addItem("7")
        combo_conexions.addItem("8")
        combo_conexions.addItem("9")
        combo_conexions.addItem("10")
        combo_conexions.addItem("20")
        combo_conexions.addItem("30")

        label_bandwidth = QLabel("Bandwidth")
        combo_bandwidth = QComboBox()
        combo_bandwidth.addItem("1 MB")
        combo_bandwidth.addItem("2 MB")
        combo_bandwidth.addItem("3 MB")
        combo_bandwidth.addItem("4 MB")
        combo_bandwidth.addItem("5 MB")
        combo_bandwidth.addItem("10 MB")
        combo_bandwidth.addItem("20 MB")
        combo_bandwidth.addItem("30 MB")
        combo_bandwidth.addItem("40 MB")
        combo_bandwidth.addItem("50 MB")
        combo_bandwidth.addItem("100 MB")
        combo_bandwidth.addItem("200 MB")
        combo_bandwidth.addItem("300 MB")
        combo_bandwidth.addItem("400 MB")
        combo_bandwidth.addItem("500 MB")
        combo_bandwidth.addItem("1 GB")

        grid.addWidget(label_mode, 0, 0)
        grid.addWidget(combo_mode, 1, 0)
        grid.addWidget(label_conexion, 0, 1)
        grid.addWidget(combo_conexion, 1, 1)
        grid.addWidget(label_unit, 0, 2)
        grid.addWidget(combo_unit, 1, 2)

        grid.addWidget(label_ipServer,0,3)
        grid.addWidget(edit_ipServer,1,3)

        grid.addWidget(label_conexions,0,4)
        grid.addWidget(combo_conexions,1,4)

        grid.addWidget(label_bandwidth,0,5)
        grid.addWidget(combo_bandwidth,1,5)

        button_relatory = QPushButton("Gerar Relatorio",self)
        button_relatory.clicked.connect(self.getRelatory)
        button_test = QPushButton("Iniciar teste")
        button_test.setStyleSheet("QWidget{ background-color: %s}" % QColor(0,240,100).name())

        grid.addWidget(button_relatory,0,6) 
        grid.addWidget(button_test,1,6) 

        bottom_hBox.addLayout(grid)


        global_vBox = QVBoxLayout(self)
        global_vBox.addLayout(top_hBox)
        global_vBox.addLayout(bottom_hBox)
        
        self.setLayout(global_vBox)

        self.setGeometry(500,100,1000,600)
        self.center()
        self.setWindowTitle("Pyperf")
        self.show()
    
    def getRelatory(self):
        
        relatoryWindow = RelatoryWindow()   
        relatoryWindow.show()
        relatoryWindow.exec_()  
        
        

    
    def set_title(self, title):
        self.chart.setTitle(title)

    def add_data(self, xdata, ydata, color=None):
        curve = QLineSeries()
        pen = curve.pen()
        if color is not None:
            pen.setColor(color)
        pen.setWidthF(.1)
        curve.setPen(pen)
        curve.setUseOpenGL(True)
        curve.append(series_to_polyline(xdata, ydata))
        self.chart.addSeries(curve)
        self.chart.createDefaultAxes()
        self.ncurves += 1

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    sys.exit(app.exec_())


