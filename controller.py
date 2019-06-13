"""Controller für ToDoList App"""

class Controller():
    def __init__(self, model):
        self.model = model
        self.createDB()

    def createDB(self):
        self.model.executeSql(self.model.getSqlCreateDB())

