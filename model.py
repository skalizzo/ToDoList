"""datamodel for ToDoList App"""
import sqlite3

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ToDoModel(metaclass=Singleton):
    def __init__(self):
        self.dbpfad = 'DB/todo.db'

    def getConn(self):
        conn = sqlite3.connect(self.dbpfad)
        return conn

    def executeSql(self, sqlCommands:list):
        conn = self.getConn()
        try:
            for sql in sqlCommands:
                c = conn.cursor()
                c.execute(sql)
            conn.commit()
        except:
            print('DB_executeSql Fehler')
            print(sqlCommands)
        finally:
            conn.close()

    def getSqlCreateDB(self):
        sql_ToDo = """CREATE TABLE IF NOT EXISTS ToDoItems (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Prio INTEGER,
                        Titel VARCHAR(100),
                        ToDo VARCHAR(100),
                        Termin DATE,
                        Auftraggeber_ID INTEGER, 
                        Bemerkungen VARCHAR(500),
                        Bemerkungen_WS VARCHAR(500),
                        Erledigt_am DATE);"""

        sql_User = """CREATE TABLE IF NOT EXISTS ToDoUser (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Name VARCHAR(100),
                                Mail VARCHAR(100),
                                Type VARCHAR(20));"""
        return [sql_ToDo, sql_User]


    def addEntry(self):
        pass

    def modifyEntry(self, ID):
        pass

    def deleteEntry(self, ID):
        pass

    def getToDos(self):
        pass

    def getToDoByID(self, ID):
        pass



