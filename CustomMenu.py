from PyQt5.QtWidgets import QMenu
from PyQt5 import QtWidgets, QtGui, QtCore

# Custom Menu requires list of tuples that contains title name in string and action funciton
# When pass_argvs is turned on target and position information that is passed to Custom Menu
# will be directly passed to actions in tuples
# See Example for details
class CustomMenu(QMenu):
    def __init__(self, actions, target=None, pos=None, pass_args=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target = target
        self.pos = pos

        self.init(self, actions, pass_args)
        if target and pos:
            self.exec_(target.mapToGlobal(pos))

    def init(self, parent, actions, pass_args):
        for action in actions:
            title, func = action
            if not isinstance(title, str):
                raise TypeError("Action title must be String")
            if isinstance(func, list):
                subMenu = parent.addMenu(title)
                self.init(subMenu, func, pass_args)

            else:
                if title == "separator":
                    parent.addSeparator()
                    continue
                action_added = parent.addAction(title)
                if pass_args:
                    self.connectAction(action_added, func, self.target, self.pos)
                else:
                    action_added.triggered.connect(func)

    def connectAction(self, parent, func, target, pos):
        parent.triggered.connect(lambda: func(target, pos))

# class CustomMenu(QMenu):
#     def __init__(self, actions, target=None, pos=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.init(self, actions)
#         if target and pos:
#             self.exec_(target.mapToGlobal(pos))
#
#     def init(self, parent, actions):
#         for action in actions:
#             title, func = action
#             if isinstance(func, list):
#                 subMenu = parent.addMenu(title)
#                 self.init(subMenu, func)
#
#             else:
#                 if title == "separator":
#                     parent.addSeparator()
#                     continue
#                 action_added = parent.addAction(title)
#                 action_added.triggered.connect(func)

#################################3
# test
class UISample(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(UISample, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        # カスタムUIを作成
        self.list = QtWidgets.QTreeView()
        layout.addWidget(self.list)
        self.list2 = QtWidgets.QTreeView()
        # List1で表示するContextMenuを設定
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list.customContextMenuRequested.connect(self.listContext)
        # List2で表示するContextMenuを指定
        self.list2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list2.customContextMenuRequested.connect(self.list2Context)
        self.model = QtGui.QStandardItemModel()
        self.model_item = QtGui.QStandardItem("Hello")
        self.model.appendRow(self.model_item)
        self.list.setModel(self.model)
        layout.addWidget(self.list2)
        # ここまでUI作成

        self.setLayout(layout)

    def listContext(self, pos):
        actions = [("Yo Yo", [("What", self.printYu), ("separator", "separator"), ("What", self.printHello)]),
                   ("Yo Yo", self.printHello),
                   ("Yo Yo", self.printYu), ("Yo Yo", self.printYu), ]
        menu = CustomMenu(actions)
        action_01 = menu.addAction('ほげほげ')
        action_01.triggered.connect(lambda: self.action('A'))
        action_02 = menu.addAction('ふがふが')
        action_02.triggered.connect(lambda: self.action('B'))
        # print(self.list.indexAt(pos).data())
        menu.addSeparator()
        subMenu = menu.addMenu('SubMenu')
        action_03 = subMenu.addAction('さぶめにゅー1')
        action_03.triggered.connect(self.subMenu)

        menu.exec_(self.list.mapToGlobal(pos))

    def action(self, actionText):
        print(actionText)

    def subMenu(self):
        print("SUBMENU")

    def list2Context(self, pos):

        menu = QtWidgets.QMenu(self.list2)
        menu.addAction('list2_Menu')
        menu.addAction('list2_Menu2')
        menu.addAction('list2_Menu2')

        menu.exec_(self.list2.mapToGlobal(pos))

    def printHello(self):
        print("Hello")

    def printYu(self):
        print("Yu")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a = UISample()
    a.show()
    sys.exit(app.exec_())
