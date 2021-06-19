import sys

from PyQt5.QtWidgets import QApplication

from view.window import OsuLoaderWindow


def main():
    print("Starting osu!Loader 2.0")
    app = QApplication(sys.argv)
    window = OsuLoaderWindow.OsuLoaderWindow()
    app.exec_()
    pass


if __name__ == "__main__":
    main()
