import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

class ProgramSelector:
    def __init__(self, master):
        self.master = master
        master.title('Program Selector')
        self.create_buttons()
        
    def create_buttons(self):
        self.button1 = tk.Button(self.master, text='Cézarova šifra', command=lambda: self.run_program('cezarova.py'))
        self.button2 = tk.Button(self.master, text='Atbaš', command=lambda: self.run_program('šiforvanie,dešifrovanie atbaš.py'))
        self.button3 = tk.Button(self.master, text='Vigenerova šifra', command=lambda: self.run_program('vigener.py'))
        self.button4 = tk.Button(self.master, text='Hillova šifra', command=lambda: self.run_program('hillova.py'))
        self.button5 = tk.Button(self.master, text='Playferova šifra', command=lambda: self.run_program('playferova šifra.py'))
        self.button6 = tk.Button(self.master, text='Moja šifra', command=lambda: self.run_program('moja_šifra.py'))
        self.button7 = tk.Button(self.master, text='Polybiov štvorec', command=lambda: self.run_program('Polybiov štvorec.py'))
        self.button8 = tk.Button(self.master, text='Scytle', command=lambda: self.run_program('scytle.py'))
        self.button9 = tk.Button(self.master, text='šifra RSA', command=lambda: self.run_program('šifrovanie a dešifrovanie RSA.py'))
        
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()
        self.button7.pack()
        self.button8.pack()
        self.button9.pack()
        
    def run_program(self, program_file):
        messagebox.showinfo('Program Selector', 'Spúšťam program {}'.format(program_file))
        subprocess.Popen(["python", program_file])
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("960x550+0+0")
    selector = ProgramSelector(root)
    root.mainloop()