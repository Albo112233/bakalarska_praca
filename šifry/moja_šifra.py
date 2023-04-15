import time
from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Prosím zadajte otvorený alebo zašifrovaný text.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()
local = time.localtime()

label = Label(root, text="zašifrovaný text")
label.pack()

def sifruj():
    r=0
    k=format(local[0]) # zistí rok
    for j in k:
        r+=int(j)
    m=int(format(local[1])) # zistí mesiac
    d=int(format(local[2])) # zistí deň
    h=int(format(local[3])) # zistí hodinu
    znaky=['A','a','Q','q','y','Y',',',' ','.','W','w','?','s','S','<','>',':','E','e','X','x','r','R','D','d','c','C','V','v','b','B','ô','ú','ä','ň','t','T','Z','z','f','F','h','H','n','N','M','m','-','_','u','U','i','I','J','j','k','K','P','p','o','O','l','L','!','(',')','ď','Ď','@','ľ','š','Š','č','Č','ť','Ť','ž','Ž','ó','ý','á','í','é','=','1','*','2','/','3','4','5','6','+','8','9','7','&','[',']','€','ř',';','0','~','%','#','ŕ','ĺ']
    počet=len(znaky)//2
    text=input_entry.get()
    safe=''
    n=d+h-m-r
    for e in text:
        poloha=0
        posun=0
        for i in znaky:
            if i==e:
                if poloha < počet:
                    posun=poloha+n
                    safe+=znaky[posun]
                elif  poloha > počet:
                    posun=poloha-n
                    safe+=znaky[posun]
            else:
                poloha+=1
    safe+=str(n)
    label.config(text=safe)

button = Button(root, text="Šifruj", command=sifruj)
button.pack()

def desifruj():
    znaky=['A','a','Q','q','y','Y',',',' ','.','W','w','?','s','S','<','>',':','E','e','X','x','r','R','D','d','c','C','V','v','b','B','ô','ú','ä','ň','t','T','Z','z','f','F','h','H','n','N','M','m','-','_','u','U','i','I','J','j','k','K','P','p','o','O','l','L','!','(',')','ď','Ď','@','ľ','š','Š','č','Č','ť','Ť','ž','Ž','ó','ý','á','í','é','=','1','*','2','/','3','4','5','6','+','8','9','7','&','[',']','€','ř',';','0','~','%','#','ŕ','ĺ']
    počet=len(znaky)//2
    text=input_entry.get()
    h=int(text[-2:])
    text=text[:-2]
    original=''
    for e in text:
        poloha=0
        posun=0
        for i in znaky:
            if i==e:
                if poloha < 40:
                    posun=poloha+n
                    original+=znaky[posun]
                elif poloha > 40:
                    posun=poloha-n
                    original+=znaky[posun]
            else:
                poloha+=1

    label.config(text=original)

button1 = Button(root, text="Dešifruj", command=desifruj)
button1.pack()

root.mainloop()
