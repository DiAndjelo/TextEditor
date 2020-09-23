from PyQt5.QtWidgets import QApplication, QTabWidget
from .Document import Document


class PageControl(QTabWidget):
    """
    PageControl class
    """
    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

    def open_tab(self):
        text_widget = Document()
        if self.count() == 0:
            self.addTab(text_widget, "Untitled")
        else:
            self.addTab(text_widget, "Untitled ({})".format(self.count() + 1))
        self.setCurrentIndex(self.count() - 1)

    def close_tab(self, index):
        self.removeTab(index)
        if self.count() == 0:
            QApplication.quit()
