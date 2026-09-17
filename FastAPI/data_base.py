import os
import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,
        user=os.environ['User'],
        passwd=os.environ['passwd'],
        database='fastapilearning',
        charset='utf8',
        cursorclass=DictCursor
    )