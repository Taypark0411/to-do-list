import sqlite3
from sqlite3 import Error


def createconnection():
    db_file = r"C:\DevApps\sqlite\Testdb.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Exception as e:
        print("dbconnection error: " + e)
    return connection


if __name__ == "__main__":
    createconnection()
