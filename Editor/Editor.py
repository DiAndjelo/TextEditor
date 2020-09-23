from os.path import split
from PyQt5.QtCore import QSettings, QPoint, QSize, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QFontDialog, QMainWindow
from .About import About
from .MenuBar import MenuBar
from .PageControl import PageControl


class Editor(QMainWindow):
    """
    Main Editor Class
    """
    def __init__(self):
        super().__init__()
        self.fileToLanguage = {
            '': None,
            'txt': None,
        }
        self.read_window_settings()
        self.about = About()
        self.menuBar = MenuBar()
        self.setMenuBar(self.menuBar)
        self.page_control = PageControl()
        self.read_page_control_settings()
        self.setCentralWidget(self.page_control)
        self.change_font(self.font())
        self.statusBar = self.statusBar()
        self.configure_signals()
        self.show()

    def read_window_settings(self):
        settings = QSettings("DiAndjelo", "TextEditor")
        settings.beginGroup("Editor")
        self.setWindowIcon(QIcon("static/editor.png"))
        self.resize(settings.value("size", QSize(600, 800)))
        self.move(settings.value("pos", QPoint(0, 0)))
        self.setFont(settings.value("font", self.font()))
        settings.endGroup()

    def write_window_settings(self):
        settings = QSettings("DiAndjelo", "TextEditor")
        settings.beginGroup("Editor")
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())
        settings.setValue("font", self.font())
        settings.endGroup()

    def read_page_control_settings(self):
        settings = QSettings("DiAndjelo", "TextEditor")
        settings.beginGroup("Tab Bar")
        saved_tabs = settings.value("openedTabs")
        tab_lexers = settings.value("tab_lexers")
        if saved_tabs is None or saved_tabs[0] == "Untitled":
            self.page_control.open_tab()
        else:
            for i in range(len(saved_tabs)):
                if saved_tabs[i] != "Untitled":
                    self.page_control.open_tab()
                    self.open_file(saved_tabs[i])
                    self.page_control.widget(i).change_lexer(tab_lexers[i])
        self.page_control.setCurrentIndex(int(settings.value("currentTab", 0)))
        self.update_window_title()
        settings.endGroup()

    def write_tab_bar_settings(self):
        open_tabs = []
        tab_lexers = []
        for i in range(self.page_control.count()):
            open_tabs.append(self.page_control.widget(i).filePath)
            tab_lexers.append(self.page_control.widget(i).currentLanguage)
        settings = QSettings("DiAndjelo", "TextEditor")
        settings.beginGroup("Tab Bar")
        settings.setValue("openedTabs", open_tabs)
        settings.setValue("tab_lexers", tab_lexers)
        settings.setValue("currentTab", self.page_control.currentIndex())
        settings.endGroup()

    def close_event(self, event):
        self.write_tab_bar_settings()
        self.write_window_settings()
        while self.page_control.count() > 0:
            self.page_control.close_tab(0)

    def configure_signals(self):
        # FILE TAB
        self.menuBar.new_file.connect(self.page_control.open_tab)
        self.menuBar.open_file.connect(self.open_file_dialog)
        self.menuBar.save_file.connect(self.save_file)
        self.menuBar.save_file_as.connect(self.save_file_as)
        # EDIT TAB
        self.menuBar.undo_edit.connect(self.page_control.currentWidget().undo)
        self.menuBar.redo_edit.connect(self.page_control.currentWidget().redo)
        self.menuBar.cut_text.connect(self.page_control.currentWidget().cut)
        self.menuBar.copy_text.connect(self.page_control.currentWidget().copy)
        self.menuBar.paste_text.connect(self.page_control.currentWidget().paste)
        # SETTINGS TAB
        self.menuBar.change_font.connect(self.change_font_dialog)
        # HELP TAB
        self.menuBar.open_about_dialog.connect(lambda: self.about.exec_())
        # TAB BAR
        self.page_control.currentChanged.connect(self.tab_changed)
        # TEXT AREA
        self.menuBar.change_language.connect(self.change_language)

    def change_language(self, language):
        self.page_control.currentWidget().change_lexer(language)
        self.change_font(self.font())

    def change_font(self, new_font):
        self.setFont(new_font)
        for i in range(self.page_control.count()):
            self.page_control.widget(i).update_font(new_font)

    def change_font_dialog(self):
        font = QFontDialog().getFont()[0]
        self.change_font(font)

    def open_file(self, file_name):
        with open(file_name, 'r') as file:
            self.page_control.currentWidget().setText(file.read())
        shortened_file_name = split(file_name)[1]
        extension = shortened_file_name.split('.')
        if len(extension) == 2:
            language = self.fileToLanguage.get(extension[1])
            self.change_language(language)
        else:
            self.change_language(None)
        self.page_control.currentWidget().filePath = file_name
        self.page_control.setTabText(self.page_control.currentIndex(), shortened_file_name)
        self.page_control.currentWidget().change_margin_width()
        self.update_window_title()

    def open_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File")[0]
        if file_name != "":
            self.open_file(file_name)

    def save_file(self):
        if self.page_control.currentWidget().filePath != "Untitled":
            file_name = self.page_control.currentWidget().filePath
            if file_name != "":
                text = self.page_control.currentWidget().text()
                with open(file_name, 'w') as file:
                    file.write(text)
            self.change_font(self.font())
        else:
            self.save_file_as()

    def save_file_as(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", None, self.page_control.currentWidget().get_file_type())[0]
        if file_name != "":
            shortened_file_name = split(file_name)[1]
            self.page_control.setTabText(self.page_control.currentIndex(), shortened_file_name)
            self.update_window_title()
            text = self.page_control.currentWidget().text()
            with open(file_name, 'w') as file:
                file.write(text)
        self.change_font(self.font())

    def tab_changed(self):
        if self.page_control.count() > 1:
            self.update_window_title()

    def update_window_title(self):
        self.setWindowTitle(self.page_control.tabText(self.page_control.currentIndex()) + " - TextEditor")

    @pyqtSlot(int, int)
    def update_status_bar_text(self, line, column):
        self.statusBar.showMessage("Line {}, Column {}".format(line, column))
