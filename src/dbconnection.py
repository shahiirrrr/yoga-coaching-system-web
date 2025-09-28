import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Environment-driven DB configuration with safe defaults
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
MYSQL_DB = os.getenv('MYSQL_DB', 'yoga')


def iud(qry, val):
    con = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cmd = con.cursor()
    cmd.execute(qry, val)
    id = cmd.lastrowid
    con.commit()
    con.close()

    return id


def selectone(qry, val):
    con = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, cursorclass=pymysql.cursors.DictCursor)
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.fetchone()

    return res


def selectall(qry) -> object:
    con = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, cursorclass=pymysql.cursors.DictCursor)
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchall()
    return res


def selectall2(qry, val):
    con = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, cursorclass=pymysql.cursors.DictCursor)
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.fetchall()
    return res