import mysql.connector as MySQL
from mysql.connector import Error as MySQLException

MYSQL = {}
MYSQL["host"] = "127.0.0.1"
MYSQL["port"] = 3306
MYSQL["user"] = "root"
MYSQL["passwd"] = ""
MYSQL["database"] = "searchrecordweb"

class Connect:

    def __init__(self):
        self.__instance = None
        self.__error = None
    
    def getInstance(self,data:dict):
        specific = self.specific(data)
        try:
            if self.__instance == None:
                self.__instance = MySQL.connect(
                    host=specific["host"],
                    port=specific["port"],
                    user=specific["user"],
                    passwd=specific["passwd"],
                    database=specific["database"],
                )
            if not self.__instance.is_connected():
                raise MySQLException("Não foi possivel conectar ao destino")
        except MySQLException as error:
            self.__error = error
        return self.__instance

    @staticmethod
    def specific(data:dict) -> dict:
        for arg in data:
            if data[arg] == None:
                data[arg] = MYSQL[arg]
        return data

    def getError(self):
        return self.__error
