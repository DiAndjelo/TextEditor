from PyQt5 import QtWidgets
from Editor import Editor
import sys


def main():
    # ----------- #
    # Entry point #
    # ----------- #
    app = QtWidgets.QApplication(sys.argv)
    Editor.Editor()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # ----------------------------------- #
    # Only if start this script start app #
    # ----------------------------------- #
    main()
