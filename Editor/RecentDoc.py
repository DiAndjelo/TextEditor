import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QAction, QWidget


class RecentDoc(QWidget):
    """
    Recent Docs class
    """
    # open_recent_file = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.actions = {}
        self.recent_docs = []
        self.recent_actions = []

    @staticmethod
    def open_recent():
        result = []
        with open("data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                result.append(line[:-1])
        return result

    def update_recent(self, checker=False):
        if checker:
            for _ in self.parent.recent_docs_menu.actions():
                self.parent.recent_docs_menu.removeAction(_)
        self.recent_docs = self.open_recent()
        count = 0
        for recent_doc in reversed(self.recent_docs):
            self.actions[f'{count}'] = QAction("{}".format(os.path.basename(recent_doc)), self)
            self.actions[f'{count}'].triggered.connect(lambda: self.parent.open_recent_file.emit(recent_doc))
            self.recent_actions.append(self.actions[f'{count}'])
            count += 1
        self.parent.recent_docs_menu.addActions(self.recent_actions)
        self.recent_actions = []
