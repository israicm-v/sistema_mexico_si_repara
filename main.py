import tkinter as tk
from tkinter import messagebox
from init_db import SistemaReparaciones

class InterfazGrafica:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Reparaciones")
        self.crear_menu()

    def crear_menu(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Button(frame, text="Registrar Cliente", command=self.registrar_cliente).pack(fill=tk.X)
        tk.Button(frame, text="Crear Ticket", command=self.crear_ticket).pack(fill=tk.X)
        tk.Button(frame, text="Ver Tickets de Cliente", command=self.ver_tickets_cliente).pack(fill=tk.X)
        tk.Button(frame, text="Cambiar Estatus de Ticket", command=self.cambiar_estatus_ticket).pack(fill=tk.X)
        tk.Button(frame, text="Ver Clientes", command=self.ver_clientes).pack(fill=tk.X)
        tk.Button(frame, text="Salir", command=self.root.quit).pack(fill=tk.X)

    def registrar_cliente(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Cliente")

        tk.Label(top, text="Nombre:").pack(padx=10, pady=5)
        nombre_entry = tk.Entry(top)
        nombre_entry.pack(padx=10, pady=5)

        tk.Label(top, text="Número de Contacto:").pack(padx=10, pady=5)
        contacto_entry = tk.Entry(top)
        contacto_entry.pack(padx=10, pady=5)

        def registrar():
            nombre = nombre_entry.get()
            contacto = contacto_entry.get()
            self.sistema.registrar_cliente(nombre, contacto)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            top.destroy()

        tk.Button(top, text="Registrar", command=registrar).pack(pady=10)

    def crear_ticket(self):
        top = tk.Toplevel(self.root)
        top.title("Crear Ticket")

        tk.Label(top, text="ID Cliente:").pack(padx=10, pady=5)
        cliente_id_entry = tk.Entry(top)
        cliente_id_entry.pack(padx=10, pady=5)

        tk.Label(top, text="Descripción:").pack(padx=10, pady=5)
        descripcion_entry = tk.Entry(top)
        descripcion_entry.pack(padx=10, pady=5)

        def crear():
            cliente_id = int(cliente_id_entry.get())
            descripcion = descripcion_entry.get()
            self.sistema.crear_ticket(cliente_id, descripcion)
            messagebox.showinfo("Éxito", "Ticket creado correctamente.")
            top.destroy()

        tk.Button(top, text="Crear", command=crear).pack(pady=10)

    def ver_tickets_cliente(self):
        top = tk.Toplevel(self.root)
        top.title("Ver Tickets de Cliente")

        tk.Label(top, text="ID Cliente:").pack(padx=10, pady=5)
        cliente_id_entry = tk.Entry(top)
        cliente_id_entry.pack(padx=10, pady=5)

        def ver():
            cliente_id = int(cliente_id_entry.get())
            tickets = self.sistema.ver_tickets_cliente(cliente_id)
            for ticket in tickets:
                tk.Label(top, text=f"ID Ticket: {ticket[0]}, Fecha: {ticket[2]}, Descripción: {ticket[3]}, Estatus: {ticket[4]}").pack(pady=2)

        tk.Button(top, text="Ver", command=ver).pack(pady=10)

    def cambiar_estatus_ticket(self):
        top = tk.Toplevel(self.root)
        top.title("Cambiar Estatus de Ticket")

        tk.Label(top, text="ID Ticket:").pack(padx=10, pady=5)
        ticket_id_entry = tk.Entry(top)
        ticket_id_entry.pack(padx=10, pady=5)

        tk.Label(top, text="Nuevo Estatus:").pack(padx=10, pady=5)
        estatus_entry = tk.Entry(top)
        estatus_entry.pack(padx=10, pady=5)

        def cambiar():
            ticket_id = int(ticket_id_entry.get())
            nuevo_estatus = estatus_entry.get()
            self.sistema.cambiar_estatus_ticket(ticket_id, nuevo_estatus)
            messagebox.showinfo("Éxito", "Estatus del ticket actualizado.")
            top.destroy()

        tk.Button(top, text="Cambiar", command=cambiar).pack(pady=10)

    def ver_clientes(self):
        top = tk.Toplevel(self.root)
        top.title("Ver Clientes")

        clientes = self.sistema.ver_clientes()
        for cliente in clientes:
            tk.Label(top, text=f"ID Cliente: {cliente[0]}, Nombre: {cliente[1]}, Número de Contacto: {cliente[2]}").pack(pady=2)

if __name__ == "__main__":
    sistema = SistemaReparaciones()
    root = tk.Tk()
    interfaz = InterfazGrafica(root, sistema)
    root.mainloop()
