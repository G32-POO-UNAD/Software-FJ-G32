import tkinter as tk
from tkinter import ttk
from controllers.reserva_controller import ReservaController


class ReservaView(tk.Toplevel):

    def __init__(self, master=None):

        super().__init__(master)

        self.title("Gestión de Reservas")
        self.geometry("1000x650")
        self.resizable(False, False)
        self.configure(bg="#ECF0F1")

        self.crear_componentes()

        self.controlador = ReservaController(self)

    # INTERFAZ

    def crear_componentes(self):

        titulo = tk.Label(self,text="GESTIÓN DE RESERVAS",font=("Segoe UI", 20, "bold"),bg="#ECF0F1",fg="#154360")

        titulo.pack(pady=15)

        formulario = tk.LabelFrame(self,text="Datos de la Reserva",font=("Segoe UI", 11, "bold"),padx=15,pady=15)

        formulario.pack(fill="x", padx=20)

        # Código

        tk.Label(formulario,text="Código",font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=8)

        self.codigo = ttk.Entry(formulario, width=30)
        self.codigo.grid(row=0, column=1)

        # Cliente

        tk.Label(formulario,text="Cliente",font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=8)

        self.cliente = ttk.Combobox(formulario,width=28,state="readonly")

        self.cliente.grid(row=1, column=1)

        # Servicio

        tk.Label(formulario,text="Servicio",font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=8)

        self.servicio = ttk.Combobox(formulario,width=28,state="readonly")

        self.servicio.grid(row=2, column=1)

        # Duración

        tk.Label(formulario,text="Duración",font=("Segoe UI", 10)).grid(row=3, column=0, sticky="w", pady=8)

        self.duracion = ttk.Entry(formulario, width=30)
        self.duracion.grid(row=3, column=1)

        # Botones

        frame_botones = tk.Frame(self,bg="#ECF0F1")

        frame_botones.pack(pady=20)

        self.btn_guardar = ttk.Button(frame_botones,text="Guardar",width=15)

        self.btn_guardar.grid(row=0, column=0, padx=10)

        self.btn_actualizar = ttk.Button(frame_botones,text="Confirmar",width=15)

        self.btn_actualizar.grid(row=0, column=1, padx=10)

        self.btn_eliminar = ttk.Button(frame_botones,text="Eliminar",width=15)

        self.btn_eliminar.grid(row=0, column=2, padx=10)

        self.btn_limpiar = ttk.Button(frame_botones, text="Limpiar", width=15,command=self.limpiar)

        self.btn_limpiar.grid(row=0, column=3, padx=10)

        # Tabla

        tabla_frame = tk.Frame(self)

        tabla_frame.pack(fill="both",expand=True,padx=20,pady=10)

        columnas = ("Código","Cliente","Servicio","Duración","Estado")

        self.tabla = ttk.Treeview(tabla_frame,columns=columnas,show="headings",height=12)

        for columna in columnas:

            self.tabla.heading(columna, text=columna)

            self.tabla.column(columna,width=180,anchor="center")

        scrollbar = ttk.Scrollbar(tabla_frame,orient="vertical",command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left",fill="both",expand=True)

        scrollbar.pack(side="right",fill="y")

    # MÉTODOS

    def guardar(self):
        self.controlador.guardar_reserva()

    def actualizar(self):
        self.controlador.confirmar_reserva()

    def eliminar(self):
        self.controlador.cancelar_reserva()

    def limpiar(self):

        self.codigo.delete(0, tk.END)
        self.cliente.set("")
        self.servicio.set("")
        self.duracion.delete(0, tk.END)