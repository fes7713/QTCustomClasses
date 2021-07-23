from PyQt5 import QtCore

class Filter(QtCore.QObject):
    left = QtCore.pyqtSignal()
    focusOut = QtCore.pyqtSignal()
    doubleClicked = QtCore.pyqtSignal()
    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.FocusOut:
            print('focus out')
            self.focusOut.emit()
        if event.type() == QtCore.QEvent.Leave:
            print("leave")
            self.left.emit()
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("double")
            self.doubleClicked.emit()
        return False