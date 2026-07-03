"""Controlador para gestionar las reservas.""" 
from tkinter import messagebox
from models.reserva import Reserva
from data.memoria import clientes, servicios, reservas
from utils.logger import registrar_info, registrar_error


class ReservaController:

    def __init__(self, vista):

        self.vista = vista

        self.vista.btn_guardar.config(command=self.guardar_reserva)
        self.vista.btn_actualizar.config(command=self.confirmar_reserva)
        self.vista.btn_eliminar.config(command=self.cancelar_reserva)
        self.vista.btn_limpiar.config(command=self.limpiar_campos)

        self.vista.tabla.bind("<<TreeviewSelect>>",self.seleccionar_reserva)

        self.cargar_combobox()

        self.cargar_tabla()

  
    # COMBOBOX

    def cargar_combobox(self):

        self.vista.cliente["values"] = [cliente.nombre for cliente in clientes]

        self.vista.servicio["values"] = [servicio.nombre for servicio in servicios]

        if clientes:
            self.vista.cliente.current(0)
            
        if servicios:
            self.vista.servicio.current(0)
                
    # GUARDAR

    def guardar_reserva(self):

        try:

            nombre_cliente = self.vista.cliente.get()

            nombre_servicio = self.vista.servicio.get()

            cliente = next((c for c in clientes if c.nombre == nombre_cliente),None)

            servicio = next((s for s in servicios if s.nombre == nombre_servicio),None)

            if cliente is None:
                raise ValueError("Debe seleccionar un cliente válido.")

            if servicio is None:
                raise ValueError("Debe seleccionar un servicio válido.")

            reserva = Reserva(self.vista.codigo.get(),cliente,servicio,int(self.vista.duracion.get()))

            # Confirmar antes de guardar
            if not messagebox.askyesno("Confirmar","¿Desea confirmar la reserva?"):
                return

            reservas.append(reserva)

            registrar_info("Reserva registrada.")

            messagebox.showinfo("Éxito","Reserva registrada correctamente.")

            self.cargar_tabla()

            self.limpiar_campos()

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error",str(error))
            
        self.vista.master.dashboard.actualizar_dashboard()


    # TABLA

    def cargar_tabla(self):

        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)

        for reserva in reservas:

            self.vista.tabla.insert("","end",values=(reserva.codigo,reserva.cliente.nombre,reserva.servicio.nombre,reserva.duracion,reserva.estado))


    # SELECCIONAR

    def seleccionar_reserva(self, event):

        seleccion = self.vista.tabla.selection()

        if not seleccion:
            return

        valores = self.vista.tabla.item(seleccion[0],"values")

        self.limpiar_campos()

        self.vista.codigo.insert(0,valores[0])

        self.vista.cliente.set(valores[1])

        self.vista.servicio.set(valores[2])

        self.vista.duracion.insert(0,valores[3])


    # ACTUALIZAR

    def confirmar_reserva(self):

        seleccion = self.vista.tabla.selection()

        if not seleccion:

            messagebox.showwarning("Aviso","Seleccione una reserva.")

            return

        indice = self.vista.tabla.index(seleccion[0])

        try:

            reservas[indice].confirmar()

            registrar_info("Reserva confirmada.")

            self.cargar_tabla()

            self.limpiar_campos()

            messagebox.showinfo("Éxito","Reserva confirmada correctamente.")

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error",str(error))
            
        self.vista.master.dashboard.actualizar_dashboard()


    # CANCELAR RESERVA

    def cancelar_reserva(self):

        seleccion = self.vista.tabla.selection()

        if not seleccion:

            messagebox.showwarning("Aviso","Seleccione una reserva.")

            return

        indice = self.vista.tabla.index(seleccion[0])

        try:

            reservas[indice].cancelar()

            del reservas[indice]

            registrar_info("Reserva eliminada.")

            self.cargar_tabla()

            self.limpiar_campos()

            messagebox.showinfo("Éxito","Reserva cancelada y eliminada.")

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error", str(error))

        registrar_info("Reserva eliminada.")

        self.cargar_tabla()

        self.limpiar_campos()

        messagebox.showinfo("Éxito","Reserva eliminada.")
        
        self.vista.master.dashboard.actualizar_dashboard()


    # LIMPIAR

    def limpiar_campos(self):

        self.vista.codigo.delete(0, "end")
        self.vista.cliente.set("")
        self.vista.servicio.set("")
        self.vista.duracion.delete(0, "end")