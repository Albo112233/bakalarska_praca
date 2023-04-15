from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text. Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()

labelx1 = Label(root, text="Prosím zadajte kľúč v rozmedzí 1-25.")
labelx1.pack()
input_spinbox = Spinbox(root, from_=1, to=25)
input_spinbox.pack()

label = Label(root, text="výpis")
label.pack()

def sifruj():
    abeceda=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sprava=input_entry.get()
    kluc=int(input_spinbox.get())
    sifrovana_sprava=""
    posun_abeceda=[chr((ord(znak) - ord("A") + kluc) % 26 + ord("A")) for znak in abeceda]
    for e in sprava:
        poloha=0
        for i in abeceda:
            if i==e:
                sifrovana_sprava+=posun_abeceda[poloha]
            else:
                poloha+=1
    label.config(text=sifrovana_sprava)

button = Button(root, text="Šifruj", command=sifruj)
button.pack()

def desifruj():
    abeceda=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sifrovana_sprava=input_entry.get()
    kluc=int(input_spinbox.get())
    sprava=""
    posun_abeceda=[chr((ord(znak) - ord("A") + kluc) % 26 + ord("A")) for znak in abeceda]
    for e in sifrovana_sprava:
        poloha=0
        for i in posun_abeceda:
            if i==e:
               sprava+=abeceda[poloha]
            else:
                poloha+=1
    label.config(text=sprava)

button = Button(root, text="Dešifruj", command=desifruj)
button.pack()
root.mainloop()

