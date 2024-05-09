'''Rory Collins - Python interface to interact with SQL database'''
# imports#
import sqlite3
DATABASE = "brawlhalla.db"

# functions#


# func 1#
def print_all_legends():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql = "SELECT LegendName FROM Legend;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results#
    print('''Legends
    ''')
    for item in results:
        print(f"{item[0]:<10}")
    # close db#
    db.close()


# func 2#
def print_all_weapons():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql = "SELECT WeaponName FROM Weapon;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results#
    print('''Weapons
    ''')
    for item in results:
        print(f"{item[0]:<10}")
    # close db#
    db.close()


# func 3#
def print_all_legends_and_weapons():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql1 = "SELECT LegendName FROM Legend;"
    cursor.execute(sql1)
    results = cursor.fetchall()
    # print results#
    print('''Legends  Weapons
    ''')
    for item in results:
        print(f"{item[0]:<10}")
    # close db#
    db.close()


# func 4#
def print_all_legends_and_their_weapons():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql = "SELECT LegendName,Weapon1,Weapon2 FROM Legend;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results#
    print('''Legends    Weapon 1   Weapon 2
    ''')
    for item in results:
        print(f"{item[0]:<10} {item[1]:<10} {item[2]:<10}")
    # close db#
    db.close()

# func 5#
def search_legend_with_1_weapon()
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql = f"SELECT LegendName,Weapon1,Weapon2 FROM Legend WHERE Weapon1 OR Weapon2 = {Weapon1};"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results#
    print('''Legends    Weapon 1   Weapon 2
    ''')
    for item in results:
        print(f"{item[0]:<10} {item[1]:<10} {item[2]:<10}")
    # close db#
    db.close()


# main code#

# ask what function users want to use#
while True: 
    print('''
Functions:
1. Print all Legends
2. Print all Weapons
3. Print all Legends and Weapons
4. Print all Legends and their Weapons
5. Search for Legends with 1 Weapon
6. Search for Legends with 2 Weapons
''')

    # account for invalid inputs#
    try:
        AskQuestion = int(input("What do you want to do? "))
    except ValueError:
        print("Not a valid function. Try again.")

    # if users input is valid
    if AskQuestion == 1:
        print_all_legends()
        break
    if AskQuestion == 2:
        print_all_weapons()
        break
    if AskQuestion == 3:
        print_all_legends_and_weapons()
    if AskQuestion == 4:
        print_all_legends_and_their_weapons()
        break
    if AskQuestion == 5:
        input('''Type a weapon to see what Legends are able to use it: 
        1. Weapons:
        2. Hammer
        3. Sword
        4. Blasters
        5. Lance
        6. Katars
        7. Axe
        8. Bow
        9. Gauntlets
        10. Scythe
        11. Cannon
        12. Orb
        13. Greatsword
        14. Boots''')