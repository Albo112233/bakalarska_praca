import numpy as np
import math
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

def multiply_matrix(m1, m2):
    m3 = np.zeros((m1.shape[0], m2.shape[1]), dtype=int)
    for i in range(m1.shape[0]):
        for j in range(m2.shape[1]):
            for k in range(m2.shape[0]):
                m3[i][j] += m1[i][k] * m2[k][j]
            m3[i][j] %= 26
    return m3

def sifruj():
    LETTER_A = 65
    ALPHABET_SIZE = 26

    key_str = input_entry1.get()
    key_str = key_str.upper()
    key_str = key_str.replace(" ", "")
    key_nums = [ord(c) - 65 for c in key_str]
    n = int(math.sqrt(len(key_nums)))
    key_matrix = np.array(key_nums).reshape(n, n)

    message = input_entry.get()
    message = ''.join(filter(str.isalpha, message)).upper()
    block_size = key_matrix.shape[0]

    if len(message) % block_size != 0:
        message += ' ' * (block_size - len(message) % block_size)

    blocks = [np.array([ord(c) - LETTER_A for c in message[i:i+block_size]]).reshape(block_size, 1) for i in range(0, len(message), block_size)]
    message_matrix = np.hstack(blocks)
    encrypted_matrix = multiply_matrix(key_matrix, message_matrix)


    encrypted_text = ""
    for i in range(encrypted_matrix.shape[1]):
        for j in range(encrypted_matrix.shape[0]):
            encrypted_text += chr(int(encrypted_matrix[j][i]) + LETTER_A)

    label.config(text=encrypted_text)

button = Button(root, text="Šifruj", command=sifruj)
button.pack()

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x1, y1 = extended_euclidean_algorithm(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)



def inv_mat(mat):
    D = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    a = 0
    if D<0 or D>26:
        a = D%26
    else:
        a=D
    b = 26
    d, u, v = extended_euclidean_algorithm(a, b)
    mat[0][1]*=-1
    mat[1][0]*=-1
    mat[0][0], mat[1][1] = mat[1][1], mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j] * u
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j] % 26
    return mat

def get_key():
    key_str = input_entry1.get()
    key_str = key_str.upper()
    key_str = key_str.replace(" ", "")
    key_nums = [ord(c) - 65 for c in key_str]
    n = int(math.sqrt(len(key_nums)))
    return np.array(key_nums).reshape(n, n)


def desifruj():
    LETTER_A = 65
    ALPHABET_SIZE = 26
    MODULUS = ALPHABET_SIZE

    key = get_key()

    message = input_entry.get()

    message = ''.join(filter(str.isalpha, message)).upper()
    block_size = key.shape[0]

    if len(message) % block_size != 0:
        message += ' ' * (block_size - len(message) % block_size)

    blocks = [np.array([ord(c) - LETTER_A for c in message[i:i+block_size]]).reshape(block_size, 1) for i in range(0, len(message), block_size)]
    message_matrix = np.hstack(blocks)
    i_matrix = inv_mat(key)
    decrypted_matrix = multiply_matrix(i_matrix, message_matrix)

    decrypted_text = ""
    for i in range(decrypted_matrix.shape[1]):
        for j in range(decrypted_matrix.shape[0]):
            decrypted_text += chr(int(decrypted_matrix[j][i]) + LETTER_A)

    label.config(text=decrypted_text)


button = Button(root, text="Dešifruj", command=desifruj)
button.pack()
root.mainloop()
