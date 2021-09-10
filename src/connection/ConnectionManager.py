#  import mysql.connector

class ConnectionManager():
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

        self.connection = self.__startConnection()
    
    def __startConnection(self):
        databaseConnector = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        connection = databaseConnector.cursor()

        return connection

    def executeSelect(self, table, columnsToSelect=["*"], conditions=""):
        sql = "select"

        for column in columnsToSelect:
            sql += " " + column + ", "

        sql = sql.strip()

        if sql[-1] == ",":
            sql = sql[:-1]

        sql += " from " + table

        if conditions != "":
            sql += " where " + conditions

        self.connection.execute(sql)

        result = self.connection.fetchall()

        return result

    def executeInsert(self, table, insertionDictionary):
        sql = "insert into " + table

        columns = ""
        values = ""

        for column in insertionDictionary:
            value = insertionDictionary[column]

            columns += column + ", "
            values += value + ", "

        columns = columns.strip()

        if columns[-1] == ",":
            columns = columns[:-1]

        columns = "(" + columns + ")"

        values = values.strip()

        if values[-1] == ",":
            values = values[:-1]

        values = "(" + values + ")"

        sql += " " + columns + " values " + values

        self.connection.execute(sql)

        self.connection.commit()

        insertedRowsCount = self.connection.rowcount

        print("Inserção concluída!")

        return insertedRowsCount
        

    def executeDelete(self, table, conditions):
        sql = "delete from " + table + " where " + conditions

        self.connection.execute(sql)

        self.connection.commit()

        deletedRowsCount = self.connection.rowcount

        print("Deleção concluída!")

        return deletedRowsCount


    def executeUpdate(self, table, updateDictionary, conditions):
        sql = "update " + table + " set"

        for column in updateDictionary:
            value = updateDictionary[column]

            sql += " " + column + " = " + value + ", "

        sql = sql.strip()

        if sql[-1] == ",":
            sql = sql[:-1]

        sql += " where " + conditions

        self.connection.execute(sql)

        self.connection.commit()

        updatedRowsCount = self.connection.rowcount

        print("Atualização concluída!")

        return updatedRowsCount
