#Conexión a la base de datos
import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Alg0R@ndo5",
    database = "db_starts"
)