import math
import random


def breeding(text, parts):  #делит на равные части
    text_part = []
    lon=len(text)                             #длинна всего текста
    parts_lon =  math.ceil(lon / parts)       #длинна одной части
    #print(parts_lon)
    for i in range(0, lon, parts_lon):
        text_part.append( text[i : i+parts_lon] )
        
    if lon%parts !=0:   #если не по ровну, добавляем пробелы
        x=len(text_part)-1
        for i in range(len(text_part[0])-len(text_part[x])):
           # print(i)
            text_part[x] += " "    
            
    if len(text_part) !=parts :
        text_part.append("")
        for i in range(0, parts_lon):
            text_part[len(text_part)-1]+=" "

    

    return text_part


def dedreeding(parts_text):
    text=""
    for i in range(0, len(parts_text)):
        text+=parts_text[i]
    return text


def generatinKey(parts_text):
    parts_lon=len(parts_text[0])
    parts=len(parts_text)
    key=str(parts)

    for i in range(0, parts):
        key=key+str(i)
        for k in range(0, parts_lon):
            x=random.randint(0, parts-1)

            while x == i:
                x=random.randint(0, parts-1)
            key=key+str(x)

        key=key+str(i)

    return key


def coding(parts_text, key):
    
    
    parts_lon=len(parts_text[0])
    parts=len(parts_text)
    numb_key=2

    for i in range(0,parts):
        for k in range(0,parts_lon):
            x=int(key[numb_key])
           # print(x,i,k)
            #if k == parts_lon-1:k-=1

            bufT2 = parts_text[i][k]
            #if k==0:
             #   buf1=parts_text[x][k] + parts_text[i][k+1:parts_lon]
              #  buf2=bufT1 + parts_text=[x][k+1:parts_lon]
            buf1=parts_text[i][0:k] + parts_text[x][k] + parts_text[i][k+1:parts_lon]
            buf2=parts_text[x][0:k] + bufT2 + parts_text[x][k+1:parts_lon]

            parts_text[i] = buf1
            parts_text[x] = buf2

            numb_key += 1


        numb_key += 2
   # print(parts_text)
    return parts_text


def decoding(parts_text, key):
    parts_lon=len(parts_text[0])
    parts=len(parts_text)
    numb_key=len(key)-2

    for i in range(parts-1, -1, -1):
        for k in range(parts_lon-1, -1, -1):
            x=int(key[numb_key])
           # print(x,i,k)
            #if k == parts_lon-1:k-=1

            bufT2 = parts_text[i][k]
            #if k==0:
             #   buf1=parts_text[x][k] + parts_text[i][k+1:parts_lon]
              #  buf2=bufT1 + parts_text=[x][k+1:parts_lon]
            buf1=parts_text[i][0:k] + parts_text[x][k] + parts_text[i][k+1:parts_lon]
            buf2=parts_text[x][0:k] + bufT2 + parts_text[x][k+1:parts_lon]

            parts_text[i] = buf1
            parts_text[x] = buf2

            numb_key -= 1


        numb_key -= 2
   # print(parts_text)
    return parts_text


texting = input("input text")
lon_parts= int(input("input long part"))
while lon_parts>9 or lon_parts<2:
    print("xuinu ne vvodi")
    lon_parts= int(input("input long part"))
tx=breeding(texting,lon_parts)
print("parts vervion ", tx )
key=generatinKey(tx)
print("key= ",key)
cod=coding(tx,key)
text_cod=dedreeding(cod)
#print("parts cipher vervion ",cod)
print("cipher text: ", text_cod)
cod=breeding(text_cod,lon_parts)
#print(cod)
decod=decoding(cod, key)
#print(decod)
text_cod=dedreeding(decod)
print("decipher text: ",text_cod)
