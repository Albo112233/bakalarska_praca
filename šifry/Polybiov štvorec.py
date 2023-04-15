from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text. Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()
labelx1 = Label(root, text="Prosím zadajte kľúč. Píšte iba veľké písmená bez diakritiky.")
labelx1.pack()
input_entry1 = Entry(root)
input_entry1.pack()


label = Label(root, text="výpis")
label.pack()

def sifruj():
    plaintext = input_entry.get()
    key = input_entry1.get()
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    plaintext = plaintext.replace("W", "")
    key = key.replace("W", "")
    
    alphabet = []
    for letter in key:
        if letter not in alphabet:
            alphabet.append(letter)

    for letter in range(ord("A"), ord("Z")+1):
        if chr(letter) not in alphabet and chr(letter) != "W":
            alphabet.append(chr(letter))

    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(alphabet[i*5 + j])
    
    cryptid=''
    for e in plaintext:
        for i in range(5):
            for j in range(5):
                if e == matrix[i][j]:
                    cryptid+=str(i+1)
                    cryptid+=str(j+1)
                    
    label.config(text=cryptid)

button = Button(root, text="Šifruj", command=sifruj)
button.pack()

def desifruj():
    plaintext = input_entry.get()
    key = input_entry1.get()
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    plaintext = plaintext.replace("W", "")
    key = key.replace("W", "")
    
    alphabet = []
    for letter in key:
        if letter not in alphabet:
            alphabet.append(letter)

    for letter in range(ord("A"), ord("Z")+1):
        if chr(letter) not in alphabet and chr(letter) != "W":
            alphabet.append(chr(letter))

    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(alphabet[i*5 + j])
    
    ciphertext = ''
    i=[]
    j=[]
    k,l=0,0
    for g in plaintext[::2]:
        i.append(int(g))
        k+=1
    for f in plaintext[1::2]:
        j.append(int(f))
        l+=1
        
    for e in range(len(i)):
        ciphertext += matrix[i[e]-1][j[e]-1]
    label.config(text=ciphertext)

button = Button(root, text="Dešifruj", command=desifruj)
button.pack()
root.mainloop()