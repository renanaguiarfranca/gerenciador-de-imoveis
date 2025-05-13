from settings import *
import mysql.connector
db = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    database=DB_NAME
)
cursor = db.cursor()