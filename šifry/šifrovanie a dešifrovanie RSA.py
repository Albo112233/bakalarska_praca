import random
import math

from tkinter import *
root = Tk()
root.geometry("960x550+0+0")
root.title("Šifrovacia aplikácia")

labelx = Label(root, text="Zadajte prosím otvorený alebo zašifrovaný text. Píšte iba veľké písmená bez diakritiky.")
labelx.pack()
input_entry = Entry(root)
input_entry.pack()

label = Label(root, text="")
label.pack()
label1 = Label(root, text="")
label1.pack()
label2 = Label(root, text="")
label2.pack()
label3 = Label(root, text="")
label3.pack()

def NSD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverse_modulo(a, m):
    if NSD(a, m) != 1:
        return None  
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def random_prime(low, high):
    while True:
        num = random.randint(low, high)
        if is_prime(num):
            return num

def encrypt(ascii_codes, public_key):
    encrypted_message=[]
    e, n = public_key
    for i in ascii_codes:
        encrypted_message.append(pow(i, e, n))
    return encrypted_message

def decrypt(ciphertext, private_key):
    decrypted_message=[]
    d, n = private_key
    for i in ciphertext:
        decrypted_message.append(pow(i, d, n))
    return decrypted_message

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p a q musia byť prvočísla.")
    elif p == q:
        raise ValueError("p a q nemôžu byť rovnaké čísla.")
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = NSD(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = NSD(e, phi)
    d = inverse_modulo(e, phi)
    return ((e, n), (d, n))

def convert_to_ascii(string):
    ascii_codes = []
    for char in string:
        ascii_code = ord(char)
        ascii_codes.append(ascii_code)
    return ascii_codes


def convert_from_ascii(decrypted_message):
    characters = ""
    for code in decrypted_message:
        character = chr(code)
        characters += character
    return characters

def sifruj():
    if __name__ == '__main__':
        p = random_prime(50, 100)
        q = random_prime(100, 150)
        public_key, private_key = generate_keypair(p, q)
        message = input_entry.get()
        ascii_codes = convert_to_ascii(message)
        encrypted_message = encrypt(ascii_codes, public_key)
        decrypted_message = decrypt(encrypted_message, private_key)
        characters = convert_from_ascii(decrypted_message)
        label.config(text=public_key)
        label1.config(text=private_key)
        label2.config(text=encrypted_message)
        label3.config(text=characters)


button = Button(root, text="Šifruj", command=sifruj)
button.pack()
root.mainloop()
