# hesap makinesi arayüz
import tkinter as tk
from tkinter import END

def button_click(number):
    entry.insert(END,number)
def clear():
    entry.delete(0,END)
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,END)
        entry.insert(END,str(result))
    except Exception:
        entry.delete(0, END)
        entry.insert(END,"Error")
root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("300x400")
root.configure(bg="#e4b3e6")
entry = tk.Entry(root,width=20,font=("Arial",20),justify='right')
entry.grid(row=0,column=0,columnspan=4,pady=10)
tuslar = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('+',4,2),('=',4,3)
]
for (text, row, col) in tuslar:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 15),
                  command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 15),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)
clear_button = tk.Button(root, text="C", width=5,
                         height=2, font=("Arial", 15), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, pady=10)
root.mainloop()
