import sqlite3
from sqlite3 import Error

def create_connection(path):

    try:

        connection = sqlite3.connect(path)

    except Error as e:

        print(e)

    return connection

def add_comand(connection, comand):

    cursor = connection.cursor()

    try:

        cursor.execute(comand)

        connection.commit()

    except Error as e:

        print(e)

connection = create_connection("db.sql")

add_comand(connection, """
CREATE TABLE IF NOT EXISTS student(
    id INT PRIMARY_KEY,
    name VARCHAR(255))
;""")

add_comand(connection, """
CREATE TABLE IF NOT EXISTS employee(
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    salary INTEGER(6))
;""")

add_comand(connection, """
INSERT INTO student(id, name)
VALUES('01', 'John')
""")

add_comand(connection, """
INSERT INTO employee(id, name, salary)
VALUES('01', 'John', '10000')
""")
