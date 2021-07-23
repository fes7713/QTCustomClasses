from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileSystemModel, QTreeView
from KClass.PowerPointPreview import Preview

class TaskDialog(QtWidgets.QDialog):
    def __init__(self, Dialog):
        super().__init__()
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 154)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.taskLabel = QtWidgets.QLabel(Dialog)
        self.taskLabel.setObjectName("taskLabel")
        self.verticalLayout.addWidget(self.taskLabel)
        self.taskText = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskText.sizePolicy().hasHeightForWidth())
        self.taskText.setSizePolicy(sizePolicy)
        self.taskText.setObjectName("taskText")
        self.verticalLayout.addWidget(self.taskText)
        self.timeLabel = QtWidgets.QLabel(Dialog)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hourCombo = QtWidgets.QComboBox(Dialog)
        self.hourCombo.setObjectName("hourCombo")
        self.horizontalLayout.addWidget(self.hourCombo)
        self.minuteCombo = QtWidgets.QComboBox(Dialog)
        self.minuteCombo.setObjectName("minuteCombo")
        self.horizontalLayout.addWidget(self.minuteCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.model_hour = QtCore.QStringListModel()
        self.model_minute = QtCore.QStringListModel()

        self.model_hour.setStringList([str(n) for n in list(range(24))])
        self.model_minute.setStringList([str(n) for n in list(range(60))])
        self.hourCombo.setModel(self.model_hour)
        self.minuteCombo.setModel(self.model_minute)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.taskLabel.setText(_translate("Dialog", "Enter Task"))
        self.timeLabel.setText(_translate("Dialog", "Target Time"))

    def getText(self):
        return self.taskText.text(), self.hourCombo.currentText(), self.minuteCombo.currentText()

    def returnNumber(self):
        return 3


class PowerPointSettingDialog(QtWidgets.QDialog):
    def __init__(self, Dialog):
        super().__init__()
        Dialog.setObjectName("Dialog")
        Dialog.resize(1085, 622)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        ##############################
        self.widget = Preview(3, 3, 2, 6)
        #####################################
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(420, 594))
        self.widget.setObjectName("widget")
        self.verticalLayout_7.addWidget(self.widget)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.titleTopLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleTopLabel.sizePolicy().hasHeightForWidth())
        self.titleTopLabel.setSizePolicy(sizePolicy)
        self.titleTopLabel.setObjectName("titleTopLabel")
        self.horizontalLayout_3.addWidget(self.titleTopLabel)
        self.titleTopSpinBox = QtWidgets.QSpinBox(Dialog)
        self.titleTopSpinBox.setObjectName("titleTopSpinBox")
        self.horizontalLayout_3.addWidget(self.titleTopSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.titleTopSlider = QtWidgets.QSlider(Dialog)
        self.titleTopSlider.setOrientation(QtCore.Qt.Horizontal)
        self.titleTopSlider.setObjectName("titleTopSlider")
        self.verticalLayout_3.addWidget(self.titleTopSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.titleLeftLabel = QtWidgets.QLabel(Dialog)
        self.titleLeftLabel.setObjectName("titleLeftLabel")
        self.horizontalLayout_4.addWidget(self.titleLeftLabel)
        self.titleLeftSpinBox = QtWidgets.QSpinBox(Dialog)
        self.titleLeftSpinBox.setObjectName("titleLeftSpinBox")
        self.horizontalLayout_4.addWidget(self.titleLeftSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.titleLeftSlider = QtWidgets.QSlider(Dialog)
        self.titleLeftSlider.setOrientation(QtCore.Qt.Horizontal)
        self.titleLeftSlider.setObjectName("titleLeftSlider")
        self.verticalLayout_3.addWidget(self.titleLeftSlider)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.paddingLabel = QtWidgets.QLabel(Dialog)
        self.paddingLabel.setObjectName("paddingLabel")
        self.horizontalLayout_5.addWidget(self.paddingLabel)
        self.paddingSpinBox = QtWidgets.QSpinBox(Dialog)
        self.paddingSpinBox.setObjectName("paddingSpinBox")
        self.horizontalLayout_5.addWidget(self.paddingSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.paddingSlider = QtWidgets.QSlider(Dialog)
        self.paddingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.paddingSlider.setObjectName("paddingSlider")
        self.verticalLayout_3.addWidget(self.paddingSlider)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.titleHeightLabel = QtWidgets.QLabel(Dialog)
        self.titleHeightLabel.setObjectName("titleHeightLabel")
        self.horizontalLayout_8.addWidget(self.titleHeightLabel)
        self.titleHeightSpinBox = QtWidgets.QSpinBox(Dialog)
        self.titleHeightSpinBox.setObjectName("titleHeightSpinBox")
        self.horizontalLayout_8.addWidget(self.titleHeightSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.titleHeightSlider = QtWidgets.QSlider(Dialog)
        self.titleHeightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.titleHeightSlider.setObjectName("titleHeightSlider")
        self.verticalLayout_3.addWidget(self.titleHeightSlider)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.FileLabel = QtWidgets.QLabel(Dialog)
        self.FileLabel.setObjectName("FileLabel")
        self.horizontalLayout_6.addWidget(self.FileLabel)
        self.fileNameEntry = QtWidgets.QLineEdit(Dialog)
        self.fileNameEntry.setObjectName("fileNameEntry")
        self.horizontalLayout_6.addWidget(self.fileNameEntry)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.fileTreeView = QtWidgets.QTreeView(Dialog)
        self.fileTreeView.setAlternatingRowColors(True)
        self.fileTreeView.setObjectName("fileTreeView")
        self.verticalLayout_3.addWidget(self.fileTreeView)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        PATH = 'C:\\'
        model = QFileSystemModel()
        model.setRootPath(PATH)


        # TreeView
        self.fileTreeView.setModel(model)
        self.fileTreeView.setRootIndex(model.index(PATH))
        self.fileTreeView.clicked.connect(self.getFile)

        self.titleTopSlider.valueChanged.connect(self.updateTitleTop)
        self.titleLeftSlider.valueChanged.connect(self.updateTitleLeft)
        self.titleHeightSlider.valueChanged.connect(self.updateTitleHeight)
        self.paddingSlider.valueChanged.connect(self.updatePadding)

        self.titleTopSpinBox.valueChanged.connect(self.updateTitleTop)
        self.titleLeftSpinBox.valueChanged.connect(self.updateTitleLeft)
        self.titleHeightSpinBox.valueChanged.connect(self.updateTitleHeight)
        self.paddingSpinBox.valueChanged.connect(self.updatePadding)

        self.titleTopSlider.setValue(3)
        self.titleLeftSlider.setValue(3)
        self.titleHeightSlider.setValue(6)
        self.paddingSlider.setValue(2)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        Dialog.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleTopLabel.setText(_translate("Dialog", "Title Top"))
        self.titleLeftLabel.setText(_translate("Dialog", "Title Left"))
        self.paddingLabel.setText(_translate("Dialog", "Padding"))
        self.titleHeightLabel.setText(_translate("Dialog", "Title Height"))
        self.FileLabel.setText(_translate("Dialog", "File"))

    def updateTitleTop(self, value):
        self.titleTopSlider.blockSignals(True)
        self.titleTopSpinBox.blockSignals(True)
        self.titleTopSlider.setValue(value)
        self.titleTopSpinBox.setValue(value)
        self.titleTopSlider.blockSignals(False)
        self.titleTopSpinBox.blockSignals(False)
        self.widget.setValues(self.titleTopSlider.value(), self.titleLeftSlider.value(), self.titleHeightSlider.value(), self.paddingSlider.value())

    def updateTitleLeft(self, value):
        self.titleLeftSlider.blockSignals(True)
        self.titleLeftSpinBox.blockSignals(True)
        self.titleLeftSlider.setValue(value)
        self.titleLeftSpinBox.setValue(value)
        self.titleLeftSlider.blockSignals(False)
        self.titleLeftSpinBox.blockSignals(False)
        self.widget.setValues(self.titleTopSlider.value(), self.titleLeftSlider.value(), self.titleHeightSlider.value(),
                              self.paddingSlider.value())

    def updateTitleHeight(self, value):
        self.titleHeightSlider.blockSignals(True)
        self.titleHeightSpinBox.blockSignals(True)
        self.titleHeightSlider.setValue(value)
        self.titleHeightSpinBox.setValue(value)
        self.titleHeightSlider.blockSignals(False)
        self.titleHeightSpinBox.blockSignals(False)
        self.widget.setValues(self.titleTopSlider.value(), self.titleLeftSlider.value(), self.titleHeightSlider.value(),
                              self.paddingSlider.value())

    def updatePadding(self, value):
        self.paddingSlider.blockSignals(True)
        self.paddingSpinBox.blockSignals(True)
        self.paddingSlider.setValue(value)
        self.paddingSpinBox.setValue(value)
        self.paddingSlider.blockSignals(False)
        self.paddingSpinBox.blockSignals(False)
        self.widget.setValues(self.titleTopSlider.value(), self.titleLeftSlider.value(), self.titleHeightSlider.value(),
                              self.paddingSlider.value())

    def getFile(self, index):
        path = ""
        while index.data() != None:
            path = index.data() + "/" + path
            index = index.parent()

        path = path.replace("//", "")
        if path[-1] == "/":
            path = path[:-1]

        path = path.replace("Windows (C:)", "C:")
        print(path)
        self.fileNameEntry.setText(path)

    def getText(self):
        return self.titleTopSlider.value(), self.titleLeftSlider.value(), self.titleHeightSlider.value(), \
               self.paddingSlider.value(), self.fileNameEntry.text()

    def returnNumber(self):
        return 5


class Ui_Form(QtWidgets.QDialog):
    def __init__(self, Dialog):
        super().__init__()
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 126)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dialoglabel = QtWidgets.QLabel(Dialog)
        self.dialoglabel.setObjectName("dialoglabel")
        self.horizontalLayout_3.addWidget(self.dialoglabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dialoglineedit = QtWidgets.QLineEdit(Dialog)
        self.dialoglineedit.setObjectName("dialoglineedit")
        self.horizontalLayout_2.addWidget(self.dialoglineedit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # connect the two functions
        self.pushButton.clicked.connect(Dialog.reject)
        self.pushButton_2.clicked.connect(Dialog.accept)

        Dialog.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dialoglabel.setText(_translate("Dialog", "dialoglabel"))
        self.pushButton_2.setText(_translate("Dialog", "Acept"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))

    def getText(self):
        return self.dialoglineedit.text()

    def returnNumber(self):
        return 1


class Dialog_Manager():
    def __init__(self, Dialog):
        print(0)
        QtWidgets.QDialog()
        print(1)
        self.dialog = QtWidgets.QDialog()
        self.ui = Dialog(self.dialog)
        self.text = None
        self.text_1 = None
        self.text_2 = None
        self.text_3 = None
        self.text_4 = None
        self.dialog.accepted.connect(self.getText)
        self.ok = self.dialog.exec()

    def getText(self):
        print(self.ui)
        print(self.ui.returnNumber())
        returnNumber = self.ui.returnNumber()
        if returnNumber == 1:
            self.text = self.ui.getText()
        elif returnNumber == 2:
            self.text, self.text_1 = self.ui.getText()
        elif returnNumber == 3:
            self.text, self.text_1, self.text_2 = self.ui.getText()
        elif returnNumber == 4:
            self.text, self.text_1, self.text_2, self.text_3 = self.ui.getText()
        elif returnNumber == 5:
            self.text, self.text_1, self.text_2, self.text_3, self.text_4 = self.ui.getText()

    def result(self):
        returnNumber = self.ui.returnNumber()
        if returnNumber == 0:
            return self.ok
        elif returnNumber == 1:
            return self.text, self.ok
        elif returnNumber == 2:
            return self.text, self.text_1, self.ok
        elif returnNumber == 3:
            return self.text, self.text_1, self.text_2, self.ok
        elif returnNumber == 4:
            return self.text, self.text_1, self.text_2, self.text_3, self.ok
        elif returnNumber == 5:
            return self.text, self.text_1, self.text_2, self.text_3, self.text_4, self.ok


class Test_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstbutton = QtWidgets.QPushButton(self.centralwidget)
        self.firstbutton.setObjectName("firstbutton")
        self.horizontalLayout.addWidget(self.firstbutton)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.firstbutton.clicked.connect(self.open_dialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "First column"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Second column"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "Third"))
        self.firstbutton.setText(_translate("MainWindow", "Add"))
        # self.secondbutton.setText(_translate("MainWindow", "Delete"))

    def open_dialog(self):
        file = open("text.txt", "w")
        top, left, height, padding, fileName, ok = Dialog_Manager(PowerPointSettingDialog).result()
        file.write(str(top)+ " " + str(left) + " " + str(height) + " " + str(padding) + " " + fileName)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Test_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
