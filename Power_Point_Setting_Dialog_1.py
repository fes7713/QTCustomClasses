# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Power_Point_Setting_Dialog_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1085, 701)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(Dialog)
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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleTopLabel.setText(_translate("Dialog", "Title Top"))
        self.titleLeftLabel.setText(_translate("Dialog", "Title Left"))
        self.paddingLabel.setText(_translate("Dialog", "Padding"))
        self.titleHeightLabel.setText(_translate("Dialog", "Title Height"))
        self.FileLabel.setText(_translate("Dialog", "File"))