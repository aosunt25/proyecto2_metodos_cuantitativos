import math
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from modelo_m_m_1 import ModeloMMUno
from modelo_m_m_s import ModeloMMS
from modelo_m_g_1 import ModeloMG1
from modelo_m_m_s_k import ModeloMMSK

# importar modelos


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
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
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
        self.label2.config(font=("Courier", 23))

        self.labelLambda = tk.Label(self.master, text="Tasa media de llegadas")
        self.labelLambda.place(x=10, y=100)
        self.labelLambda.config(width=30)
        self.labelLambda.config(font=("Courier", 10))

        self.nLambda = ""
        self.nLambdaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nLambda
        )
        self.nLambdaEntered.place(x=300, y=100)

        self.labelMiu = tk.Label(self.master, text="Tasa media de servicio")
        self.labelMiu.place(x=10, y=150)
        self.labelMiu.config(width=30)
        self.labelMiu.config(font=("Courier", 10))

        self.nMiu = ""
        self.nMiuEntered = ttk.Entry(self.master, width=40, textvariable=self.nMiu)
        self.nMiuEntered.place(x=300, y=150)

        self.labelN = tk.Label(self.master, text="P(n) clientes en el sistema ")
        self.labelN.place(x=10, y=200)
        self.labelN.config(width=30)
        self.labelN.config(font=("Courier", 10))

        self.nN = ""
        self.nNEntered = ttk.Entry(self.master, width=40, textvariable=self.nN)
        self.nNEntered.place(x=300, y=200)

        self.labelCT = tk.Label(self.master, text="Costo por tiempo espera ")
        self.labelCT.place(x=10, y=300)
        self.labelCT.config(width=30)
        self.labelCT.config(font=("Courier", 10))

        self.nCT = ""
        self.nCTEntered = ttk.Entry(self.master, width=40, textvariable=self.nCT)
        self.nCTEntered.place(x=300, y=300)

        self.labelCS = tk.Label(self.master, text="Costo servicio ")
        self.labelCS.place(x=10, y=350)
        self.labelCS.config(width=30)
        self.labelCS.config(font=("Courier", 10))

        self.CS = ""
        self.nCSEntered = ttk.Entry(self.master, width=40, textvariable=self.CS)
        self.nCSEntered.place(x=300, y=350)

        self.button1 = tk.Button(self.master, text="Calcular", command=self.generar)

        self.button1.place(x=170, y=400)
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

        nLambda = int(self.nLambdaEntered.get())
        nMiu = int(self.nMiuEntered.get())

        cE = int(self.nCTEntered.get())
        cS = int(self.nCSEntered.get())

        if self.nNEntered.get() != "":
            nN = int(self.nNEntered.get())
        else:
            nN = 0

        modelo = ModeloMMUno(nLambda, nMiu, nN)

        if nLambda < nMiu:
            costoTotal =((modelo.calcularLq() * cE) + cS * 1, 2)

            ro = "Factor de utilizacion " + str(modelo.factor_de_uso)
            Pc = "P0 : " + str(modelo.calcularPcero())
            Pn = "Pn : " + str(modelo.calcularPn())
            # Cn = "Cn : " + str(modelo.calcularCN(
            Lq = "Lq : " + str(modelo.calcularLq()) + " clientes"
            L = "L : " + str(modelo.calcularL()) + " clientes"
            Wq = "Wq : " + str(modelo.calcularWq()) + " horas"
            W = "W : " + str(modelo.calcularW()) + " horas"
            Costo = "Costo : $" + str(costoTotal)

            self.mylist.insert(END, ro)
            self.mylist.insert(END, Pc)
            self.mylist.insert(END, Pn)
            # self.mylist.insert(END, Cn)
            self.mylist.insert(END, Lq)
            self.mylist.insert(END, L)
            self.mylist.insert(END, Wq)
            self.mylist.insert(END, W)
            self.mylist.insert(END, Costo)
        else:
            self.mylist.insert(
                END,
                "La media de llegadas tiene que ser mayor a la tasa media de servicios",
            )

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
        self.label2.config(font=("Courier", 23))

        # Add buttons
        # clientes, lambdaM, miu, n

        self.labelServidores = tk.Label(self.master, text="Servidores")
        self.labelServidores.place(x=10, y=100)
        self.labelServidores.config(width=30)
        self.labelServidores.config(font=("Courier", 10))

        self.servidores = ""
        self.servidoresEntered = ttk.Entry(
            self.master, width=40, textvariable=self.servidores
        )
        self.servidoresEntered.place(x=300, y=100)

        self.labelLambda = tk.Label(self.master, text="Tasa media de llegadas")
        self.labelLambda.place(x=10, y=150)
        self.labelLambda.config(width=30)
        self.labelLambda.config(font=("Courier", 10))

        self.nLambda = ""
        self.nLambdaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nLambda
        )
        self.nLambdaEntered.place(x=300, y=150)

        self.labelMiu = tk.Label(self.master, text="Tasa media de servicio")
        self.labelMiu.place(x=10, y=200)
        self.labelMiu.config(width=30)
        self.labelMiu.config(font=("Courier", 10))

        self.nMiu = ""
        self.nMiuEntered = ttk.Entry(self.master, width=40, textvariable=self.nMiu)
        self.nMiuEntered.place(x=300, y=200)

        self.labelN = tk.Label(self.master, text="P(n) clientes en el sistema ")
        self.labelN.place(x=10, y=250)
        self.labelN.config(width=30)
        self.labelN.config(font=("Courier", 10))

        self.nN = ""
        self.nNEntered = ttk.Entry(self.master, width=40, textvariable=self.nN)
        self.nNEntered.place(x=300, y=250)

        self.labelCT = tk.Label(self.master, text="Costo por tiempo espera ")
        self.labelCT.place(x=10, y=300)
        self.labelCT.config(width=30)
        self.labelCT.config(font=("Courier", 10))

        self.nCT = ""
        self.nCTEntered = ttk.Entry(self.master, width=40, textvariable=self.nCT)
        self.nCTEntered.place(x=300, y=300)

        self.labelCS = tk.Label(self.master, text="Costo servicio ")
        self.labelCS.place(x=10, y=350)
        self.labelCS.config(width=30)
        self.labelCS.config(font=("Courier", 10))

        self.CS = ""
        self.nCSEntered = ttk.Entry(self.master, width=40, textvariable=self.CS)
        self.nCSEntered.place(x=300, y=350)

        self.button1 = tk.Button(self.master, text="Calcular", command=self.generar)

        self.button1.place(x=170, y=400)
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
        cE = int(self.nCTEntered.get())
        cS = int(self.nCSEntered.get())
        servidores = int(self.servidoresEntered.get())
        nLambda = int(self.nLambdaEntered.get())
        nMiu = int(self.nMiuEntered.get())

        if self.nNEntered.get() != "":
            nN = int(self.nNEntered.get())
        else:
            nN = 0

        modelo = ModeloMMS(servidores, nLambda, nMiu, nN)

        print(servidores)

        if nLambda < nMiu:
            ro = "Factor de utilizacion " + str(modelo.factor_de_uso)
            Pc = "P0 : " + str(modelo.calcularPcero())
            Pn = "Pn : " + str(modelo.calcularPn())
            Lq = "Lq : " + str(modelo.calcularLq()) + " clientes"
            L = "L : " + str(modelo.calcularL()) + " clientes"
            Wq = "Wq : " + str(modelo.calcularWq()) + " horas"
            W = "W : " + str(modelo.calcularW()) + " horas"

            print(cE)
            print(Lq)
            costoTotal =(
                ((modelo.calcularLq() * cE) + (cS * servidores)), 2
            )
            print(modelo.calcularLq())
            print(costoTotal)
            Costo = "Costo : $" + str(costoTotal)

            self.mylist.insert(END, ro)
            self.mylist.insert(END, Pc)
            self.mylist.insert(END, Pn)
            self.mylist.insert(END, Lq)
            self.mylist.insert(END, L)
            self.mylist.insert(END, Wq)
            self.mylist.insert(END, W)

            self.mylist.insert(END, Costo)

        else:
            self.mylist.insert(
                END,
                "La media de llegadas tiene que ser mayor a la tasa media de servicios",
            )

    def close_windows(self):
        self.master.destroy()


