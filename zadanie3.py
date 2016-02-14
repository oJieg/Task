a=int(input("vvedite god: "))
if a % 4 == 0:
 if a % 100 == 0:
   if a % 400 == 0:
    print("god visokosnui")
   else:
    print("god nevisokosnui")
 else:
  print("god visokosnui")
else:
 print("god nevisokosnui") 
 
