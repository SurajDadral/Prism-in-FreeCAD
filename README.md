# Prism in FreeCAD
This is a simple form to create Triangular Prism in FreeCAD. It also calculates the Area and Volume of Prism.

## Pre-requisites
* FreeCAD
* PyQt4
* git

To install the above mentioned packages, run the command :   

    ````sudo apt-get install freecad python3-pyqt4 git````

## How to use
1. Open the terminal and download the Source-code in your system with the command :   

    ````git clone https://github.com/SurajDadral/Prism-in-FreeCAD.git prism````

1. Enter the prism directory with the command :   

    ````cd prism````

1. Now copy the prism.py file to FreeCAD's Macro folder (default location is ~/.FreeCAD/Macros):   

    ````cp prism.py ~/.FreeCAD/Macros/````

1. Launch FreeCAD using command:   

    ````freecad````

1. Now click on Macro->Macros and select prism.py and click on execute.   

    (Caution: Make sure you have an opened document in which you wants to create prism)

Have Fun
