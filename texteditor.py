from mainui import UiMainWindow
from PyQt5 import QtWidgets
import sys


def main():
    # -----------
    # Entry point
    # -----------
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow(main_window)
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # ------------------------- #
    # Only if start this script #
    # ------------------------- #
    main()
