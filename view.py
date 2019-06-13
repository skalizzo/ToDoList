from PyQt5 import QtWidgets
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(exitAct)

        self.setGeometry(600, 600, 600, 400)
        self.setWindowTitle('ToDo List')
        self.show()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     mainwindow = MainWindow()
#     sys.exit(app.exec_())