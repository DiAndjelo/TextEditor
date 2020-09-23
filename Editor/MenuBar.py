from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QMenuBar


class MenuBar(QMenuBar):
    """
    MenuBar Class
    """
    new_file = pyqtSignal()
    open_file = pyqtSignal()
    save_file = pyqtSignal()
    save_file_as = pyqtSignal()
    undo_edit = pyqtSignal()
    redo_edit = pyqtSignal()
    cut_text = pyqtSignal()
    copy_text = pyqtSignal()
    paste_text = pyqtSignal()
    change_font = pyqtSignal()
    change_language = pyqtSignal(str)
    open_about_dialog = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.fileMenu = None
        self.editMenu = None
        self.settingsMenu = None
        self.helpMenu = None
        self.change_file_menu()
        self.create_edit_menu()
        self.create_settings_menu()
        self.create_help_menu()

    def change_file_menu(self):
        # New File
        new_file_action = QAction(QIcon("static/new.png"), 'New File', self)
        new_file_action.setShortcut("Ctrl+N")
        new_file_action.setStatusTip("New file")
        new_file_action.triggered.connect(lambda: self.new_file.emit())
        # Open File
        open_file_action = QAction(QIcon("static/open.png"), 'Open File', self)
        open_file_action.setShortcut("Ctrl+O")
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(lambda: self.open_file.emit())
        # Save File
        save_file_action = QAction(QIcon("static/save.png"), 'Save File', self)
        save_file_action.setShortcut("Ctrl+S")
        save_file_action.setStatusTip("Save file")
        save_file_action.triggered.connect(lambda: self.save_file.emit())
        # Save File As
        save_file_as_action = QAction(QIcon("static/save.png"), 'Save File As', self)
        save_file_as_action.setShortcut("Ctrl+Shift+S")
        save_file_as_action.setStatusTip("Save file as")
        save_file_as_action.triggered.connect(lambda: self.save_file_as.emit())
        # Quit
        quit_action = QAction(QIcon("static/quit.png"), 'Quit', self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.setStatusTip("Quit EasyEdit")
        quit_action.triggered.connect(lambda: QApplication.quit())
        # Adding actions to file menu
        self.fileMenu = self.addMenu("File")
        self.fileMenu.addAction(new_file_action)
        self.fileMenu.addAction(open_file_action)
        self.fileMenu.addAction(save_file_action)
        self.fileMenu.addAction(save_file_as_action)
        self.fileMenu.addAction(quit_action)

    def create_edit_menu(self):
        # Undo
        undo_edit_action = QAction(QIcon("static/undo.png"), "Undo", self)
        undo_edit_action.setStatusTip("Undo last edit")
        undo_edit_action.setShortcut("Ctrl+Z")
        undo_edit_action.triggered.connect(lambda: self.undo_edit.emit())
        # Redo
        redo_edit_action = QAction(QIcon("static/redo.png"), "Redo", self)
        redo_edit_action.setStatusTip("Redo last edit")
        redo_edit_action.setShortcut("Ctrl+Shift+Z")
        redo_edit_action.triggered.connect(lambda: self.redo_edit.emit())
        # Cut
        cut_text_action = QAction(QIcon("static/cut.png"), "Cut Selection", self)
        cut_text_action.setStatusTip("Cut text to clipboard")
        cut_text_action.setShortcut("Ctrl+X")
        cut_text_action.triggered.connect(lambda: self.cut_text.emit())
        # Copy
        copy_text_action = QAction(QIcon("static/copy.png"), "Copy Selection", self)
        copy_text_action.setStatusTip("Copy text to clipboard")
        copy_text_action.setShortcut("Ctrl+C")
        copy_text_action.triggered.connect(lambda: self.copy_text.emit())
        # Paste
        paste_text_action = QAction(QIcon("static/paste.png"), "Paste", self)
        paste_text_action.setStatusTip("Paste text from clipboard")
        paste_text_action.setShortcut("Ctrl+V")
        paste_text_action.triggered.connect(lambda: self.paste_text.emit())
        # Adding actions to create menu
        self.editMenu = self.addMenu("Edit")
        self.editMenu.addAction(undo_edit_action)
        self.editMenu.addAction(redo_edit_action)
        self.editMenu.addAction(cut_text_action)
        self.editMenu.addAction(copy_text_action)
        self.editMenu.addAction(paste_text_action)

    def create_settings_menu(self):
        change_font_action = QAction(QIcon("static/font.png"), "Change Font", self)
        change_font_action.setStatusTip("Change font")
        change_font_action.triggered.connect(lambda: self.change_font.emit())
        self.settingsMenu = self.addMenu("Settings")
        self.settingsMenu.addAction(change_font_action)

    def create_help_menu(self):
        about_dialog_action = QAction(QIcon("static/about.png"), 'About', self)
        about_dialog_action.setStatusTip('About the application.')
        about_dialog_action.setShortcut('CTRL+H')
        about_dialog_action.triggered.connect(lambda: self.open_about_dialog.emit())
        self.helpMenu = self.addMenu("Help")
        self.helpMenu.addAction(about_dialog_action)
