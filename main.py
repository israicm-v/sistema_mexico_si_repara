import tkinter as tk
from tkinter import messagebox, ttk
from init_db import SistemaReparaciones

class InterfazGrafica:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Reparaciones")
        self.root.geometry("600x400")
        self.crear_menu()

    def crear_menu(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(pady=20)

        titulo = tk.Label(frame, text="Sistema de Reparaciones", font=("Helvetica", 20, "bold"))
        titulo.pack(pady=20)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)

        ttk.Button(frame, text="Registrar Cliente", command=self.registrar_cliente).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Crear Ticket", command=self.crear_ticket).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Ver Tickets de Cliente", command=self.ver_tickets_cliente).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Cambiar Estatus de Ticket", command=self.cambiar_estatus_ticket).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Ver Clientes", command=self.ver_clientes).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Buscar Cliente", command=self.buscar_cliente).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Buscar Ticket", command=self.buscar_ticket).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Generar Reporte", command=self.generar_reporte).pack(fill=tk.X, pady=10)
        ttk.Button(frame, text="Salir", command=self.root.quit).pack(fill=tk.X, pady=10)

    def registrar_cliente(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Cliente")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="Nombre:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        nombre_entry = ttk.Entry(container, font=("Helvetica", 14))
        nombre_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Número de Contacto:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        contacto_entry = ttk.Entry(container, font=("Helvetica", 14))
        contacto_entry.pack(padx=10, pady=5, fill=tk.X)

        def registrar():
            nombre = nombre_entry.get()
            contacto = contacto_entry.get()
            self.sistema.registrar_cliente(nombre, contacto)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            top.destroy()

        ttk.Button(container, text="Registrar", command=registrar).pack(pady=20)

    def crear_ticket(self):
        top = tk.Toplevel(self.root)
        top.title("Crear Ticket")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="ID Cliente:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        cliente_id_entry = ttk.Entry(container, font=("Helvetica", 14))
        cliente_id_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Descripción:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        descripcion_entry = ttk.Entry(container, font=("Helvetica", 14))
        descripcion_entry.pack(padx=10, pady=5, fill=tk.X)

        def crear():
            cliente_id = int(cliente_id_entry.get())
            descripcion = descripcion_entry.get()
            self.sistema.crear_ticket(cliente_id, descripcion)
            messagebox.showinfo("Éxito", "Ticket creado correctamente.")
            top.destroy()

        ttk.Button(container, text="Crear", command=crear).pack(pady=20)

    def ver_tickets_cliente(self):
        top = tk.Toplevel(self.root)
        top.title("Ver Tickets de Cliente")
        top.geometry("500x400")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="ID Cliente:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        cliente_id_entry = ttk.Entry(container, font=("Helvetica", 14))
        cliente_id_entry.pack(padx=10, pady=5, fill=tk.X)

        def ver():
            cliente_id = int(cliente_id_entry.get())
            tickets = self.sistema.ver_tickets_cliente(cliente_id)
            for ticket in tickets:
                tk.Label(container, text=f"ID Ticket: {ticket[0]}\nFecha: {ticket[2]}\nDescripción: {ticket[3]}\nEstatus: {ticket[4]}", font=("Helvetica", 12), anchor="w").pack(pady=2, fill=tk.X)

        ttk.Button(container, text="Ver", command=ver).pack(pady=20)

    def cambiar_estatus_ticket(self):
        top = tk.Toplevel(self.root)
        top.title("Cambiar Estatus de Ticket")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="ID Ticket:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        ticket_id_entry = ttk.Entry(container, font=("Helvetica", 14))
        ticket_id_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Nuevo Estatus:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        estatus_entry = ttk.Entry(container, font=("Helvetica", 14))
        estatus_entry.pack(padx=10, pady=5, fill=tk.X)

        def cambiar():
            ticket_id = int(ticket_id_entry.get())
            nuevo_estatus = estatus_entry.get()
            self.sistema.cambiar_estatus_ticket(ticket_id, nuevo_estatus)
            messagebox.showinfo("Éxito", "Estatus del ticket actualizado.")
            top.destroy()

        ttk.Button(container, text="Cambiar", command=cambiar).pack(pady=20)

    def ver_clientes(self):
        top = tk.Toplevel(self.root)
        top.title("Ver Clientes")
        top.geometry("500x400")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        clientes = self.sistema.ver_clientes()
        for cliente in clientes:
            tk.Label(container, text=f"ID Cliente: {cliente[0]}, Nombre: {cliente[1]}, Número de Contacto: {cliente[2]}", font=("Helvetica", 12), anchor="w").pack(pady=2, fill=tk.X)

    def buscar_cliente(self):
        top = tk.Toplevel(self.root)
        top.title("Buscar Cliente")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        criterios = ["nombre", "numero_contacto"]
        tk.Label(container, text="Buscar por:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        criterio_var = tk.StringVar(value=criterios[0])
        ttk.Combobox(container, textvariable=criterio_var, values=criterios, font=("Helvetica", 14)).pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Valor:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        valor_entry = ttk.Entry(container, font=("Helvetica", 14))
        valor_entry.pack(padx=10, pady=5, fill=tk.X)

        def buscar():
            criterio = criterio_var.get()
            valor = valor_entry.get()
            clientes = self.sistema.buscar_clientes(criterio, valor)
            for cliente in clientes:
                tk.Label(container, text=f"ID Cliente: {cliente[0]}, Nombre: {cliente[1]}, Número de Contacto: {cliente[2]}", font=("Helvetica", 12), anchor="w").pack(pady=2, fill=tk.X)

        ttk.Button(container, text="Buscar", command=buscar).pack(pady=20)

    def buscar_ticket(self):
        top = tk.Toplevel(self.root)
        top.title("Buscar Ticket")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        criterios = ["descripcion", "estatus"]
        tk.Label(container, text="Buscar por:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        criterio_var = tk.StringVar(value=criterios[0])
        ttk.Combobox(container, textvariable=criterio_var, values=criterios, font=("Helvetica", 14)).pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Valor:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        valor_entry = ttk.Entry(container, font=("Helvetica", 14))
        valor_entry.pack(padx=10, pady=5, fill=tk.X)

        def buscar():
            criterio = criterio_var.get()
            valor = valor_entry.get()
            tickets = self.sistema.buscar_tickets(criterio, valor)
            for ticket in tickets:
                tk.Label(container, text=f"ID Ticket: {ticket[0]}, Cliente ID: {ticket[1]}, Fecha: {ticket[2]}, Descripción: {ticket[3]}, Estatus: {ticket[4]}", font=("Helvetica", 12), anchor="w").pack(pady=2, fill=tk.X)

        ttk.Button(container, text="Buscar", command=buscar).pack(pady=20)

    def generar_reporte(self):
        reporte = self.sistema.generar_reporte()
        top = tk.Toplevel(self.root)
        top.title("Reporte de Tickets")
        top.geometry("600x400")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        texto_reporte = tk.Text(container, font=("Helvetica", 12))
        texto_reporte.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        texto_reporte.insert(tk.END, reporte)

if __name__ == "__main__":
    sistema = SistemaReparaciones()
    root = tk.Tk()
    interfaz = InterfazGrafica(root, sistema)
    root.mainloop()
