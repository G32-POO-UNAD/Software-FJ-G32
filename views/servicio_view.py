import tkinter as tk
from tkinter import ttk

from controllers.servicio_controller import ServicioController


class ServicioView(tk.Toplevel):

    def __init__(self, master=None):

        super().__init__(master)

        self.title("Gestión de Servicios")
        self.geometry("1000x650")
        self.resizable(False, False)
        self.configure(bg="#ECF0F1")

        self.crear_componentes()

        self.controlador = ServicioController(self)

    # INTERFAZ

    def crear_componentes(self):

        titulo = tk.Label(self,text="GESTIÓN DE SERVICIOS",font=("Segoe UI",20,"bold"),bg="#ECF0F1",fg="#154360")

        titulo.pack(pady=15)

        formulario = tk.LabelFrame(self,text="Datos del Servicio",font=("Segoe UI",11,"bold"),padx=15,pady=15)
        formulario.pack(fill="x", padx=20)

        # Código

        tk.Label(formulario,text="Código",font=("Segoe UI",10)).grid(row=0,column=0,sticky="w",pady=8)

        self.codigo = ttk.Entry(formulario,width=30)
        self.codigo.grid(row=0,column=1)

        # Tipo

        tk.Label(formulario,text="Tipo",font=("Segoe UI",10)).grid(row=1,column=0,sticky="w",pady=8)

        self.tipo = ttk.Combobox(formulario,values=["Reserva de Sala","Alquiler de Equipos","Asesoría Especializada"],state="readonly",width=28)

        self.tipo.grid(row=1,column=1) 
        self.tipo.current(0) 
        self.tipo.bind("<<ComboboxSelected>>", self.cambiar_etiqueta)
        
        # Precio

        tk.Label(formulario,text="Precio",font=("Segoe UI",10)).grid(row=2,column=0,sticky="w",pady=8)

        self.precio = ttk.Entry(formulario,width=30)
        self.precio.grid(row=2,column=1)

        # Capacidad / Cantidad / Horas

        self.lbl_valor = tk.Label(formulario,text="Capacidad",font=("Segoe UI",10))

        self.lbl_valor.grid(row=3,column=0,sticky="w",pady=8)
        
        self.valor = ttk.Entry(formulario,width=30)
        self.valor.grid(row=3,column=1)
        
        # Botones

        frame_botones = tk.Frame(self,bg="#ECF0F1")
        frame_botones.pack(pady=20)

        self.btn_guardar = ttk.Button(frame_botones,text="Guardar",width=15)
        self.btn_guardar.grid(row=0,column=0,padx=10)

        self.btn_actualizar = ttk.Button(frame_botones,text="Actualizar",width=15)
        self.btn_actualizar.grid(row=0,column=1,padx=10)

        self.btn_eliminar = ttk.Button(frame_botones,text="Eliminar",width=15)
        self.btn_eliminar.grid(row=0,column=2,padx=10)

        self.btn_limpiar = ttk.Button(frame_botones,text="Limpiar",width=15,command=self.limpiar)
        self.btn_limpiar.grid(row=0,column=3,padx=10)

        # Tabla

        tabla_frame = tk.Frame(self)
        tabla_frame.pack(fill="both",expand=True,padx=20,pady=10)

        columnas = ("Código","Tipo","Precio","Valor")

        self.tabla = ttk.Treeview(tabla_frame,columns=columnas,show="headings",height=12)

        for columna in columnas:

            self.tabla.heading(columna,text=columna)

            self.tabla.column(columna,width=220,anchor="center")

        scrollbar = ttk.Scrollbar(tabla_frame,orient="vertical",command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left",fill="both",expand=True)

        scrollbar.pack(side="right",fill="y")

    # MÉTODOS

    def guardar(self):
        self.controlador.guardar_servicio()

    def actualizar(self):
        self.controlador.actualizar_servicio()

    def eliminar(self):
        self.controlador.eliminar_servicio()

    def limpiar(self):

        self.codigo.delete(0,tk.END)
        self.tipo.set("")
        self.precio.delete(0,tk.END)
        self.valor.delete(0,tk.END)
        
    def cambiar_etiqueta(self, event=None):

        tipo = self.tipo.get()

        if tipo == "Reserva de Sala":

            self.lbl_valor.config(text="Capacidad")

        elif tipo == "Alquiler de Equipos":

            self.lbl_valor.config(text="Cantidad")

        elif tipo == "Asesoría Especializada":

            self.lbl_valor.config(text="Horas")
            
        self.valor.delete(0, tk.END)
    
