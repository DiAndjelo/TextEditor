import re

from PyQt5.QtWidgets import QTabWidget, QMessageBox
from .Document import Document


class PageControl(QTabWidget):
    """
    Page Control class
    """
    def __init__(self, parent):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.parent = parent
        self.tabCloseRequested.connect(self.close_tab)

    def open_tab(self):
        text_widget = Document()
        if self.count() == 0:
            self.addTab(text_widget, "Untitled")
        else:
            self.addTab(text_widget, "Untitled ({})".format(self.count() + 1))
        self.setCurrentIndex(self.count() - 1)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)
        if reply == QMessageBox.Close:
            event.accept()
        else:
            event.ignore()

    def close_tab(self, index):
        pattern = re.compile('Untitled')
        res = pattern.findall(self.tabText(index))
        if res:
            self.removeTab(index)
        else:
            reply = QMessageBox.question(
                self, "Message",
                "Are you sure you want to quit? Any unsaved work will be lost.",
                QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
                QMessageBox.Save)
            if reply == QMessageBox.Close:
                self.removeTab(index)
                # if self.count() == 0:
                #     QApplication.quit()
            elif reply == QMessageBox.Save:
                self.parent.save_file()
                self.removeTab(index)
                # if self.count() == 0:
                #     QApplication.quit()


"""
Звездочка если изменено.
Диалог только для не сохраненных файлов.
"""