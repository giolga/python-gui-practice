import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets

Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName("Midterm")
        ## added for icon
        MainWindow.setWindowIcon(QtGui.QIcon("mid-term/rect.png"))

        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 70, 361, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageLbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imageLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.imageLbl.setAutoFillBackground(False)
        self.imageLbl.setStyleSheet("QWidget {\n"
"background-color:#e4ffdb\n"
"}")
        self.imageLbl.setScaledContents(True)
        self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLbl.setObjectName("imageLbl")
        self.verticalLayout.addWidget(self.imageLbl)
        self.messageLbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.messageLbl.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.messageLbl.setFont(font)
        self.messageLbl.setStyleSheet("QWidget {\n"
"background-color:#b3e1ff\n"
"}")
        self.messageLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLbl.setWordWrap(True)
        self.messageLbl.setObjectName("messageLbl")
        self.verticalLayout.addWidget(self.messageLbl)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 300, 361, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trapezoidBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.trapezoidBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.trapezoidBtn.setFont(font)
        self.trapezoidBtn.setStyleSheet("")
        self.trapezoidBtn.setObjectName("trapezoidBtn")
        self.horizontalLayout.addWidget(self.trapezoidBtn)
        self.rectangleBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rectangleBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.rectangleBtn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rectangleBtn.setFont(font)
        self.rectangleBtn.setObjectName("rectangleBtn")
        self.horizontalLayout.addWidget(self.rectangleBtn)
        self.squareBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.squareBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.squareBtn.setFont(font)
        self.squareBtn.setObjectName("squareBtn")
        self.horizontalLayout.addWidget(self.squareBtn)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 390, 361, 91))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clearBtn = QtWidgets.QPushButton(self.widget)
        self.clearBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout_2.addWidget(self.clearBtn)
        self.closeBtn = QtWidgets.QPushButton(self.widget)
        self.closeBtn.setMinimumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ####
        self.clearBtn.clicked.connect(self.clearClick)
        self.closeBtn.clicked.connect(self.closeApp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imageLbl.setText(_translate("MainWindow", "ImageLabel"))
        self.messageLbl.setText(_translate("MainWindow", "MessageLabel"))
        self.trapezoidBtn.setText(_translate("MainWindow", "Trapezoid"))
        self.rectangleBtn.setText(_translate("MainWindow", "Rectangle"))
        self.squareBtn.setText(_translate("MainWindow", "Square"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.closeBtn.setText(_translate("MainWindow", "Close App"))

    def trapezoidClick(self, trapezoid):
        print('Trapezoid Clicked')
        self.imageLbl.setPixmap(QtGui.QPixmap("mid-term/trap.png"))
        self.messageLbl.setText(trapezoid)
        # self.messageLbl.adjustSize()

    def rectangleClick(self, rectangle):
        print('Rectangle Clicked')
        self.imageLbl.setPixmap(QtGui.QPixmap("mid-term/rect.png"))
        self.messageLbl.setText(rectangle)
        # self.messageLbl.adjustSize()
    
    def squareClick(self, square):
        print('Square Clicked')
        self.imageLbl.setPixmap(QtGui.QPixmap("mid-term/square.png"))
        self.messageLbl.setText(square)
        # self.messageLbl.adjustSize()

    def clearClick(self):
        self.imageLbl.setPixmap(QtGui.QPixmap(''))
        self.messageLbl.setText('')
    
    def closeApp(self):
        sys.exit(app.exec_())

class Trapezoid(object):
    def __init__(self, list):
        self.a = list[0] # ფუძე
        self.b = list[1]
        self.height = list[2]
    
    def __str__(self):
        return 'Trapezoid has {} cm a, {} cm b and {} cm height'.format(self.a, self.b, self.height)
    
    def area(self):
        self.s = (self.a + self.b) * (self.height / 2)
        return self.s
    
    def __le__(self, other):
        if self.area() <= other.area():
            return True
        return False
    
    def __eq__(self, other):
        if self.area() == other.area():
            return "Both are Eqaul"
        return "Not equal"


class Rectangle(Trapezoid):
    def __init__(self, list):
        super().__init__(list)
        self.height = None

    def area(self):
        self.s = self.a * self.b
        return self.s
    
    def __str__(self):
        return 'Rectangle has {} cm width and {} cm height'.format(self.a, self.b)

class Square(Rectangle):
    def __init__(self, list):
        super().__init__(list)
        self.b = None
    
    def area(self):
        self.s = self.a ** 2
        return self.s
    
    def __str__(self):
        return 'Square has {} cm width and height'.format(self.a) 
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    print(Digit_list, '\n')
    t1 = Trapezoid(Digit_list[0])
    print(t1)
    print(f"area t1 {t1.area()}\n")

    t2 = Trapezoid(Digit_list[1])
    print(t2)
    print(f"area t2 {t2.area()}\n")

    print("Trapzoid 1 is less then or equal to Trapzoid 2:",t1 <= t2)
    print("Trapezoid 1 and Trapezoid 2 are equall:", t1 == t2, '\n\n\n')

    r1 = Rectangle(Digit_list[0])
    print(r1)
    print(f"area r1 {r1.area()}\n")

    r2 = Rectangle(Digit_list[1])
    print(r2)
    print(f"area r2 {r2.area()}\n")

    print("Recangle 1 is less then or equal to rectangle 2:",r1 <= r2)
    print("Recangle 1 and Recangle 2 are equall:", r1 == r2, '\n\n\n')

    s1 = Square(Digit_list[0])
    print(s1)
    print(f"area s1 {s1.area()}\n")

    s2 = Square(Digit_list[5])
    print(s2)
    print(f"area s2 {s2.area()}\n")

    print("Square 1 is less then or equal to Square 2:",s1 <= s2)
    print("Square 1 and Square 2 are equall:", s1 == s2, '\n')

    ui.trapezoidBtn.clicked.connect(lambda: ui.trapezoidClick(str(t1)))
    ui.rectangleBtn.clicked.connect(lambda: ui.rectangleClick(str(r1)))
    ui.squareBtn.clicked.connect(lambda: ui.squareClick(str(s1)))
    sys.exit(app.exec_())
