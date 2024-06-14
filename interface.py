'''Python interface to interact with Brawlhalla database using SQL
- Rory Collins'''

# imports#
import sqlite3

# variables#
DATABASE = "brawlhalla.db"

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
    # take weapon to search for#
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
14. Boots
Enter number: '''))
    if Weapon1ID > 14 or Weapon1ID < 0:
        print("Invalid input")
    else:
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
    # take first weapon to search for#
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
14. Boots
Enter number: '''))
    # take second weapon to search for#
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
14. Boots
Enter another number: '''))
    if Weapon2ID < 15 and Weapon1ID < 15:
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
        # if no legends then print#
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


# func 7#
def add_legend():
    # take legend name#
    legendName = input("Name of legend: ")
    # take first weapon#
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
14. Boots
What weapon do they have? (Enter number): '''))
    if Weapon1ID > 14 or Weapon1ID < 0:
        print("Invalid input")
    else:
        # take second weapon#
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
14. Boots
What other weapon do they have? (Enter number): '''))
        if Weapon2ID > 14 or Weapon2ID < 0:
            print("Invalid input")
        else:
            # connect to database#
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            # sql command query to execute#
            sql = f'''INSERT INTO Legend (legendName, weapon1ID, weapon2ID)
        VALUES ('{legendName}', {Weapon1ID}, {Weapon2ID});'''
            cursor.execute(sql)
            db.commit()
            sql2 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon1ID};"
            cursor.execute(sql2)
            Weapon1 = cursor.fetchall()
            Weapon1 = str(Weapon1)[3:-4]
            sql3 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon2ID};"
            cursor.execute(sql3)
            Weapon2 = cursor.fetchall()
            Weapon2 = str(Weapon2)[3:-4]
            print(f"Added new Legend named {legendName}, with {Weapon1} and {Weapon2}")
            # close db#
            db.close()


# func 8#
def delete_legend():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # take legend name#
    legendName = input("What is the name of the legend you want to delete?: ")
    # sql command query to execute#
    sql = f'''DELETE FROM Legend WHERE legendName = '{legendName}';'''
    cursor.execute(sql)
    db.commit()
    # print results#
    print(f"Deleted a Legend named {legendName}.")
    # close db#
    db.close()


# func 9#
def edit_legend():
    # connect to database#
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql command query to execute#
    legendName = input("What is the name of the legend you want to edit?: ")
    sql4 = f"SELECT legendName FROM Legend WHERE legendName = '{legendName}';"
    cursor.execute(sql4)
    results = cursor.fetchall
    if len(str(results)) < 1:
        print(f"No legend named {legendName}")
    else:
        # take first weapon#
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
14. Boots
What weapon do you want them to have? (Enter number): '''))
        # take second weapon#
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
14. Boots
What other weapon do you want them to have? (Enter number): '''))
        # update legend#
        sql = f'''UPDATE Legend
        SET legendName = '{legendName}',
        Weapon1ID = {Weapon1ID}, Weapon2ID = {Weapon2ID}
        WHERE legendName = '{legendName}';'''
        cursor.execute(sql)
        db.commit()
        sql2 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon1ID};"
        cursor.execute(sql2)
        Weapon1 = cursor.fetchall()
        Weapon1 = str(Weapon1)[3:-4]
        sql3 = f"SELECT WeaponName FROM Weapon WHERE WeaponID = {Weapon2ID};"
        cursor.execute(sql3)
        Weapon2 = cursor.fetchall()
        Weapon2 = str(Weapon2)[3:-4]
        print(f'''Edited a Legend named {legendName}.
So they now have {Weapon1} and {Weapon2}!''')
        # close db#
        db.close()


# func 10#
def quiz():
    try:
        # take type of quiz#
        typeofquiz = int(input('''What type of quiz do you want to do?
