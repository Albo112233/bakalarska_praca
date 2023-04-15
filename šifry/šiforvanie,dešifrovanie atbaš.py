from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text. Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()

label = Label(root, text="výpis")
label.pack()

def atbas():
    abeceda=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sprava=input_entry.get()
    počet=len(abeceda)//2
    sifrovana_sprava=""
    for e in sprava:
        poloha=0
        zmena=0
        for i in abeceda:
            if i==e:
                zmena=počet-poloha+počet-1
                sifrovana_sprava+=abeceda[zmena]
            else:
                poloha+=1
    
    label.config(text=sifrovana_sprava)

button = Button(root, text="Šifruj/dešifruj", command=atbas)
button.pack()
root.mainloop()