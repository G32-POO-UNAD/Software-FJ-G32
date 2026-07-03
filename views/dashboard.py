import tkinter as tk
from tkinter import ttk
from views.cliente_view import ClienteView
from views.servicio_view import ServicioView
from views.reserva_view import ReservaView
from views.logs_view import LogsView
from data.memoria import clientes, servicios, reservas
from views.reportes_view import ReportesView

class Dashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Software FJ - Sistema Integral de Gestión")
        self.root.geometry("1300x750")
        self.root.configure(bg="#ECF0F1")
        self.root.resizable(False, False)

        self.crear_header()
        self.crear_menu()
        self.crear_panel()


    # BARRA SUPERIOR
  
    def crear_header(self):

        self.header = tk.Frame(self.root,bg="#154360",height=70)

        self.header.pack(fill="x")

        titulo = tk.Label(self.header,text="SOFTWARE FJ",font=("Segoe UI", 24, "bold"),fg="white",bg="#154360")

        titulo.pack(side="left", padx=30, pady=15)

        subtitulo = tk.Label(self.header,text="Sistema Integral de Gestión",font=("Segoe UI", 12),fg="white",bg="#154360")

        subtitulo.pack(side="right", padx=30)

    # ABRIR VENTANAS

    def abrir_clientes(self):
        
        ventana = ClienteView(self.root)
        ventana.grab_set()

    def abrir_servicios(self):
        
       ventana = ServicioView(self.root)
       ventana.grab_set()

    def abrir_reservas(self):
        
        ventana = ReservaView(self.root)
        ventana.grab_set()
        
    def abrir_reportes(self):

        ventana = ReportesView(self.root)
        ventana.grab_set()
        
    def abrir_logs(self):

        ventana = LogsView(self.root)

        ventana.grab_set()

    # MENÚ LATERAL
   
    def crear_menu(self):

        self.menu = tk.Frame(self.root,bg="#1F2D3D",width=220)

        self.menu.pack(side="left", fill="y")

        opciones = [
            ("🏠 Dashboard", None),
            ("👤 Clientes", self.abrir_clientes),
            ("🛠 Servicios", self.abrir_servicios),
            ("📅 Reservas", self.abrir_reservas),
            ("📊 Reportes", self.abrir_reportes),
            ("⚠ Logs", self.abrir_logs),
            ("🚪 Salir", self.root.destroy)
        ]

        for texto, comando in opciones:
            boton = tk.Button(self.menu,text=texto,font=("Segoe UI", 12),bg="#1F2D3D",fg="white",relief="flat",cursor="hand2",activebackground="#2E4053",activeforeground="white",height=2,command=comando)

            boton.pack(fill="x", padx=10, pady=5)

    
    # PANEL CENTRAL

    def crear_panel(self):

        self.panel = tk.Frame(self.root,bg="#ECF0F1")

        self.panel.pack(expand=True, fill="both")

        bienvenida = tk.Label(self.panel,text="Bienvenido al Sistema Software FJ",font=("Segoe UI", 22, "bold"),bg="#ECF0F1")

        bienvenida.pack(pady=20)

        descripcion = tk.Label(self.panel,text="Panel de administración",font=("Segoe UI", 12),bg="#ECF0F1")

        descripcion.pack()
 
        # TARJETAS
  
        tarjetas = tk.Frame(self.panel,bg="#ECF0F1")

        tarjetas.pack(pady=40)

        datos = ["Clientes","Servicios","Reservas","Pendientes"]

        for titulo in datos:

            tarjeta = tk.Frame(tarjetas,width=180,height=120,bg="white",relief="ridge",bd=2)

            tarjeta.pack(side="left", padx=20)

            tarjeta.pack_propagate(False)

            tk.Label(tarjeta,text=titulo,font=("Segoe UI", 14, "bold"),bg="white").pack(pady=10)

            if titulo == "Clientes":

                self.lbl_clientes = tk.Label(tarjeta,text="0",font=("Segoe UI", 28, "bold"),fg="#154360",bg="white")
                self.lbl_clientes.pack()

            elif titulo == "Servicios":

                self.lbl_servicios = tk.Label(tarjeta,text="0",font=("Segoe UI", 28, "bold"),fg="#154360",bg="white")
                self.lbl_servicios.pack()

            elif titulo == "Reservas":

                self.lbl_reservas = tk.Label(tarjeta,text="0",font=("Segoe UI", 28, "bold"),fg="#154360",bg="white")
                self.lbl_reservas.pack()

            else:

                self.lbl_pendientes = tk.Label(tarjeta,text="0",font=("Segoe UI", 28, "bold"),fg="#154360",bg="white")
                self.lbl_pendientes.pack()
            
          

     
        # TABLA
  
        frame_tabla = tk.Frame(self.panel,bg="#ECF0F1")

        frame_tabla.pack(fill="both", expand=True, padx=20, pady=20)

        columnas = ("Código","Cliente","Servicio","Estado")

        
        self.tabla = ttk.Treeview(frame_tabla,columns=columnas,show="headings",height=12)

        for columna in columnas:

            self.tabla.heading(columna, text=columna)

            self.tabla.column(columna,width=180,anchor="center")

        self.tabla.pack(fill="both", expand=True)
        
        self.actualizar_dashboard()
        
    def actualizar_dashboard(self): 
        
        self.lbl_clientes.config(text=str(len(clientes))) 
        self.lbl_servicios.config(text=str(len(servicios))) 
        self.lbl_reservas.config(text=str(len(reservas))) 
        
        pendientes = 0 
        
        for reserva in reservas: 
            if reserva.estado != "Confirmada": pendientes += 1 
            self.lbl_pendientes.config(text=str(pendientes)) 
            
        for fila in self.tabla.get_children(): 
            self.tabla.delete(fila) 
            
        for reserva in reservas: 
            self.tabla.insert( "", "end", values=( reserva.codigo, reserva.cliente.nombre, reserva.servicio.nombre, reserva.estado ) )