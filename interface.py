'''Python interface to interact with Brawlhalla database using SQL
- Rory Collins'''

# to do list
# 1> Add legend
# 2> Edit legend
# 3> Delete legend
# 4> End the world :) DONE

# imports#
import sqlite3
DATABASE = "brawlhalla.db"

legendcount = 52
weaponcount = 13
# functions#


# func 0#
def end():
    print("Ending interface. Bye!!")


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
    print('''Legends:
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
    print('''Weapons:
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
    result1 = cursor.fetchall()
    sql2 = "SELECT WeaponName FROM Weapon"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    # print results#
    print('''Legends:
    ''')
    for item in result1:
        print(f"{item[0]:<10}")
    print('''Weapons:
    ''')
    for item in result2:
        print(f"{item[0]:<10}")
    # close db#
    db.close()


# func 4#
def print_all_legends_and_their_weapons():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql = '''SELECT Legend.legendName,
       Weapon1.weaponName AS Weapon1Name,
       Weapon2.weaponName AS Weapon2Name
FROM Legend
JOIN Weapon AS Weapon1 ON Legend.Weapon1ID = Weapon1.WeaponID
JOIN Weapon AS Weapon2 ON Legend.Weapon2ID = Weapon2.WeaponID;'''
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results#
    print('''Legends    Weapon 1   Weapon 2:
    ''')
    for item in results:
        print(f"{item[0]:<10} {item[1]:<10} {item[2]:<10}")
    # close db#
    db.close()


# func 5#
def search_legend_with_weapon():
    Weapon1ID = int(input('''
Type a the number next to a weapon to see what Legends are able to use it:
Weapons:
1. Hammer
2. Sword
3. Blasters
4. Lance
5. Spear
6. Katars
7. Axe
8. Bow
9. Gauntlets
10. Scythe
11. Cannon
12. Orb
13. Greatsword
Enter number: '''))
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    sql1 = f'''SELECT LegendName FROM Legend
    WHERE Weapon1ID = {Weapon1ID} OR Weapon2ID = {Weapon1ID};'''
    cursor.execute(sql1)
    results = cursor.fetchall()
    sql2 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon1ID};"
    cursor.execute(sql2)
    Weapon1 = cursor.fetchall()
    Weapon1 = str(Weapon1)[3:-4]
    # print results#
    print(f'''Legends with {Weapon1}:
    ''')
    for item in results:
        print(f"{item[0]:<10}")
    # close db#
    db.close()


# func 6#
def search_legend_with_weapons():
    Weapon1ID = int(input('''
Type a the number next to a weapon to see what Legends are able to use it:
Weapons:
1. Hammer
2. Sword
3. Blasters
4. Lance
5. Spear
6. Katars
7. Axe
8. Bow
9. Gauntlets
10. Scythe
11. Cannon
12. Orb
13. Greatsword
Enter number: '''))
    Weapon2ID = int(input('''
Type another number next to a weapon to see what Legends are able to use it:
Weapons:
1. Hammer
2. Sword
3. Blasters
4. Lance
5. Spear
6. Katars
7. Axe
8. Bow
9. Gauntlets
10. Scythe
11. Cannon
12. Orb
13. Greatsword
Enter another number: '''))
    if Weapon2ID < 14 and Weapon1ID < 14:
        # connect to database#
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # sql command query to execute#
        sql = f'''SELECT legendName FROM Legend
        WHERE (weapon1ID = {Weapon1ID} OR weapon2ID = {Weapon1ID})
        AND (weapon1ID = {Weapon2ID} OR weapon2ID = {Weapon2ID});'''
        cursor.execute(sql)
        results = cursor.fetchall()
        sql2 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon1ID};"
        cursor.execute(sql2)
        Weapon1 = cursor.fetchall()
        Weapon1 = str(Weapon1)[3:-4]
        sql3 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon2ID};"
        cursor.execute(sql3)
        Weapon2 = cursor.fetchall()
        Weapon2 = str(Weapon2)[3:-4]
        # print results#
        print(f'''Legends with {Weapon1} and {Weapon2}:
        ''')
        if len(results) <= 0:
            print('''No legends with those two weapons :(
Please try again.''')
        else:
            for item in results:
                print(f"{item[0]:<10}")
        # close db#
        db.close()
    else:
        print("Not a valid number. Try again.")

# function 7#


def add_legend():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    legendName = input("Name of legend: ")
    Weapon1ID = int(input('''Weapons:
1. Hammer
2. Sword
3. Blasters
4. Lance
5. Spear
6. Katars
7. Axe
8. Bow
9. Gauntlets
10. Scythe
11. Cannon
12. Orb
13. Greatsword
What weapon do they have?: '''))
    Weapon2ID = int(input('''Weapons:
1. Hammer
2. Sword
3. Blasters
4. Lance
5. Spear
6. Katars
7. Axe
8. Bow
9. Gauntlets
10. Scythe
11. Cannon
12. Orb
13. Greatsword
What other weapon do they have?: '''))
    sql = f'''INSERT INTO Legend (legendName, weapon1ID, weapon2ID)
VALUES ('{legendName}', {Weapon1ID}, {Weapon2ID});'''
    cursor.execute(sql)
    results = cursor.fetchall
    print(results)
    sql2 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon1ID};"
    cursor.execute(sql2)
    Weapon1 = cursor.fetchall()
    Weapon1 = str(Weapon1)[3:-4]
    sql3 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon2ID};"
    cursor.execute(sql3)
    Weapon2 = cursor.fetchall()
    Weapon2 = str(Weapon2)[3:-4]
    print(f"Added new legend named {legendName}, with {Weapon1}, and {Weapon2}")
    # close db#
    db.close()


# main code#

# ask what function users want to use#
while True:
    print('''
Functions:
0. Quit
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
        if AskQuestion > 9:
            print("Not a valid function. Try again.")
        else:
            # if users input is valid
            if AskQuestion == 0:
                end()
                break
            if AskQuestion == 1:
                print_all_legends()

            if AskQuestion == 2:
                print_all_weapons()

            if AskQuestion == 3:
                print_all_legends_and_weapons()

            if AskQuestion == 4:
                print_all_legends_and_their_weapons()

            if AskQuestion == 5:
                search_legend_with_weapon()

            if AskQuestion == 6:
                search_legend_with_weapons()

            if AskQuestion == 7:
                legendcount += 1
                add_legend()

    except ValueError:
        print("Not a valid function. Try again.")
