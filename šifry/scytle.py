from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()
labelx = Label(root, text="Prosím zadajte počet riadkov matice.")
labelx.pack()
input_entry1 = Entry(root)
input_entry1.pack()
labelx = Label(root, text="Prosím zadajte stĺpcov riadkov matice.")
labelx.pack()
input_entry2 = Entry(root)
input_entry2.pack()

label = Label(root, text="zašifrovaný text")
label.pack()

def encrypt():
    text=input_entry.get()
    row=int(input_entry1.get())
    col=int(input_entry2.get())
    matrix = [['' for j in range(col)] for i in range(row)]
    i, j = 0, 0
    for char in text:
        matrix[i][j] = char
        j += 1
        if j == col:
            j = 0
            i += 1
            
    encrypted_text = ''
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for j in range(num_cols):
        for i in range(num_rows):
            encrypted_text+=matrix[i][j]

    label.config(text=encrypted_text)

button = Button(root, text="Šifruj", command=encrypt)
button.pack()

def decrypt():
    text=input_entry.get()
    row=int(input_entry1.get())
    col=int(input_entry2.get())
    matrix = [['' for j in range(col)] for i in range(row)]    

    pos = 0
    for j in range(col):
        for i in range(row):
            if pos < len(text):
                matrix[i][j] = text[pos]
                pos += 1
            
    decrypted_text = ''
    for i in range(row):
        for j in range(col):
            decrypted_text += matrix[i][j]

    label.config(text=decrypted_text)
button = Button(root, text="Dešifruj", command=decrypt)
button.pack()
root.mainloop()