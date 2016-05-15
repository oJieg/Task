import InpWord, TestWord
import sqlite3, os


def menMain():
    ex = 0
    while ex == 0:
        os.system("cls")
        print("hello")
        print("1-edit word")
        print("2-test")
        print("3- exet")
        print("0-create table")
        inp = input("input command:  ")
        if inp == '1':
            InpWord.editMeny()
            # elif inp == '2':
            # outBD()
        elif inp == '2':
            TestWord.HelloTestMeny("eng")
        elif inp == "3":
            # ex = 1
            break
        elif inp == "0":
            con = sqlite3.connect("MaimBD.db")
            cur = con.cursor()
            cur.execute(
                "create table Glassary (ID integer primary key, EngWord, RuWord, coif DEFAULT 10, dataRepeat, Enable BLOB)")


# __________________________________________________________________________#
# __________________________________________________________________________#
# __________________________________________________________________________#


menMain()
