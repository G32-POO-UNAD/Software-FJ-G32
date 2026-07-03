import tkinter as tk

from views.dashboard import Dashboard
from utils.logger import registrar_info, registrar_critico


def main():

    try:

        registrar_info("Sistema Software FJ iniciado.")

        ventana = tk.Tk()

        ventana.dashboard = Dashboard(ventana)

        ventana.mainloop()

    except Exception as error:

        registrar_critico(f"Error crítico al iniciar el sistema: {error}")

        raise


if __name__ == "__main__":
    main()