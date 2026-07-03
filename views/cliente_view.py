import tkinter as tk
from tkinter import ttk
from controllers.cliente_controller import ClienteController

class ClienteView(tk.Toplevel):

    def __init__(self, master=None):
        
        super().__init__(master)
        
        
        self.title("Gestión de Clientes")
        self.geometry("1000x650")
        self.resizable(False, False)

        self.configure(bg="#ECF0F1")

        self.crear_componentes()
        
        self.controlador = ClienteController(self)

 
    # INTERFAZ

    def crear_componentes(self):

        titulo = tk.Label(self,text="GESTIÓN DE CLIENTES",font=("Segoe UI", 20, "bold"),bg="#ECF0F1",fg="#154360")

        titulo.pack(pady=15)


        # Frame del formulario

        formulario = tk.LabelFrame(self,text="Datos del Cliente",font=("Segoe UI", 11, "bold"),padx=15,pady=15)

        formulario.pack(fill="x", padx=20)

        # Código

        tk.Label(formulario,text="Código",font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=8)

        self.codigo = ttk.Entry(formulario, width=30)
        self.codigo.grid(row=0, column=1)

        # Nombre

        tk.Label(formulario,text="Nombre",font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=8)

        self.nombre = ttk.Entry(formulario, width=30)
        self.nombre.grid(row=1, column=1)

        # Correo

        tk.Label(formulario,text="Correo",font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=8)

        self.correo = ttk.Entry(formulario, width=30)
        self.correo.grid(row=2, column=1)

        # Teléfono

        tk.Label(formulario,text="Teléfono",font=("Segoe UI", 10)).grid(row=3, column=0, sticky="w", pady=8)

        self.telefono = ttk.Entry(formulario, width=30)
        self.telefono.grid(row=3, column=1)

        
        # Botones
     
        frame_botones = tk.Frame(self, bg="#ECF0F1")
        frame_botones.pack(pady=20)

        self.btn_guardar = ttk.Button(frame_botones,text="Guardar",width=15)
        self.btn_guardar.grid(row=0, column=0, padx=10)

        self.btn_actualizar = ttk.Button(frame_botones,text="Actualizar",width=15)
        self.btn_actualizar.grid(row=0, column=1, padx=10)

        self.btn_eliminar = ttk.Button(frame_botones,text="Eliminar",width=15)
        self.btn_eliminar.grid(row=0, column=2, padx=10)

        self.btn_limpiar = ttk.Button(frame_botones,text="Limpiar",width=15,command=self.limpiar)
        self.btn_limpiar.grid(row=0, column=3, padx=10)
        
        
        # Tabla

        tabla_frame = tk.Frame(self)
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columnas = ("Código","Nombre","Correo","Teléfono")

        self.tabla = ttk.Treeview(tabla_frame,columns=columnas,show="headings",height=12)

        for columna in columnas:

            self.tabla.heading(columna, text=columna)

            self.tabla.column(columna,width=200,anchor="center")

        scrollbar = ttk.Scrollbar(tabla_frame,orient="vertical",command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)

        scrollbar.pack(side="right", fill="y")


    # MÉTODOS 

    def guardar(self):
        self.controlador.guardar_cliente()

    def actualizar(self):
        self.controlador.actualizar_cliente()

    def eliminar(self):
        self.controlador.eliminar_cliente()

    def limpiar(self):

        self.codigo.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.correo.delete(0, tk.END)
        self.telefono.delete(0, tk.END)