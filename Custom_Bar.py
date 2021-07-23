from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Multi_Bar(QtWidgets.QWidget):
    clickedValue = QtCore.pyqtSignal(str)

    def __init__(self, colors=None, gaps=False, vertical=False, drag=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('grey')
        self.nSteps = None
        self.padding = 5
        self.colors = []
        self.gaps = gaps
        self.vertical = vertical
        self.drag = drag
        if not colors:
            return

        self.nSteps = len(colors)
        self.colors = colors
        self.draw_steps = self.nSteps

    def sizeHint(self):
        return QtCore.QSize(180, 80)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)
        if self.colors:
            width = self.size().width()
            height = self.size().height()
            d_width = width - self.padding * 2
            d_height = height - self.padding * 2

            # Gaps between bars
            if self.vertical:
                step_size = d_height / self.nSteps

                for i in range(self.draw_steps):
                    brush.setColor(QColor(self.colors[i]))
                    rect = QtCore.QRect(self.padding,
                                        d_height - step_size * i + self.padding - step_size,
                                        d_width,
                                        step_size + 1)
                    painter.fillRect(rect, brush)
            else:
                if not self.gaps:
                    step_size = d_width / self.nSteps

                    for i in range(self.draw_steps):
                        brush.setColor(QColor(self.colors[i]))
                        rect = QtCore.QRect(self.padding + step_size * i - 1,
                                            self.padding,
                                            step_size + 1,
                                            d_height)
                        painter.fillRect(rect, brush)

                else:
                    step_size = d_width / self.nSteps

                    for i in range(self.draw_steps):
                        brush.setColor(QColor(self.colors[i]))
                        rect = QtCore.QRect(self.padding * 2 + step_size * i,
                                            self.padding,
                                            step_size - self.padding,
                                            d_height)
                        painter.fillRect(rect, brush)
        painter.end()

    def indexAt(self, pos, length):
        if not self.colors:
            return
        d_length = length - (self.padding * 2)
        step_size = d_length / self.nSteps
        click_x = pos
        index = int((click_x - self.padding) / step_size)
        return index

    def mouseMoveEvent(self, e):
        if not self.drag:
            return
        if self.vertical:
            index = self.indexAt(-1 * e.y() + self.size().height(), self.size().height())
        else:
            index = self.indexAt(e.x(), self.size().width())
        if index >= self.nSteps:
            index = self.nSteps - 1
        color = self.colors[index]
        self.clickedValue.emit(color)

    def mousePressEvent(self, e):
        if not self.drag:
            return
        if self.vertical:
            index = self.indexAt(-1 * e.y() + self.size().height(), self.size().height())
        else:
            index = self.indexAt(e.x(), self.size().width())
        if index >= self.nSteps:
            index = self.nSteps - 1
        color = self.colors[index]
        self.clickedValue.emit(color)

    def setColors(self, colors):
        self.nSteps = len(colors)
        self.colors = colors
        self.update()

    def setBarPadding(self, i):
        self.padding = int(i)
        self.update()

    def setBarSolidPercent(self, f):
        self._bar_solid_percent = float(f)
        self.update()

    def setBackgroundColor(self, color):
        self._background_color = QtGui.QColor(color)
        self.update()


class Progress_Bar(Multi_Bar):
    clickedValue = QtCore.pyqtSignal(float)

    def __init__(self, colors=None, gaps=False, *args, **kwargs):
        super().__init__(colors, gaps, *args, **kwargs)
        self.value = 0
        self.max = 100
        self.min = 0
        self.draw_steps = int(self.nSteps * (self.value - self.min) / (self.max - self.min))

    def mouseMoveEvent(self, e):
        if self.vertical:
            d_length = self.size().height() - (self.padding * 2)
            click_x = -1 * e.y() + self.size().height()
            pc = (click_x - self.padding) / d_length
            if pc > 1:
                pc = 1
            elif pc < 0:
                pc = 0
            print(pc)
            self.clickedValue.emit(pc)
        else:
            d_length = self.size().width() - (self.padding * 2)
            click_x = e.x()
            pc = (click_x - self.padding) / d_length

            if pc > 1:
                pc = 1
            elif pc < 0:
                pc = 0
            print(pc)
            self.clickedValue.emit(pc)

        # if not self.drag:
        #     return
        # if self.vertical:
        #     index = self.indexAt(-1 * e.y() + self.size().height(), self.size().height()) + 1
        # else:
        #     index = self.indexAt(e.x(), self.size().width()) + 1
        # if index > self.nSteps:
        #     index = self.nSteps
        # self.draw_steps = index
        # self.update()

    def mousePressEvent(self, e):
        if self.vertical:
            d_length = self.size().height() - (self.padding * 2)
            click_x = -1 * e.y() + self.size().height()
            pc = (click_x - self.padding) / d_length
            if pc > 1:
                pc = 1
            elif pc < 0:
                pc = 0
            print(pc)
            self.clickedValue.emit(pc)
        else:
            d_length = self.size().width() - (self.padding * 2)
            click_x = e.x()
            pc = (click_x - self.padding) / d_length

            if pc > 1:
                pc = 1
            elif pc < 0:
                pc = 0
            print(pc)
            self.clickedValue.emit(pc)

    def setValue(self, value):
        if value > self.max:
            self.value = self.max
        elif value < self.min:
            self.value = self.min
        else:
            self.value = value

        if self.max == 0:
            self.draw_steps = 0
        elif self.value == self.max:
            self.draw_steps = self.nSteps
        elif self.value == self.min:
            self.draw_steps = 0
        else:
            self.draw_steps = int(self.nSteps * (self.value - self.min) / (self.max - self.min)) + 1
        self.update()

    def setLimit(self, nMax, nMin):
        if nMax <= nMin:
            if nMax != 0:
                raise TypeError("maximun value must be bigger than minimum value")
        self.max = nMax
        self.min = nMin

    def enableDrag(self):
        self.drag = True

    def disableDrag(self):
        self.drag = False

    def maxLimit(self):
        return self.max


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    volume = Progress_Bar(
        colors=["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43",
                "#d53e4f", "#9e0142"],
        gaps=True,
        vertical=False)

    volume.setBarPadding(3)
    volume.setBarSolidPercent(0.9)
    volume.setBackgroundColor('gray')
    volume.setValue(120)

    # Connect clickedValue Signal to set value function and now you can interact bar with mouse
    volume.clickedValue.connect(lambda pc: volume.setValue(pc*volume.maxLimit()))
    volume.show()
    app.exec_()
