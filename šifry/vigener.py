from string import ascii_uppercase
from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text.Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()
labelx1 = Label(root, text="Zadajte prosím otvorený kľúč.Píšte iba veľké písmená bez diakritiky.")
labelx1.pack()
input_entry2 = Entry(root)
input_entry2.pack()

def vytvor_maticu():
    matica = []
    for riadok in ascii_uppercase:
        matica.append([ascii_uppercase[(ord(riadok) + ord(stlpec) - 2 * ord("A")) % 26] for stlpec in ascii_uppercase])
    return matica

label = Label(root, text="výpis")
label.pack()

def sifruj():
    matica = vytvor_maticu()
    sprava=input_entry.get()
    kluc=input_entry2.get()
    polohaspole=[]
    poloharpole=[]
    for e in sprava:
        polohas=0
        for i in matica[0]:
            if i==e:
                polohaspole.append(polohas)
            else:
                polohas+=1
            
    for j in kluc:
        polohar=0
        for y in matica[0]:
            if y==j:
                poloharpole.append(polohar)
            else:
                polohar+=1

    sifrovana_sprava=''
    l=0
    for i in range(len(polohaspole)):
        if l<= len(poloharpole)-1:
            sifrovana_sprava+=matica[int(poloharpole[l])][int(polohaspole[i])]
            l+=1
        else:
            l=0
            sifrovana_sprava+=matica[int(poloharpole[l])][int(polohaspole[i])]
            l+=1
    label.config(text=sifrovana_sprava)

def desifruj():
    matica = vytvor_maticu()
    sprava_s=input_entry.get()
    kluc=input_entry2.get()
    polohaspole=[]
    poloharpole=[]
                
    for j in kluc:
        polohar=0
        for y in matica[0]:
            if y==j:
                poloharpole.append(polohar)
            else:
                polohar+=1

    l=0
    for e in sprava_s:
        polohas=0
        for y in matica[int(poloharpole[l])]:
            if l<= len(poloharpole)-1:
                if y==e:
                    polohaspole.append(polohas)
                    l+=1
                else:
                    polohas+=1
            else:
                l=0
   
    desifrovana_sprava=''
    for i in range(len(polohaspole)):
        desifrovana_sprava+=matica[0][int(polohaspole[i])]
    label.config(text=desifrovana_sprava)

button = Button(root, text="Dešifruj", command=desifruj)
button.pack()

button = Button(root, text="Šifruj", command=sifruj)
button.pack()
root.mainloop()

