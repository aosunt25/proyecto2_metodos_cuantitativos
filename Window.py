import math
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
#from CuadradosMedios import CuadradosMedios



class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        container = tk.Frame(master)
        self.canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(
            container, orient="vertical", command=self.canvas.yview
        )
        scrollable_frame = ttk.Frame(self.canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="w")
        self.canvas.config(width=605, height=1000)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Add buttons
        self.button1 = tk.Button(
            scrollable_frame,
            text="M/M/1",
            command=self.new_MM1,
        )
        self.button1.pack(pady=20)
        self.button1.config(width=50, height=5)
        self.button1.config(font=("Courier", 15))

        self.button2 = tk.Button(
            scrollable_frame,
            text="M/M/s",
            command=self.loadMMs,
        )
        self.button2.pack(pady=20)
        self.button2.config(width=50, height=5)
        self.button2.config(font=("Courier", 15))

        self.button3 = tk.Button(
            scrollable_frame,
            text="M/M/s/K",
            command=self.loadMMsK,
        )
        self.button3.pack(pady=20)
        self.button3.config(width=50, height=5)
        self.button3.config(font=("Courier", 15))

        self.button4 = tk.Button(
            scrollable_frame,
            text="M/G/1",
            command=self.loadMG1,
        )
        self.button4.pack(pady=20)
        self.button4.config(width=50, height=5)
        self.button4.config(font=("Courier", 15))

        container.pack()
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        # button = Button(window, text="Refresh Screen", command=).place(x=80, y=660, width=300, height=75)

        # self.frame.pack()

    def new_MM1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MM1(self.newWindow)

    def loadMMs(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MMs(self.newWindow)

    def loadMMsK(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MMsK(self.newWindow)

    def loadMG1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = MG1(self.newWindow)


class MM1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x460")
        # Show image using label

        self.label2 = tk.Label(self.master, text="M/M/1")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        self.labelAyuda = tk.Label(
            self.master, text="Procura que la semilla sea de 4 digitos"
        )
        self.labelAyuda.pack(pady=10)
        self.labelAyuda.config(width=200)
        self.labelAyuda.config(font=("Courier", 10))

        # Add buttons
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=200)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=200)

        self.labelnRandom = tk.Label(self.master, text="")
        self.labelnRandom.place(x=10, y=250)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=250)

        # nameEntered.grid(column = 0, row = 1)

        print(self.semillaEntered.get())

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.generar)
        self.button1.place(x=170, y=300)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        # Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generar(self):

        self.mylist.delete(0, END)
        self.cuadrado = CuadradosMedios()
        semilla = self.semillaEntered.get()
        nRandoms = self.nRandomsEntered.get()

        self.cuadrado.ciclo(int(semilla), int(nRandoms))

        print(self.cuadrado.listaRands)

        for i in self.cuadrado.listaRands:
            self.mylist.insert(END, i)

    def close_windows(self):
        self.master.destroy()



class MMs:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x460")
        # Show image using label

        self.label2 = tk.Label(self.master, text="M/M/s")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        self.labelAyuda = tk.Label(
            self.master, text="Procura que la semilla sea de 4 digitos"
        )
        self.labelAyuda.pack(pady=10)
        self.labelAyuda.config(width=200)
        self.labelAyuda.config(font=("Courier", 10))

        # Add buttons
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=200)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=200)

        self.labelnRandom = tk.Label(self.master, text="")
        self.labelnRandom.place(x=10, y=250)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=250)

        # nameEntered.grid(column = 0, row = 1)

        print(self.semillaEntered.get())

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.generar)
        self.button1.place(x=170, y=300)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        # Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generar(self):

        self.mylist.delete(0, END)
        self.cuadrado = CuadradosMedios()
        semilla = self.semillaEntered.get()
        nRandoms = self.nRandomsEntered.get()

        self.cuadrado.ciclo(int(semilla), int(nRandoms))

        print(self.cuadrado.listaRands)

        for i in self.cuadrado.listaRands:
            self.mylist.insert(END, i)

    def close_windows(self):
        self.master.destroy()


class MMsK:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x460")
        # Show image using label

        self.label2 = tk.Label(self.master, text="M/M/s/K")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        self.labelAyuda = tk.Label(
            self.master, text="Procura que la semilla sea de 4 digitos"
        )
        self.labelAyuda.pack(pady=10)
        self.labelAyuda.config(width=200)
        self.labelAyuda.config(font=("Courier", 10))

        # Add buttons
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=200)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=200)

        self.labelnRandom = tk.Label(self.master, text="")
        self.labelnRandom.place(x=10, y=250)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=250)

        # nameEntered.grid(column = 0, row = 1)

        print(self.semillaEntered.get())

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.generar)
        self.button1.place(x=170, y=300)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        # Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generar(self):

        self.mylist.delete(0, END)
        self.cuadrado = CuadradosMedios()
        semilla = self.semillaEntered.get()
        nRandoms = self.nRandomsEntered.get()

        self.cuadrado.ciclo(int(semilla), int(nRandoms))

        print(self.cuadrado.listaRands)

        for i in self.cuadrado.listaRands:
            self.mylist.insert(END, i)

    def close_windows(self):
        self.master.destroy()


class MG1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x460")
        # Show image using label

        self.label2 = tk.Label(self.master, text="M/G/1")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier", 44))

        self.labelAyuda = tk.Label(
            self.master, text="Procura que la semilla sea de 4 digitos"
        )
        self.labelAyuda.pack(pady=10)
        self.labelAyuda.config(width=200)
        self.labelAyuda.config(font=("Courier", 10))

        # Add buttons
        self.labelSmilla = tk.Label(self.master, text="Semilla")
        self.labelSmilla.place(x=10, y=200)
        self.labelSmilla.config(width=30)
        self.labelSmilla.config(font=("Courier", 10))

        self.semilla = ""
        self.semillaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.semilla
        )
        self.semillaEntered.place(x=300, y=200)

        self.labelnRandom = tk.Label(self.master, text="")
        self.labelnRandom.place(x=10, y=250)
        self.labelnRandom.config(width=30)
        self.labelnRandom.config(font=("Courier", 10))

        self.nRandoms = ""
        self.nRandomsEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nRandoms
        )
        self.nRandomsEntered.place(x=300, y=250)

        # nameEntered.grid(column = 0, row = 1)

        print(self.semillaEntered.get())

        self.button1 = tk.Button(
            self.master, text="Generar", command=self.generar)
        self.button1.place(x=170, y=300)
        self.button1.config(width=25, height=2)
        self.button1.config(font=("Courier", 10))

        # Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)

        self.frame.pack()

    def generar(self):

        self.mylist.delete(0, END)
        self.cuadrado = CuadradosMedios()
        semilla = self.semillaEntered.get()
        nRandoms = self.nRandomsEntered.get()

        self.cuadrado.ciclo(int(semilla), int(nRandoms))

        print(self.cuadrado.listaRands)

        for i in self.cuadrado.listaRands:
            self.mylist.insert(END, i)

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    root.geometry("1200x850")

    root.title("Colas")


    label2 = Label(root, text="Sistemas de Colas")
    label2.pack(pady=50)
    label2.config(width=200)
    label2.config(font=("Courier", 44))
    app = Demo1(root)
    root.mainloop()


if __name__ == "__main__":
    main()
