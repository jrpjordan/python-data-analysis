# run: pip3 install mysql-connector-python
# run: docker run -p 3306:3306 --name python-test -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e  MYSQL_DATABASE=test -e MYSQL_USER=test -e MYSQL_PASSWORD=test -d mysql:latest
import mysql.connector

cnx = mysql.connector.connect(host="localhost",
                              port=3306,
                              user="test",
                              password="test",
                              database="test")

query = """
CREATE TABLE test 
(a VARCHAR(20), b VARCHAR(20), c INT, d INT);
"""
cursor = cnx.cursor()
cursor.execute(query)
cnx.commit()

#Inserting some data
data = [("Atlanta", "Georgia", 1.25, 6),
        ("Tallahassee", "Florida", 2.6, 3),
        ("Sacramento", "California", 1.7, 5)]
stmt = "INSERT INTO test VALUES (%s, %s, %s, %s)"
cursor.executemany(stmt, data)
cnx.commit()

cnx.close()