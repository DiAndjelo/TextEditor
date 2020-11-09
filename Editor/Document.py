from PyQt5.Qsci import QsciScintilla
from PyQt5.QtWidgets import QTextEdit


class Document(QTextEdit):
    def __init__(self, parent, index):
        super().__init__()
        self.parent = parent
        self.index = index
        self.filePath = "Untitled"
        self.textChanged.connect(self.text_changed)
        self.is_changed = False

    def text_changed(self):
        current_tab_text = self.parent.tabText(self.parent.currentIndex())
        if not self.is_changed:
            self.parent.setTabText(self.parent.currentIndex(), current_tab_text+' *')
            self.is_changed = True

    def remove_is_changed(self):
        self.is_changed = False

    def remove_is_changed_for_save(self):
        self.is_changed = False
        current_tab_text = self.parent.tabText(self.parent.currentIndex())
        print(current_tab_text[:-1])
        if '*' in current_tab_text[:-1]:
            self.parent.setTabText(self.parent.currentIndex(), current_tab_text[:-1])
