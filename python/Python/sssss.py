import mysql.connector

cnx = mysql.connector.connect(user='aaaa', password='1363',
                              host='127.0.0.1',
                              database='employees')
cnx.close()