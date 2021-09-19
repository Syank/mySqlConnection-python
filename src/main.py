import mysql.connector as mysql


def selectExemple(cursor):
    print("---- Exemplo de select ----")
    sql = "select * from alunos;"

    print(sql)
    print("Resultado:")
    cursor.execute(sql)

    registros = cursor.fetchall()

    for registro in registros:
        print(registro)

    print("-------------------------\n")


def insertExemple(cursor):
    print("---- Exemplo de insert ----")
    sql = "insert into alunos (nome, curso) values ('Natasha', 'BDD');"
    print(sql)

    cursor.execute(sql)

    print(cursor.rowcount, "Inserido com sucesso!")
    print("-------------------------\n")


def updateExemple(cursor):
    print("---- Exemplo de update ----")
    sql = "update alunos set nome = 'Rafael Furtado' where id = 1;"
    print(sql)

    cursor.execute(sql)

    print(cursor.rowcount, "Atualizado com sucesso!")
    print("-------------------------\n")


def deleteExemple(cursor):
    print("---- Exemplo de delete ----")
    sql = "delete from alunos where id = 2;"
    print(sql)

    cursor.execute(sql)

    print(cursor.rowcount, "Deletado com sucesso!")
    print("-------------------------\n")


def exemples(cursor):
    selectExemple(cursor)
    insertExemple(cursor)
    updateExemple(cursor)
    deleteExemple(cursor)

    selectExemple(cursor)


host = "192.168.1.104"
database = "fatec"
user = "admin"
password = "123"
connection = mysql.connect(host=host, database=database, user=user, password=password, connection_timeout=5)

cursor = connection.cursor()

exemples(cursor)

