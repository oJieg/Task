import sqlite3, os

con = sqlite3.connect("MaimBD.db")
cur = con.cursor()


def editMeny():
    ex = 0
    while ex == 0:
        os.system("cls")
        print("hello")
        outBD()
        print("______________")
        print(" 1 - add word")
        print(" 2 - exit")
        print(" 3 - del")
        print("______________")
        inp = input("input command:  ")
        if inp == '1':
            add()
        elif inp == '2':
            break
        elif inp == "3":
            delword()


def add():
    inp = input("eng:  ")
    inp2 = input("ru: ")
    cur.execute("insert into Glassary (EngWord, RuWord) values ( ? , ?)", (inp, inp2))
    con.commit()
    #cur.close()


def delword():
    inp = input("inpyt id delite: ")
    cur.execute("delete from Glassary where ID =:id ", {"id": inp})
    con.commit()


def outBD():
    cur.execute("select ID, EngWord, RuWord, coif from Glassary")
    for n, i, k, w in cur.fetchall():
        print(n, i, k, w)
