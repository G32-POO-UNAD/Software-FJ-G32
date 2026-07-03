from tkinter import messagebox

from models.cliente import Cliente
from data.memoria import clientes

from utils.logger import registrar_info, registrar_error


class ClienteController:

    def __init__(self, vista):

        self.vista = vista

        # Asociar botones
        self.vista.btn_guardar.config(command=self.guardar_cliente)
        self.vista.btn_actualizar.config(command=self.actualizar_cliente)
        self.vista.btn_eliminar.config(command=self.eliminar_cliente)
        self.vista.btn_limpiar.config(command=self.limpiar_campos)

        # Evento al seleccionar una fila
        self.vista.tabla.bind("<<TreeviewSelect>>", self.seleccionar_cliente)

        self.cargar_tabla()

   
    # GUARDAR

    def guardar_cliente(self):

        try:

            cliente = Cliente(self.vista.codigo.get(),self.vista.nombre.get(),self.vista.correo.get(),self.vista.telefono.get())

            clientes.append(cliente)

            registrar_info("Cliente registrado.")

            messagebox.showinfo("Éxito","Cliente registrado correctamente.")

            self.cargar_tabla()

            self.limpiar_campos()

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error",str(error))
            
        self.vista.master.dashboard.actualizar_dashboard()


    # CARGAR TABLA
  
    def cargar_tabla(self):

        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)

        for cliente in clientes:

            self.vista.tabla.insert("","end",values=(cliente.codigo,cliente.nombre,cliente.correo,cliente.telefono))


    # SELECCIONAR

    def seleccionar_cliente(self, _event):

        seleccion = self.vista.tabla.selection()

        if not seleccion:
            return

        valores = self.vista.tabla.item(seleccion[0],"values")

        self.limpiar_campos()

        self.vista.codigo.insert(0, valores[0])
        self.vista.nombre.insert(0, valores[1])
        self.vista.correo.insert(0, valores[2])
        self.vista.telefono.insert(0, valores[3])


    # ACTUALIZAR

    def actualizar_cliente(self):

        seleccion = self.vista.tabla.selection()

        if not seleccion:

            messagebox.showwarning("Aviso","Seleccione un cliente.")

            return

        indice = self.vista.tabla.index(seleccion[0])

        try:

            clientes[indice] = Cliente(self.vista.codigo.get(),self.vista.nombre.get(),self.vista.correo.get(),self.vista.telefono.get())

            registrar_info("Cliente actualizado.")

            self.cargar_tabla()

            self.limpiar_campos()

            messagebox.showinfo("Éxito","Cliente actualizado.")

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error",str(error))
            
        self.vista.master.dashboard.actualizar_dashboard()


    # ELIMINAR

    def eliminar_cliente(self):

        seleccion = self.vista.tabla.selection()

        if not seleccion:

            messagebox.showwarning("Aviso","Seleccione un cliente.")

            return

        indice = self.vista.tabla.index(seleccion[0])

        del clientes[indice]

        registrar_info("Cliente eliminado.")

        self.cargar_tabla()

        self.limpiar_campos()

        messagebox.showinfo("Éxito","Cliente eliminado.")
        
        self.vista.master.dashboard.actualizar_dashboard()


    # LIMPIAR

    def limpiar_campos(self):

        self.vista.codigo.delete(0, "end")
        self.vista.nombre.delete(0, "end")
        self.vista.correo.delete(0, "end")
        self.vista.telefono.delete(0, "end")