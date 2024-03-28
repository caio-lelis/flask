import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='c@t5RUn#N1ght',
        database='teste_mysql'
    )
    return connection