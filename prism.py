# -*- coding: utf-8 -*-
#-------------------------------------------------
#-- PyQt4 Form implementation generated from reading ui file
#--
#-- Suraj Dadral 2018
#--
#-------------------------------------------------

import FreeCAD as App
import FreeCADGui
import PartDesign
import PartDesignGui
import Sketcher
import math

import sys
from PySide import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
    	QtGui.QMainWindow.__init__(self, parent)
    	self.setupUi(self)
    	
## the dialog layout

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 393)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dimensions_lbl = QtGui.QLabel(self.centralwidget)
        self.dimensions_lbl.setObjectName("dimensions_lbl")
        self.verticalLayout.addWidget(self.dimensions_lbl)
        self.sides_lbl = QtGui.QLabel(self.centralwidget)
        self.sides_lbl.setObjectName("sides_lbl")
        self.verticalLayout.addWidget(self.sides_lbl)
        self.side_a = QtGui.QLineEdit(self.centralwidget)
        self.side_a.setObjectName("side_a")
        self.side_a.setText("5")
        self.verticalLayout.addWidget(self.side_a)
        self.side_b = QtGui.QLineEdit(self.centralwidget)
        self.side_b.setObjectName("side_b")
        self.side_b.setText("5")
        self.verticalLayout.addWidget(self.side_b)
        self.side_c = QtGui.QLineEdit(self.centralwidget)
        self.side_c.setObjectName("side_c")
        self.side_c.setText("5")
        self.verticalLayout.addWidget(self.side_c)
        self.height_lbl = QtGui.QLabel(self.centralwidget)
        self.height_lbl.setObjectName("height_lbl")
        self.verticalLayout.addWidget(self.height_lbl)
        self.height = QtGui.QLineEdit(self.centralwidget)
        self.height.setObjectName("height")
        self.height.setText("10")
        self.verticalLayout.addWidget(self.height)
        self.getPrism = QtGui.QPushButton(self.centralwidget)
        self.getPrism.setObjectName("getPrism")
        self.verticalLayout.addWidget(self.getPrism)
        self.area_lbl = QtGui.QLabel(self.centralwidget)
        self.area_lbl.setObjectName("area_lbl")
        self.verticalLayout.addWidget(self.area_lbl)
        self.area_disp = QtGui.QLineEdit(self.centralwidget)
        self.area_disp.setText("171.650635095")
        self.area_disp.setReadOnly(True)
        self.area_disp.setObjectName("area_disp")
        self.verticalLayout.addWidget(self.area_disp)
        self.volume_lbl = QtGui.QLabel(self.centralwidget)
        self.volume_lbl.setObjectName("volume_lbl")
        self.verticalLayout.addWidget(self.volume_lbl)
        self.volume_disp = QtGui.QLineEdit(self.centralwidget)
        self.volume_disp.setText("108.253175473")
        self.volume_disp.setReadOnly(True)
        self.volume_disp.setObjectName("volume_disp")
        self.verticalLayout.addWidget(self.volume_disp)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
## Signals and Slots	
	self.side_a.textChanged.connect(self.getArea_and_Volume)
	self.side_b.textChanged.connect(self.getArea_and_Volume)
	self.side_c.textChanged.connect(self.getArea_and_Volume)
	self.height.textChanged.connect(self.getArea_and_Volume)
	self.getPrism.clicked.connect(self.Prism)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prism"))
        self.dimensions_lbl.setText(_translate("MainWindow", "Enter dimensions of prism:"))
        self.sides_lbl.setText(_translate("MainWindow", "Sides:"))
        self.height_lbl.setText(_translate("MainWindow", "Height:"))
        self.getPrism.setText(_translate("MainWindow", "Make Prism"))
        self.area_lbl.setText(_translate("MainWindow", "Area:"))
        self.volume_lbl.setText(_translate("MainWindow", "Volume:"))


## the gui backend functions	
    def getArea_and_Volume(self):
    	a_disp=self.side_a.text()
	a=float(a_disp)
	b_disp=self.side_b.text()
	b=float(b_disp)
	c_disp=self.side_c.text()
	c=float(c_disp)
	height_disp=self.height.text()
	height=float(height_disp)
	s=(a+b+c)/2
	ar_tri=math.sqrt(s*(s-a)*(s-b)*(s-c))
	area=2*ar_tri+(a+b+c)*height
	self.area_disp.setText(str(area))
	volume=ar_tri*height
	self.volume_disp.setText(str(volume))

    def Prism(self):
	a_disp=self.side_a.text()
	a=float(a_disp)
	b_disp=self.side_b.text()
	b=float(b_disp)
	c_disp=self.side_c.text()
	c=float(c_disp)
	height_disp=self.height.text()
	height=float(height_disp)
	App.activeDocument().addObject('PartDesign::Body','Body')
	App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch')
	App.activeDocument().Sketch.Support = (App.activeDocument().XZ_Plane, [''])
	App.activeDocument().Sketch.MapMode = 'FlatFace'
	App.ActiveDocument.recompute()
	x=float((a*a+c*c-b*b)/(2*a))
	y=float(math.sqrt(c*c-x*x))
	App.ActiveDocument.Sketch.addGeometry(Part.LineSegment(App.Vector(a,0,0),App.Vector(x,y,0)),False)
	App.ActiveDocument.Sketch.addGeometry(Part.LineSegment(App.Vector(x,y,0),App.Vector(0,0,0)),False)
	App.ActiveDocument.Sketch.addGeometry(Part.LineSegment(App.Vector(0,0,0),App.Vector(a,0,0)),False)
	App.ActiveDocument.recompute()
	App.activeDocument().Body.newObject("PartDesign::Pad","Pad")
	App.activeDocument().Pad.Profile = App.activeDocument().Sketch
	App.activeDocument().Pad.Length = height
	App.ActiveDocument.recompute()

## the gui startup	
if __name__=='__main__':
	w=MainWindow()
	w.show()