1. Guess Legend based on two weapons
2. Guess two Weapons based on Legend
'''))
        if typeofquiz > 2:
            print("Invalid number.")
        else:
            correctq = 0
            if typeofquiz == 1:
                try:
                    # take number of questions#
                    amount = int(input("How many questions?: "))
                    # connect to database#
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    # sql command query to execute#
                    for i in range(amount):
                        # select random legend#
                        sql = '''SELECT legendName FROM Legend
            ORDER BY RANDOM()
            LIMIT 1'''
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        # results = (['NAME'])
                        results = str(results)[3:-4]
                        # results = NAME#
                        sql2 = f'''SELECT weapon1ID FROM Legend
            WHERE legendName = '{results}';'''
                        cursor.execute(sql2)
                        Weapon1ID = cursor.fetchall()
                        # Weapon1ID = (ID,)#
                        Weapon1ID = str(Weapon1ID)[2:-3]
                        # Weapon1ID = ID#
                        sql3 = f'''SELECT weapon2ID FROM Legend
            WHERE legendName = '{results}';'''
                        cursor.execute(sql3)
                        Weapon2ID = cursor.fetchall()
                        # Weapon2ID = (ID,)#
                        Weapon2ID = str(Weapon2ID)[2:-3]
                        # Weapon2ID = ID#
                        sql4 = f'''SELECT WeaponName FROM Weapon
            WHERE WeaponID = {Weapon1ID};'''
                        cursor.execute(sql4)
                        Weapon1 = cursor.fetchall()
                        Weapon1 = str(Weapon1)[3:-4]
                        sql5 = f'''SELECT WeaponName FROM Weapon
            WHERE WeaponID = {Weapon2ID};'''
                        cursor.execute(sql5)
                        Weapon2 = cursor.fetchall()
                        Weapon2 = str(Weapon2)[3:-4]
                        answer = input(f"What legend has {Weapon1} and {Weapon2}?: ")
                        # check answer is correct#
                        if answer.lower() == results.lower():
                            print("Correct!!")
                            correctq += 1
                        else:
                            print(f"Incorrect, its {results}!")
                    # close db#
                    db.close()
                except ValueError:
                    print("Not a valid number. Try again.")
                # print correct question score and percent#
                try:
                    percent = int(correctq) / int(amount) * 100
                    print(f"Your score was: [{correctq}/{amount}] ({percent}%)")
                except:
                    print("Invalid score.")
            if typeofquiz == 2:
                try:
                    # take question amount#
                    amount = int(input("How many questions?: "))
                    # connect to database#
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    # sql command query to execute#
                    for i in range(amount):
                        q1correct = 0
                        q2correct = 0
                        # select random legend#
                        sql = '''SELECT legendName FROM Legend
            ORDER BY RANDOM()
            LIMIT 1'''
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        # results = (['NAME'])
                        results = str(results)[3:-4]
                        # results = NAME#
                        sql2 = f'''SELECT weapon1ID FROM Legend
            WHERE legendName = '{results}';'''
                        cursor.execute(sql2)
                        Weapon1ID = cursor.fetchall()
                        # Weapon1ID = (ID,)#
                        Weapon1ID = str(Weapon1ID)[2:-3]
                        # Weapon1ID = ID#
                        sql3 = f'''SELECT weapon2ID FROM Legend
            WHERE legendName = '{results}';'''
                        cursor.execute(sql3)
                        Weapon2ID = cursor.fetchall()
                        # Weapon2ID = (ID,)#
                        Weapon2ID = str(Weapon2ID)[2:-3]
                        # Weapon2ID = ID#
                        sql4 = f'''SELECT WeaponName FROM Weapon
            WHERE WeaponID = {Weapon1ID};'''
                        cursor.execute(sql4)
                        Weapon1 = cursor.fetchall()
                        Weapon1 = str(Weapon1)[3:-4]
                        sql5 = f'''SELECT WeaponName FROM Weapon
            WHERE WeaponID = {Weapon2ID};'''
                        cursor.execute(sql5)
                        Weapon2 = cursor.fetchall()
                        Weapon2 = str(Weapon2)[3:-4]
                        answer1 = input(f"{results} has two weapons, what is the first one?: ")
                        # check answers are correct#
                        if answer1.lower() == Weapon1.lower() or answer1.lower() == Weapon2.lower():
                            print("Correct!!")
                            q1correct = 1
                        else:
                            print("Incorrect.")
                        answer2 = input(f"{results} has two weapons, what is the second one?: ")
                        if answer2.lower() == Weapon1.lower() or answer2.lower() == Weapon2.lower():
                            print("Correct!!")
                            q2correct = 1
                        else:
                            print(f"Incorrect, it's {Weapon1} and {Weapon2}!")
                        # if both questions are correct, add 1 to correct question total#
                        if q1correct == 1 and q2correct == 1:
                            correctq += 1
                    # print correct question score and percent#
                    try:
                        percent = int(correctq) / int(amount) * 100
                        print(f"Your score was: [{correctq}/{amount}] ({percent}%)")
                    except:
                        print("Invalid score.")
                    # close db#
                    db.close()
                except ValueError:
                    print("Not a valid number. Try again.")
    except ValueError:
        print("Invalid number.")


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
7. Add a new Legend
8. Delete a Legend
9. Edit a Legend
10. Quiz
''')

    # account for invalid inputs#
    try:
        AskQuestion = int(input("What do you want to do? "))
        if AskQuestion > 10 or AskQuestion < 0:
            print("Not a valid function. Try again.")
        else:
            # if users input is valid
            if AskQuestion == 0:
                # end database#
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
                add_legend()

            if AskQuestion == 8:
                delete_legend()

            if AskQuestion == 9:
                edit_legend()

            if AskQuestion == 10:
                quiz()
    except ValueError:
        print("Not a valid function. Try again.")
