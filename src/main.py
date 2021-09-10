from connection import ConnectionManager

conn = ConnectionManager("localhost", "mysqluser", "pass", "database")





def testSelect():
    table = ""    

    results = conn.executeSelect(table)

    for result in results:
        print(result)

def testInsert():
    table = ""
    values = {"1": "a", "2": "b"}

    
    pass

def testUpdate():
    pass

def testDelete():
    pass
