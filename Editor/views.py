from PyQt5 import QtWidgets


class Editor(QtWidgets.QWidget):
    """
    Main Editor class

    """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent


class PageControl(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class Document(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class TextBox(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()


class List(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
