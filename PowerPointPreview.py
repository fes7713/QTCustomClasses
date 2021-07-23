from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QColor, QIcon

class Preview(QtWidgets.QWidget):
    def __init__(self, titleTop, titleLeft, titleHeight, padding,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.titleTop = titleTop
        self.titleLeft = titleLeft
        self.padding = padding
        self.titleHeight = titleHeight
        self._background_color = QtGui.QColor('grey')
        self.itemColor = QtGui.QColor('cyan')
        self.titleColor = QtGui.QColor('yellow')

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        width = self.size().width()
        height = self.size().height()

        titleTop_pix = int(self.titleTop * height /100)
        titleLeft_pix = int(self.titleLeft * width / 100)
        titleHeight_pix = int(self.titleHeight * height /100)
        padding_pix = int(self.padding * width / 100)


        rect = QtCore.QRect(titleLeft_pix,
                            titleTop_pix,
                            painter.device().width() - titleLeft_pix * 2,
                            titleHeight_pix)

        brush.setColor(self.titleColor)
        painter.fillRect(rect, brush)
        brush.setColor(self.itemColor)

        d_height = height - titleTop_pix - titleHeight_pix
        d_width = width
        item_height = d_height / 3
        item_width = width / 2


        for i in range(6):
            rect = QtCore.QRect(padding_pix + (i % 2) * item_width,
                                titleTop_pix + titleHeight_pix + (i // 2) * item_height + padding_pix,
                                item_width - padding_pix * 2,
                                item_height - padding_pix * 2)
            painter.fillRect(rect, brush)

        painter.end()


    def setValues(self, titleTop, titleLeft, titleHeight, padding):
        self.titleTop = titleTop
        self.titleLeft = titleLeft
        self.padding = padding
        self.titleHeight = titleHeight
        self.update()
