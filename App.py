import sys
from PyQt5 import Qt
from model import ToDoModel
from view import MainWindow
from controller import Controller

class App(Qt.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = ToDoModel()
        self.main_ctrl = Controller(self.model)
        self.main_view = MainWindow(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())