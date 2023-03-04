import sys


from PyQt5.QtWidgets import (

    QApplication,

    QCheckBox,

    QTabWidget,

    QVBoxLayout,

    QWidget,
    
    QComboBox,

    QSlider,

    QLabel,

    QPushButton,

    QDialog,

    QSizePolicy,

    QGridLayout

)
# THIS PROGRAM NEEDS TO RUN AS ROOT!
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5 import QtGui, QtCore

from pyqt_color_picker import ColorPickerDialog

import main
class Window(QWidget):
    tabWidgets = []
    def closeEvent(self, ev):
        print("Detaching from mouse")
        main.detach_mouse()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("XENON 770")
        self.resize(270, 110)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.RGBTab(), "RGB")
        tabs.addTab(self.macroTabUI(), "Macro")
        layout.addWidget(tabs)


    def RGBTab(self):
        print("Attaching to mouse")
        main.attach_mouse()
        RGBTab = QWidget()
        layout = QVBoxLayout()
        comboBox = QComboBox()

        comboBox.addItem("PRISMO Effect")
        comboBox.addItem("Steady")
        comboBox.addItem("Breathing")
        comboBox.addItem("Colorful Tail")
        comboBox.addItem("Neon")
        comboBox.addItem("Colorful Steady")
        comboBox.addItem("Flicker")
        comboBox.addItem("Stars Twinkle")
        comboBox.addItem("Wave")
        comboBox.addItem("LED Off")

        comboBox.currentIndexChanged.connect(lambda i: self.RGBSelectionChanged(i, RGBTab))
        layout.addWidget(comboBox)
        layout.setAlignment(Qt.AlignTop)
        RGBTab.setLayout(layout)
        self.RGBSelectionChanged(0, RGBTab)
        
        return RGBTab
    def cleanRGBTab(self, RGBTab):
        for widget in self.tabWidgets:
            RGBTab.layout().removeWidget(widget)
            widget.setParent(None)
        self.tabWidgets = []
        self.setFixedSize(270, 110)
    def macroTabUI(self):

        macroTab = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Not implemented yet, but some \nstuff has been implemented \nin main.py. \nCheck that out, if u want."))
        layout.setAlignment(Qt.AlignTop)
        macroTab.setLayout(layout)
        
        return macroTab
    def RGBSelectionChanged(self, selectionIndex, RGBTab):
        self.cleanRGBTab(RGBTab)
        options = {
           0 : self.prismoEffect,
           1 : self.steadyEffect,
           2 : self.breathingEffect,
           3 : self.colorfulTailEffect,
           4 : self.neonEffect,
           5 : self.colorfulSteadyEffect,
           6 : self.flickerEffect,
           7 : self.starsTwinkleEffect,
           8 : self.waveEffect,
           9 : self.LEDOff,
        }
        options[selectionIndex](RGBTab)
    def addTabWidget(self,widget, RGBTab):
        self.setFixedSize(self.geometry().width(),self.geometry().height() + int(widget.sizeHint().height() + 5))
        RGBTab.layout().addWidget(widget,1)
        self.tabWidgets.append(widget)
    def prismoEffect(self,RGBTab):
        modeID = 1
        label = QLabel("Effect speed:")
        self.addTabWidget(label, RGBTab)
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMaximum(3)
        speedSlider.setMinimum(1)
        speedSlider.setValue(2)
        speedSlider.valueChanged.connect(lambda i: self.handleSpeedChange(i, modeID))
        self.addTabWidget(speedSlider, RGBTab)
        label = QLabel("Direction:")
        self.addTabWidget(label, RGBTab)
        upBtn = QPushButton("←")
        upBtn.clicked.connect(lambda a: self.handleSetDirection(1))
        self.addTabWidget(upBtn, RGBTab)
        downBtn = QPushButton("→")
        downBtn.clicked.connect(lambda a: self.handleSetDirection(0))
        self.addTabWidget(downBtn, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def steadyEffect(self,RGBTab):
        modeID = 2
        colorPickBtn = QPushButton("Pick a Color")
        colorPickBtn.clicked.connect(lambda t, modeID=modeID : self.handleColorChange(modeID=modeID, colorID=0))
        self.addTabWidget(colorPickBtn, RGBTab)
        brightnessSlider = QSlider(Qt.Horizontal)
        brightnessSlider.setMaximum(4)
        brightnessSlider.setMinimum(1)
        brightnessSlider.setValue(2)
        brightnessSlider.valueChanged.connect(lambda i: self.handleBrightnessChange(i, modeID))
        label = QLabel("Brightness:")
        self.addTabWidget(label, RGBTab)
        self.addTabWidget(brightnessSlider, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def breathingEffect(self,RGBTab):
        modeID = 3
        label = QLabel("Effect speed:")
        self.addTabWidget(label, RGBTab)
        # Speed slider for RGB speed control.
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMaximum(3)
        speedSlider.setMinimum(1)
        speedSlider.setValue(2)
        speedSlider.valueChanged.connect(lambda i: self.handleSpeedChange(i, modeID))
        self.addTabWidget(speedSlider, RGBTab)
        # Create 7 buttons with the following: 'X Color' to set the colors
        for i in range(7):
            self.colorPickBtn = QPushButton('Color {}'.format(i +1), self)
            self.colorPickBtn.clicked.connect(lambda t, i=i : self.handleColorChange(modeID=modeID, colorID=i + 1))
            self.addTabWidget(self.colorPickBtn, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def colorfulTailEffect(self,RGBTab):
        modeID = 4
        label = QLabel("Effect speed:")
        self.addTabWidget(label, RGBTab)
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMaximum(3)
        speedSlider.setMinimum(1)
        speedSlider.setValue(2)
        speedSlider.valueChanged.connect(lambda i: self.handleSpeedChange(i, modeID))
        self.addTabWidget(speedSlider, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def neonEffect(self,RGBTab):
        modeID = 5
        label = QLabel("Effect speed:")
        self.addTabWidget(label, RGBTab)
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMaximum(3)
        speedSlider.setMinimum(1)
        speedSlider.setValue(2)
        speedSlider.valueChanged.connect(lambda i: self.handleSpeedChange(i, modeID))
        self.addTabWidget(speedSlider, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def colorfulSteadyEffect(self,RGBTab):
        modeID = 6
        # Create 6 buttons with the following: 'X Color' to set the colors
        for i in range(6):
            self.colorPickBtn = QPushButton('Color {}'.format(i +1), self)
            self.colorPickBtn.clicked.connect(lambda t, i=i : self.handleColorChange(modeID=modeID, colorID=i + 1))
            self.addTabWidget(self.colorPickBtn, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def flickerEffect(self,RGBTab):
        modeID = 7
        # Create 2 buttons with the following: 'X Color' to set the colors
        for i in range(2):
            self.colorPickBtn = QPushButton('Color {}'.format(i +1), self)
            self.colorPickBtn.clicked.connect(lambda t, i=i : self.handleColorChange(modeID=modeID, colorID=i + 1))
            self.addTabWidget(self.colorPickBtn, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def starsTwinkleEffect(self,RGBTab):
        modeID = 8
        label = QLabel("Effect speed:")
        self.addTabWidget(label, RGBTab)
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMaximum(3)
        speedSlider.setMinimum(1)
        speedSlider.setValue(2)
        speedSlider.valueChanged.connect(lambda i: self.handleSpeedChange(i, modeID))
        self.addTabWidget(speedSlider, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def waveEffect(self,RGBTab):
        modeID = 9
        label = QLabel("Effect speed:")
        self.addTabWidget(label, RGBTab)
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMaximum(3)
        speedSlider.setMinimum(1)
        speedSlider.setValue(2)
        speedSlider.valueChanged.connect(lambda i: self.handleSpeedChange(i, modeID))
        self.addTabWidget(speedSlider, RGBTab)
        main.setMode(main.getMemory(True), modeID)
    def LEDOff(self,RGBTab):
        modeID = 0
        main.setMode(main.getMemory(True), modeID)


    # Handling changes
    def handleColorChange(self, modeID, colorID):
        dialog = ColorPickerDialog()
        reply = dialog.exec()
        options = {
           0 : None,
           1 : None,
           2 : main.setSteadyColor,
           3 : main.setBreathingModeColor,
           4 : None,
           5 : None,
           6 : main.setColorfulSteadyModeColor,
           7 : main.setFlickerModeColor,
           8 : None,
           9 : None,
        }
        if reply == QDialog.Accepted:
            if(modeID != 2):
                print("Changing effect color EFFECT ID: " + str(modeID) + " COLOR: " + dialog.getColor().name() + " Color num: " + str(colorID))
                options[modeID](main.getMemory(True), dialog.getColor().name().replace("#", ""), colorID)
            else:
                print("Changing effect color EFFECT ID: " + str(modeID) + " COLOR: " + dialog.getColor().name())
                options[modeID](main.getMemory(True), dialog.getColor().name().replace("#", ""))
    
    def handleSpeedChange(self, speed, effectID):
        print("Changing effect speed EFFECT ID: " + str(effectID) + " SPEED: " + str(speed))
        main.setModeSpeed(main.getMemory(True), speed)
    def handleBrightnessChange(self, brightness, effectID):
        print("Changing brightness EFFECT ID: " + str(effectID) + " SPEED: " + str(brightness))
        main.setSteadyModeBrightness(main.getMemory(True), brightness)

    def handleSetDirection(self,direction):
        print("Changing prismo effect direction to: " + str(direction))
        main.setPrismoEffectModeDirection(main.getMemory(True), direction)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
