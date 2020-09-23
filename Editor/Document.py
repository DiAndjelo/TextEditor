from PyQt5.Qsci import QsciScintilla


class Document(QsciScintilla):
    def __init__(self):
        super().__init__()
        self.languageToLexer = {
            None: None,
        }
        self.languageToFile = {
            None: "Text Files (*.txt);;All Files (*)",
        }
        self.filePath = "Untitled"
        self.currentLanguage = None
        self.setMargins(1)
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setUtf8(True)
        self.setIndentationsUseTabs(False)
        self.setTabWidth(4)
        self.setIndentationGuides(False)
        self.setAutoIndent(True)
        self.setScrollWidth(1)
        self.setScrollWidthTracking(True)

    def get_file_type(self):
        return self.languageToFile.get(self.currentLanguage)

    def change_lexer(self, lexer):
        new_lexer = lexer
        self.setLexer(new_lexer)
        self.currentLanguage = lexer

    def change_margin_width(self):
        num_lines = self.lines()
        self.setMarginWidth(0, "00" * len(str(num_lines)))

    def update_font(self, new_font):
        if self.currentLanguage is not None:
            self.lexer().setFont(new_font)
        else:
            self.setFont(new_font)