class MMsK:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1200x600")
        # Show image using label

        self.label2 = tk.Label(self.master, text="M/M/s/K")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier",23))
        # Add buttons
        # clientes, lambdaM, miu, n

        self.labelServidores = tk.Label(self.master, text="Servidores")
        self.labelServidores.place(x=10, y=100)
        self.labelServidores.config(width=30)
        self.labelServidores.config(font=("Courier", 10))

        self.servidores = ""
        self.servidoresEntered = ttk.Entry(
            self.master, width=40, textvariable=self.servidores
        )
        self.servidoresEntered.place(x=300, y=100)

        self.labelLambda = tk.Label(self.master, text="Tasa media de llegadas")
        self.labelLambda.place(x=10, y=150)
        self.labelLambda.config(width=30)
        self.labelLambda.config(font=("Courier", 10))

        self.nLambda = ""
        self.nLambdaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nLambda
        )
        self.nLambdaEntered.place(x=300, y=150)

        self.labelMiu = tk.Label(self.master, text="Tasa media de servicio")
        self.labelMiu.place(x=10, y=200)
        self.labelMiu.config(width=30)
        self.labelMiu.config(font=("Courier", 10))

        self.nMiu = ""
        self.nMiuEntered = ttk.Entry(self.master, width=40, textvariable=self.nMiu)
        self.nMiuEntered.place(x=300, y=200)

        self.labelN = tk.Label(self.master, text="P(n) clientes en el sistema ")
        self.labelN.place(x=10, y=250)
        self.labelN.config(width=30)
        self.labelN.config(font=("Courier", 10))

        self.nN = ""
        self.nNEntered = ttk.Entry(self.master, width=40, textvariable=self.nN)
        self.nNEntered.place(x=300, y=250)

        self.labelK = tk.Label(self.master, text="Limite de clientes en la cola(K)")
        self.labelK.place(x=10, y=300)
        self.labelK.config(width=30)
        self.labelK.config(font=("Courier", 10))

        self.nK = ""
        self.nKEntered = ttk.Entry(self.master, width=40, textvariable=self.nN)
        self.nKEntered.place(x=300, y=300)

        self.labelCT = tk.Label(self.master, text="Costo por tiempo espera ")
        self.labelCT.place(x=10, y=350)
        self.labelCT.config(width=30)
        self.labelCT.config(font=("Courier", 10))

        self.nCT = ""
        self.nCTEntered = ttk.Entry(self.master, width=40, textvariable=self.nCT)
        self.nCTEntered.place(x=300, y=350)

        self.labelCS = tk.Label(self.master, text="Costo servicio ")
        self.labelCS.place(x=10, y=400)
        self.labelCS.config(width=30)
        self.labelCS.config(font=("Courier", 10))

        self.CS = ""
        self.nCSEntered = ttk.Entry(self.master, width=40, textvariable=self.CS)
        self.nCSEntered.place(x=300, y=400)

        self.button1 = tk.Button(self.master, text="Calcular", command=self.generar)

        self.button1.place(x=170, y=500)
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
        cE = int(self.nCTEntered.get())
        cS = int(self.nCSEntered.get())
        k = int(self.nKEntered.get())
        servidores = int(self.servidoresEntered.get())
        nLambda = int(self.nLambdaEntered.get())
        nMiu = int(self.nMiuEntered.get())

        if self.nNEntered.get() != "":
            nN = int(self.nNEntered.get())
        else:
            nN = 0
        if nLambda < nMiu:

            modelo = ModeloMMSK(servidores, nLambda, nMiu, nN, k)

            print(servidores)

            ro = "Factor de utilizacion " + str(modelo.factor_de_uso)
            Pc = "P0 : " + str(modelo.P0())
            Pn = "Pn : " + str(modelo.Pn())
            Lq = "Lq : " + str(modelo.Lq()) + " clientes"
            L = "L : " + str(modelo.L()) + " clientes"
            Le = "Le: " + str(modelo.Le()) + " clientes"
            Wq = "Wq : " + str(modelo.Wq()) + " horas"
            W = "W : " + str(modelo.W()) + " horas"

            print(cE)
            print(Lq)
            costoTotal =(((modelo.Lq() * cE) + (cS * servidores)), 2)
            print(modelo.Lq())
            print(costoTotal)
            Costo = "Costo : $" + str(costoTotal)

            self.mylist.insert(END, ro)
            self.mylist.insert(END, Pc)
            self.mylist.insert(END, Pn)
            self.mylist.insert(END, Lq)
            self.mylist.insert(END, Le)
            self.mylist.insert(END, L)
            self.mylist.insert(END, Wq)
            self.mylist.insert(END, W)

            self.mylist.insert(END, Costo)
        else:
            self.mylist.insert(
                END,
                "La media de llegadas tiene que ser mayor a la tasa media de servicios",
            )

    def close_windows(self):
        self.master.destroy()


