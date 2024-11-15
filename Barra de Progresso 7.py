from tkinter import *
from tkinter.ttk import *
import time
import tkinter as tk

def start():
    GB = 5000
    download = 0
    speed = 1
    while(download < GB):
        time.sleep(0)
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GB completed")
        window.update_idletasks()

window = Tk()

# Definindo cores e fontes
window.title("Download Simulation")
window.config(bg="#1e1e1e")
window.geometry("400x250")

# Variáveis para texto
percent = StringVar()
text = StringVar()

# Barra de progresso
bar = Progressbar(window, orient=HORIZONTAL, length=300, maximum=100, mode='determinate')
bar.pack(pady=20)

# Labels
percentLabel = Label(window, textvariable=percent, font=('Arial', 12, 'bold'), foreground="#00FF00", background="#1e1e1e")
percentLabel.pack()

taskLabel = Label(window, textvariable=text, font=('Arial', 10), foreground="#FFFFFF", background="#1e1e1e")
taskLabel.pack(pady=10)

# Botão com estilo
button = tk.Button(window, text="Start Download", command=start, font=('Arial', 15, 'bold'), foreground="darkolivegreen", background="aqua")
button.pack(pady=20)

window.mainloop()
