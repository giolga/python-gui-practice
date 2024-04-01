import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets

Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        ## added for icon
        Form.setWindowIcon(QtGui.QIcon("mid-term/trap.png"))

        Form.resize(400, 450)
        Form.setMinimumSize(QtCore.QSize(400, 450))
        Form.setMaximumSize(QtCore.QSize(600, 450))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget {\n"
"   background-color:#d4ebff;\n"
"}")
        self.imgLabel = QtWidgets.QLabel(Form)
        self.imgLabel.setGeometry(QtCore.QRect(20, 10, 361, 201))

        #added later
        self.imgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # self.imgLabel.setFrameShape(QtWidgets.QFrame.Box) #Extra:)
        # self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.imgLabel.setText("")
        # self.imgLabel.setPixmap(QtGui.QPixmap(""))


        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.imgLabel.setFont(font)
        self.imgLabel.setStyleSheet("QWidget {\n"
"background-color:#eaffd2\n"
"}")
        self.imgLabel.setObjectName("imgLabel")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(70, 400, 100, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.closeBtn = QtWidgets.QPushButton(Form)
        self.closeBtn.setGeometry(QtCore.QRect(220, 400, 100, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(20, 220, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.messageLabel.setFont(font)
        self.messageLabel.setStyleSheet("QWidget {\n"
"background-color:#ffdcdc\n"
"}")
        self.messageLabel.setObjectName("messageLabel")

        self.messageLabel.setWordWrap(True)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(57, 330, 291, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trapezoidBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.trapezoidBtn.setFont(font)
        self.trapezoidBtn.setStyleSheet("QWidget {\n"
"background-color:#c5ffa1\n"
"}")
        self.trapezoidBtn.setObjectName("trapezoidBtn")
        self.horizontalLayout.addWidget(self.trapezoidBtn)
        self.rectangleBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rectangleBtn.setFont(font)
        self.rectangleBtn.setStyleSheet("QWidget {\n"
"background-color:#c5ffa1\n"
"}")
        self.rectangleBtn.setObjectName("rectangleBtn")
        self.horizontalLayout.addWidget(self.rectangleBtn)
        self.squareBtn = QtWidgets.QPushButton(self.widget)
        self.squareBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.squareBtn.setFont(font)
        self.squareBtn.setStyleSheet("QWidget {\n"
"background-color:#c5ffa1\n"
"}")
        self.squareBtn.setObjectName("squareBtn")
        self.horizontalLayout.addWidget(self.squareBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # self.trapezoidBtn.clicked.connect(self.trapezoidClick)
        # self.squareBtn.clicked.connect(self.squareClick)
        # self.rectangleBtn.clicked.connect(self.rectangleClick)
        self.clearBtn.clicked.connect(self.clearClick)
        self.closeBtn.clicked.connect(self.closeApp)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.imgLabel.setText(_translate("Form", "Image of Shape"))
        self.clearBtn.setText(_translate("Form", "Clear"))
        self.closeBtn.setText(_translate("Form", "Close App"))
        self.messageLabel.setText(_translate("Form", "TextLabel"))
        self.trapezoidBtn.setText(_translate("Form", "Trapezoid"))
        self.rectangleBtn.setText(_translate("Form", "Rectangle"))

        self.squareBtn.setText(_translate("Form", "Square"))

    def trapezoidClick(self, trapezoid):
        print('Trapezoid Clicked')
        self.imgLabel.setPixmap(QtGui.QPixmap("mid-term/trap.png"))
        self.messageLabel.setText(trapezoid)
        # self.messageLabel.adjustSize()

    def rectangleClick(self, rectangle):
        print('Rectangle Clicked')
        self.imgLabel.setPixmap(QtGui.QPixmap("mid-term/rect.png"))
        self.messageLabel.setText(rectangle)
        # self.messageLabel.adjustSize()
    
    def squareClick(self, square):
        print('Square Clicked')
        self.imgLabel.setPixmap(QtGui.QPixmap("mid-term/square.png"))
        self.messageLabel.setText(square)
        # self.messageLabel.adjustSize()

    def clearClick(self):
        self.imgLabel.setPixmap(QtGui.QPixmap(''))
        self.messageLabel.setText('')
    
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
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()

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