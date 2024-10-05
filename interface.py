from main_window import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('window_icon.ico'))
    window = Questionnaire()
    window.show()
    sys.exit(app.exec_())