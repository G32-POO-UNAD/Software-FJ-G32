import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import os
from utils.constantes import ARCHIVO_LOG

class LogsView(tk.Toplevel):

    def __init__(self, master=None):

        super().__init__(master)

        self.title("Registro de Eventos y Errores")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(bg="#ECF0F1")

        self.crear_componentes()

        self.cargar_logs()

    def crear_componentes(self):

        titulo = tk.Label(self,text="REGISTRO DE EVENTOS DEL SISTEMA",font=("Arial", 18, "bold"),bg="#ECF0F1",fg="#2C3E50")

        titulo.pack(pady=15)
        
        self.txt_logs = ScrolledText(self,width=110,height=28,font=("Consolas", 10),state="disabled")

        self.txt_logs.pack(padx=20, pady=10)

        frame_botones = tk.Frame(self,bg="#ECF0F1")

        frame_botones.pack(pady=10)

        ttk.Button(frame_botones,text="Actualizar",command=self.cargar_logs,width=15).grid(row=0, column=0, padx=10)

        ttk.Button(frame_botones,text="Limpiar Logs",command=self.limpiar_logs,width=15).grid(row=0, column=1, padx=10)

        ttk.Button(frame_botones,text="Cerrar",command=self.destroy,width=15).grid(row=0, column=2, padx=10)

    def cargar_logs(self):

        self.txt_logs.config(state="normal")
        self.txt_logs.delete("1.0", tk.END)

        if os.path.exists(ARCHIVO_LOG):

            with open(ARCHIVO_LOG, "r", encoding="utf-8") as archivo:

                self.txt_logs.insert(tk.END,archivo.read())

        else:

            self.txt_logs.insert(tk.END,"No existen registros.")

        self.txt_logs.config(state="disabled")

    def limpiar_logs(self):

        with open(ARCHIVO_LOG, "w", encoding="utf-8") as archivo:

            archivo.write("")

        self.cargar_logs()