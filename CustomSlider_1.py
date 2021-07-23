from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy
from PyQt5.QtGui import QPainter, QImage, qRgb, QPixmap, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint, QRect, QSize


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
    def __init__(self, colors=None, gaps=False, *args, **kwargs):
        super().__init__(colors, gaps, *args, **kwargs)
        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.Minimum
        )
        # self.setGeometry(300, 300, 300, 100)
        self.setMaximumHeight(100)
        self.radius = self.height()

        self.setSliderWidth(self.width())
        self.setSliderHeight(self.height() // 5)
        self.image_original = QPixmap("music player assets/others/progress_bar.png")
        self.image = self.image_original.scaled(self.sliderWidth, self.sliderHeight)

        self.marker_image_original = QPixmap("music player assets/others/marker_for_prog-bar_and_volume.png")
        self.marker_image = self.marker_image_original.scaled(min(self.width(), self.height()),
                                                              min(self.width(), self.height()))

        self.value = 0
        self.remaining = True
        self._background_color = QColor("gray")

    def sizeHint(self):
        return QSize(180, 60)

    def setBackgroundColor(self, color):
        self._background_color = color

    def setValue(self, value):
        if value >= 100:
            value = 100
        if value <= 0:
            value = 0
        self.value = value

    def setSliderWidth(self, width):
        self.sliderWidth = width

    def setSliderHeight(self, height):
        self.sliderHeight = height

    def setRadius(self, radius):
        self.radius = radius

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = event.rect()
        rect_source = event.rect()

        rect.setTop(self.height() / 2 - self.sliderHeight / 2)
        rect.setHeight(self.height())

        self.image = self.image_original.scaled(self.sliderWidth, self.sliderHeight)
        self.marker_image = self.marker_image_original.scaled(self.radius, self.radius)
        painter.drawPixmap(rect, self.image, rect_source)

        # Hiding remaining part
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(self._background_color)
        if self.remaining:
            rect = QRect(self.value / 100 * self.width() - self.radius / 2,
                         self.height() / 2 - self.sliderHeight / 2,
                         self.width() - (self.value / 100 * self.width() - self.radius / 2),
                         self.sliderHeight)
            painter.fillRect(rect, brush)

        # Draw Marker
        painter.drawPixmap(QRect(self.value / 100 * self.width() - self.radius / 2,
                                 self.height() / 2 - self.marker_image.height() / 2,
                                 self.width(), self.height()),
                           self.marker_image, rect_source)

        painter.end()

    def resizeEvent(self, event):
        # ウィンドウの大きさがもとの大きさより大きくなったら動くよ
        print("height", self.height())

        self.setSliderWidth(self.width())
        # self.setRadius(self.height())
        self.update()

    def mousePressEvent(self, e):
        print(e.x())
        self.setValue(e.x() / self.width() * 100)
        print(self.value)
        self.update()

    def mouseMoveEvent(self, e):
        print(e.x())
        self.setValue(e.x() / self.width() * 100)
        print(self.value)
        self.update()

    def hideRemaining(self, enable):
        self.remaining = enable

    # def setValue(self, value):
    #     if value > self.max:
    #         self.value = self.max
    #     elif value < self.min:
    #         self.value = self.min
    #     else:
    #         self.value = value
    #
    #     if self.max == 0:
    #         self.draw_steps = 0
    #     elif self.value == self.max:
    #         self.draw_steps = self.nSteps
    #     elif self.value == self.min:
    #         self.draw_steps = 0
    #     else:
    #         self.draw_steps = int(self.nSteps * (self.value - self.min) / (self.max - self.min)) + 1
    #     self.update()

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
    # volume.setBackgroundColor('gray')
    volume.setSliderHeight(5)
    volume.setRadius(15)
    volume.setValue(120)

    # Connect clickedValue Signal to set value function and now you can interact bar with mouse
    # volume.clickedValue.connect(lambda pc: volume.setValue(pc*volume.maxLimit()))
    volume.show()
    app.exec_()
