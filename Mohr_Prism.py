# -*- coding: utf-8 -*-
#-------------------------------------------------
#-- PyQt4 Form implementation generated from reading ui file
#--
#-- Suraj Dadral 2018
#--
#-------------------------------------------------

import FreeCAD as App
import FreeCADGui
import Part,PartGui
import Part
from FreeCAD import Base

import sys
from PySide import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
    	QtGui.QMainWindow.__init__(self, parent)
    	self.setupUi(self)
    	
## the dialog layout

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 103)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.angle_lbl = QtGui.QLabel(self.centralwidget)
        self.angle_lbl.setObjectName("angle_lbl")
        self.verticalLayout.addWidget(self.angle_lbl)
        self.angle = QtGui.QLineEdit(self.centralwidget)
        self.angle.setObjectName("angle")
        self.verticalLayout.addWidget(self.angle)
        self.getPrism = QtGui.QPushButton(self.centralwidget)
        self.getPrism.setObjectName("getPrism")
        self.verticalLayout.addWidget(self.getPrism)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mohr Prism"))
        self.angle_lbl.setText(_translate("MainWindow", "Angle:"))
        self.getPrism.setText(_translate("MainWindow", "Make Prism"))

## Signals and Slots
    	self.getPrism.clicked.connect(self.Prism)

## the gui backend functions
    def Prism(self):
    	Angle=self.angle.text()
    	Angle=int(Angle)
    	App.activeDocument().addObject('PartDesign::Body','Body')
	App.ActiveDocument.recompute()

	App.ActiveDocument.addObject("Part::Box","Box")
	App.ActiveDocument.Box.Length=1000.00
	App.ActiveDocument.Box.Width=1000.00
	App.ActiveDocument.Box.Height=1000.00
	App.ActiveDocument.Box.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
	App.ActiveDocument.Box.Label='Box'
	App.ActiveDocument.Box.Placement=App.Placement(App.Vector(-500,-500,-500), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
	App.ActiveDocument.recompute()

	App.ActiveDocument.addObject("Part::Box","Box001")
	App.ActiveDocument.Box001.Length=710.00
	App.ActiveDocument.Box001.Width=1000.00
	App.ActiveDocument.Box001.Height=1420.00
	App.ActiveDocument.Box001.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
	App.ActiveDocument.Box001.Label='Box'
	App.ActiveDocument.Box001.Placement=App.Placement(App.Vector(0,-500,-710), App.Rotation(App.Vector(0,1,0),-Angle), App.Vector(0,0,710))
	App.ActiveDocument.recompute()

	App.activeDocument().addObject("Part::Cut","Cut")
	App.activeDocument().Cut.Base = App.activeDocument().Box
	App.activeDocument().Cut.Tool = App.activeDocument().Box001
	App.ActiveDocument.recompute()

## the gui startup	
if __name__=='__main__':
	w=MainWindow()
	w.show()
