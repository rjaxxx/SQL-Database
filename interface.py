'''Rory Collins - Python interface to interact with SQL database - 29/04/2024'''
# imports#
import sqlite3
DATABASE = ".db"


# functions#
def print_all_():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql = "SELECT"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results#
    print(results)
    # close db#
    db.close

# main code#
print_all()