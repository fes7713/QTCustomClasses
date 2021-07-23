import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy
from PyQt5.QtGui import QPainter, QImage, qRgb, QPixmap, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint, QRect, QSize


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
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


if __name__ == '__main__':
    # 動け～
    app = QApplication(sys.argv)
    ex = Canvas()
    ex.setSliderHeight(5)
    ex.setRadius(15)
    ex.show()
    sys.exit(app.exec_())
