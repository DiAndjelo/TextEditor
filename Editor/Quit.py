from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class Quit(QDialog):
    def __init__(self, parent=None):
        super(Quit, self).__init__(parent)
        self.setWindowTitle('Quit')
        self.setWindowIcon(QIcon("static/help.png"))
        self.resize(300, 200)
        title = QLabel('TextEditor\n\nBy:\n')
        title.setAlignment(Qt.AlignCenter)
        author = QLabel('DiAndjelo')
        author.setAlignment(Qt.AlignCenter)
        github = QLabel('<a href="https://github.com/DiAndjelo/TextEditor/">GitHub</a>')
        github.setOpenExternalLinks(True)
        github.setAlignment(Qt.AlignCenter)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignVCenter)
        self.layout.addWidget(title)
        self.layout.addWidget(author)
        self.layout.addWidget(github)
        self.setLayout(self.layout)