class MG1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.bg = PhotoImage(file="fondo.gif")

        self.master.geometry("1100x720")
        # Show image using label

        self.label2 = tk.Label(self.master, text="M/G/1 o M/D/1")
        self.label2.pack(pady=25)
        self.label2.config(width=200)
        self.label2.config(font=("Courier",23))

        # Buttons
        self.labelLambda = tk.Label(self.master, text="Tasa media de llegadas")
        self.labelLambda.place(x=10, y=200)
        self.labelLambda.config(width=30)
        self.labelLambda.config(font=("Courier", 10))

        self.nLambda = ""
        self.nLambdaEntered = ttk.Entry(
            self.master, width=40, textvariable=self.nLambda
        )
        self.nLambdaEntered.place(x=300, y=200)

        self.labelMiu = tk.Label(self.master, text="Tasa media de servicio")
        self.labelMiu.place(x=10, y=250)
        self.labelMiu.config(width=30)
        self.labelMiu.config(font=("Courier", 10))

        self.nMiu = ""
        self.nMiuEntered = ttk.Entry(self.master, width=40, textvariable=self.nMiu)
        self.nMiuEntered.place(x=300, y=250)

        self.labelN = tk.Label(self.master, text="P(n) clientes en el sistema ")
        self.labelN.place(x=10, y=300)
        self.labelN.config(width=30)
        self.labelN.config(font=("Courier", 10))

        self.nN = ""
        self.nNEntered = ttk.Entry(self.master, width=40, textvariable=self.nN)
        self.nNEntered.place(x=300, y=300)

        self.labelDes = tk.Label(self.master, text="Desviación estándar ")
        self.labelDes.place(x=10, y=350)
        self.labelDes.config(width=30)
        self.labelDes.config(font=("Courier", 10))

        self.nDes = ""
        self.nDesEntered = ttk.Entry(self.master, width=40, textvariable=self.nN)
        self.nDesEntered.place(x=300, y=350)

        self.labelCT = tk.Label(self.master, text="Costo por tiempo espera ")
        self.labelCT.place(x=10, y=400)
        self.labelCT.config(width=30)
        self.labelCT.config(font=("Courier", 10))

        self.nCT = ""
        self.nCTEntered = ttk.Entry(self.master, width=40, textvariable=self.nCT)
        self.nCTEntered.place(x=300, y=400)

        self.labelCS = tk.Label(self.master, text="Costo servicio ")
        self.labelCS.place(x=10, y=450)
        self.labelCS.config(width=30)
        self.labelCS.config(font=("Courier", 10))

        self.CS = ""
        self.nCSEntered = ttk.Entry(self.master, width=40, textvariable=self.CS)
        self.nCSEntered.place(x=300, y=450)

        self.button1 = tk.Button(self.master, text="Calcular", command=self.generar)

        self.button1.place(x=170, y=500)
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

        nLambda = int(self.nLambdaEntered.get())
        nMiu = float(self.nMiuEntered.get())
        nDes = float(self.nDesEntered.get())
        cE = int(self.nCTEntered.get())
        cS = int(self.nCSEntered.get())

        if self.nNEntered.get() != "":
            nN = int(self.nNEntered.get())
        else:
            nN = 0

        if nDes < 0:
            self.mylist.insert(
                END,
                "La desviación estándar tiene que ser positiva",
            )

            
            

        else:
            if nLambda < nMiu:
                modelo = ModeloMG1(nLambda, nMiu, nN, nDes)
                costoTotal =((modelo.calcularLq() * cE) + cS * 1, 2)

                ro = "Factor de utilizacion " + str(modelo.factor_de_uso)
                Pc = "P0 : " + str(modelo.calcularPcero())
                Pn = "Pn : " + str(modelo.calcularPn())
                # Cn = "Cn : " + str(modelo.calcularCN())
                Lq = "Lq : " + str(modelo.calcularLq()) + " clientes"
                L = "L : " + str(modelo.calcularL()) + " clientes"
                Wq = "Wq : " + str(modelo.calcularWq()) + " horas"
                W = "W : " + str(modelo.calcularW()) + " horas"
                Costo = "Costo : $" + str(costoTotal)

                if (nDes == 0):
                    self.mylist.insert(END, "Estás usando las fórmulas de MD1")

                self.mylist.insert(END, "Estás usando las fórmulas de MG1")
                self.mylist.insert(END, ro)
                self.mylist.insert(END, Pc)
                self.mylist.insert(END, Pn)
                # self.mylist.insert(END, Cn)
                self.mylist.insert(END, Lq)
                self.mylist.insert(END, L)
                self.mylist.insert(END, Wq)
                self.mylist.insert(END, W)
                self.mylist.insert(END, Costo)
            else:
                self.mylist.insert(
                    END,
                    "La media de llegadas tiene que ser mayor a la tasa media de servicios",
                )

    def close_windows(self):
        self.master.destroy()

        # Scroll Bar

        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.master, yscrollcommand=scrollbar.set)

        self.mylist.pack(side=RIGHT, fill=BOTH)
        self.mylist.place(x=700, y=200)
        self.mylist.config(width=30, height=20)
        scrollbar.config(command=self.mylist.yview)


def main():
    root = tk.Tk()
    root.geometry("1200x850")

    root.title("Colas")

    label2 = Label(root, text="Sistemas de Colas")
    label2.pack(pady=50)
    label2.config(width=200)
    label2.config(font=("Courier",23))
    app = Demo1(root)
    root.mainloop()


if __name__ == "__main__":
    main()
