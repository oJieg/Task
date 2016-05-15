import sqlite3, os, random

con = sqlite3.connect("MaimBD.db")
cur = con.cursor()
listotv = [[], []]

winCoef = -1
loserCoef = 1


def HelloTestMeny(Ru_):
    sizetest = 0  # кол-во вопросов
    while sizetest == 0:
        os.system("cls")
        print("hello")
        print("elect size")
        print("1- size small")
        print("2- size mediym ")
        print("3 size big")
        print("4 - exit")
        inp = input("input command:  ")
        if inp == '1':
            sizetest = 3
        elif inp == "2":
            sizetest = 5
        elif inp == "3":
            sizetest = 50
        elif inp == "4":
            break
    if sizetest != 0:
        testMenu(sizetest, Ru_)


def testMenu(sizetest, Ru_):
    a = []
    cur.execute("select ID, EngWord, RuWord, coif from Glassary Order by coif")
    a = cur.fetchmany(sizetest)  # составляем список задействованых слов
    # print(a)
    cur.execute("select ID from Glassary Order by ID Desc")
    sizea = cur.fetchmany(1)
    sizea = sizea[0][0]
    print(sizea)

    for i in range(sizetest):
        os.system("cls")
        if Ru_ == "ru":  # !!!!!!!!!!!! если ру то русское слово в вариантах
            print(a[i][1], "ad;flkjasf")
            if rendPoint(a[i][2], "RuWord", sizea) == 1:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": a[i][3] + winCoef, "id": a[i][0]})
            else:
                print(a[i][3] + loserCoef)
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": a[i][3] + loserCoef, "id": a[i][0]})


        elif Ru_ == "eng":
            print(a[i][2])
            if rendPoint(a[i][1], "EngWord", sizea) == 1:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id", {"coi": a[i][3] + winCoef, "id": a[i][0]})
            else:
                cur.execute("UPDATE Glassary SET coif=:coi WHERE Id=:id",
                            {"coi": a[i][3] + loserCoef, "id": a[i][0]})
    con.commit()


def rendPoint(answer, word, sizea):
    tryanswer = random.randint(0, 4)
    for i in range(0, 5):

        if tryanswer == i:
            print(i, answer, "+")
        else:
            ex = 0
            while ex == 0:
                if word == "RuWord":
                    cur.execute("select RuWord from  Glassary WHERE ID=:id ", {"id": random.randint(1, sizea)})
                elif word == "EngWord":
                    cur.execute("select EngWord from  Glassary WHERE ID=:id ", {"id": random.randint(1, sizea)})
                z = cur.fetchall()
                if z[0][0] != answer:
                    break
            print(i, z[0][0])

    print(tryanswer)
    inp = int(input("??"))
    if inp == tryanswer:
        print("win")
        return 1
    else:
        print("luz")
        return 0
