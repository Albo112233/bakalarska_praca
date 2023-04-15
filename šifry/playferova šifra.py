from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text. Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()
labelx = Label(root, text="Prosím zadajte kľúč. Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry1 = Entry(root)
input_entry1.pack()

label = Label(root, text="zašifrovaný text")
label.pack()

def sifruj():
    plaintext = input_entry.get()
    key = input_entry1.get()
    
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    plaintext = plaintext.replace("J", "I")
    key = key.replace("J", "I")
    
    alphabet = []
    for letter in key:
        if letter not in alphabet:
            alphabet.append(letter)

    for letter in range(ord("A"), ord("Z")+1):
        if chr(letter) not in alphabet and chr(letter) != "J":
            alphabet.append(chr(letter))

    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(alphabet[i*5 + j])

    pairs = []
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:  
            pair = plaintext[i] + "X"
        elif plaintext[i] == plaintext[i+1]:
            pair = plaintext[i] + "X" + plaintext[i+1]
        else:
            pair = plaintext[i:i+2]
        pairs.append(pair)

    ciphertext = ""
    for pair in pairs:
        row1 = col1 = row2 = col2 = 0
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                if matrix[i][j] == pair[1]:
                    row2, col2 = i, j
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5]
            ciphertext += matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1]
            ciphertext += matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
        label.config(text=ciphertext)
    
        
button = Button(root, text="Šifruj", command=sifruj)
button.pack()

def desifruj():
    ciphertext = input_entry.get()
    key = input_entry1.get()

    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.upper()
    ciphertext = ciphertext.replace("J", "I")
    key = key.replace("J", "I")

    alphabet = []
    for letter in key:
        if letter not in alphabet:
            alphabet.append(letter)
    for letter in range(ord("A"), ord("Z")+1):
        if chr(letter) not in alphabet and chr(letter) != "J":
            alphabet.append(chr(letter))

    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(alphabet[i*5 + j])

    pairs = []
    for i in range(0, len(ciphertext), 2):
        if i == len(ciphertext) - 1:  
            pair = ciphertext[i] + "X"
        elif ciphertext[i] == ciphertext[i+1]:
            pair = ciphertext[i] + "X" + ciphertext[i+1]
        else:
            pair = ciphertext[i:i+2]
        pairs.append(pair)

    plaintext = ""
    for pair in pairs:
        row1 = col1 = row2 = col2 = 0
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                if matrix[i][j] == pair[1]:
                   row2, col2 = i, j
        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5]
            plaintext += matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1)%5][col1]
            plaintext += matrix[(row2-1)%5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    label.config(text=plaintext)
    
button1 = Button(root, text="Dešifruj", command=desifruj)
button1.pack()
root.mainloop()
