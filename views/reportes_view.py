import tkinter as tk

from data.memoria import clientes, servicios, reservas
from utils.constantes import (ESTADO_RESERVA_PENDIENTE,ESTADO_RESERVA_CONFIRMADA,ESTADO_RESERVA_CANCELADA)


class ReportesView(tk.Toplevel):

    def __init__(self, master=None):

        super().__init__(master)

        self.title("Reportes")
        self.geometry("500x450")
        self.resizable(False, False)

        self.configure(bg="#ECF0F1")

        self.crear_componentes()

    def crear_componentes(self):

        titulo = tk.Label(self,text="REPORTE GENERAL",font=("Segoe UI",18,"bold"),bg="#ECF0F1",fg="#154360")

        titulo.pack(pady=20)

        pendientes = sum(1 for r in reservas if r.estado == ESTADO_RESERVA_PENDIENTE)

        confirmadas = sum(1 for r in reservas if r.estado == ESTADO_RESERVA_CONFIRMADA)

        canceladas = sum(1 for r in reservas if r.estado == ESTADO_RESERVA_CANCELADA)

        datos = [

            f"Clientes registrados: {len(clientes)}",

            f"Servicios registrados: {len(servicios)}",

            f"Reservas registradas: {len(reservas)}",

            f"Reservas pendientes: {pendientes}",

            f"Reservas confirmadas: {confirmadas}",

            f"Reservas canceladas: {canceladas}"

        ]

        for dato in datos:

            tk.Label(self,text=dato,font=("Segoe UI",13),bg="#ECF0F1").pack(anchor="w", padx=40, pady=10)

        tk.Button(self,text="Cerrar",command=self.destroy).pack(pady=20)