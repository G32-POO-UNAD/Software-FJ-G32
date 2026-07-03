"""Controlador para gestionar los servicios."""

from tkinter import messagebox

from models.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from data.memoria import servicios
from utils.logger import registrar_info, registrar_error


class ServicioController:

    def __init__(self, vista):

        self.vista = vista

        self.vista.btn_guardar.config(command=self.guardar_servicio)
        self.vista.btn_actualizar.config(command=self.actualizar_servicio)
        self.vista.btn_eliminar.config(command=self.eliminar_servicio)
        self.vista.btn_limpiar.config(command=self.limpiar_campos)

        self.vista.tabla.bind("<<TreeviewSelect>>", self.seleccionar_servicio)

        self.cargar_tabla()
        self.vista.master.dashboard.actualizar_dashboard()
        
    # GUARDAR
    def guardar_servicio(self):

        try:

            tipo = self.vista.tipo.get()

            if tipo == "Reserva de Sala":

                servicio = ReservaSala(self.vista.codigo.get(),float(self.vista.precio.get()),int(self.vista.valor.get()))

            elif tipo == "Alquiler de Equipos":

                servicio = AlquilerEquipo(self.vista.codigo.get(),float(self.vista.precio.get()),int(self.vista.valor.get()))

            elif tipo == "Asesoria Especializada":

                servicio = AsesoriaEspecializada(self.vista.codigo.get(),float(self.vista.precio.get()),int(self.vista.valor.get()))

            else:

                raise ValueError("Seleccione un tipo de servicio.")

            servicios.append(servicio)

            registrar_info("Servicio registrado.")

            messagebox.showinfo("Éxito","Servicio registrado correctamente.")

            self.cargar_tabla()

            self.limpiar_campos()

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error",str(error))
            
    # CARGAR TABLA
    
    def cargar_tabla(self):

        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)

        for servicio in servicios:

            if isinstance(servicio, ReservaSala):
                
                tipo = "Reserva de Sala"
                valor = servicio.capacidad

            elif isinstance(servicio, AlquilerEquipo):
                
                tipo = "Alquiler de Equipos"
                valor = servicio.cantidad

            else:
                
                tipo = "Asesoria Especializada"
                valor = servicio.horas

            self.vista.tabla.insert("", "end",values=(servicio.codigo,servicio.nombre,servicio.precio,valor))
        
    # SELECCIONAR

    def seleccionar_servicio(self, event):

        seleccion = self.vista.tabla.selection()

        if not seleccion:
            return

        valores = self.vista.tabla.item(seleccion[0],"values")

        self.limpiar_campos()

        self.vista.codigo.insert(0, valores[0])
        self.vista.precio.insert(0, valores[2])
        self.vista.valor.insert(0, valores[3])

        self.vista.tipo.set(valores[1])

   
    # ACTUALIZAR

    def actualizar_servicio(self):

        seleccion = self.vista.tabla.selection()

        if not seleccion:

            messagebox.showwarning("Aviso","Seleccione un servicio.")

            return

        indice = self.vista.tabla.index(seleccion[0])

        try:

            tipo = self.vista.tipo.get()

            if tipo == "Reserva de Sala":

                servicio = ReservaSala(self.vista.codigo.get(),float(self.vista.precio.get()),int(self.vista.valor.get()))

            elif tipo == "Alquiler de Equipos":

                servicio = AlquilerEquipo(self.vista.codigo.get(),float(self.vista.precio.get()),int(self.vista.valor.get()))

            else:

                servicio = AsesoriaEspecializada(self.vista.codigo.get(),float(self.vista.precio.get()),int(self.vista.valor.get()))

            servicios[indice] = servicio

            registrar_info("Servicio actualizado.")

            self.cargar_tabla()

            self.limpiar_campos()

            messagebox.showinfo("Éxito","Servicio actualizado.")

        except Exception as error:

            registrar_error(str(error))

            messagebox.showerror("Error", str(error))

  
    # ELIMINAR

    def eliminar_servicio(self):

        seleccion = self.vista.tabla.selection()

        if not seleccion:

            messagebox.showwarning("Aviso","Seleccione un servicio.")

            return

        indice = self.vista.tabla.index(seleccion[0])

        del servicios[indice]

        registrar_info("Servicio eliminado.")

        self.cargar_tabla()

        self.limpiar_campos()

        messagebox.showinfo("Éxito","Servicio eliminado.")


    # LIMPIAR

    def limpiar_campos(self):

        self.vista.codigo.delete(0, "end")
        self.vista.tipo.set("")
        self.vista.precio.delete(0, "end")
        self.vista.valor.delete(0, "end")
        
    