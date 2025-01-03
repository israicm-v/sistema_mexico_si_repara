#ISRAEL CHALICO MONTOYA 
#2025
#VERSION 1.0 
#SISTEMA DE REGISTRO DE CLIENTES Y PRODUCTOS TIPO INVENTARIO 

import tkinter as tk 
from tkinter import messagebox, ttk
from clientes_db import SistemaReparaciones #Archivo que guarda los datos de clientes 
from inventario_db import SistemaInventario #Archivo que guarda los datos de los productos tipo inventario 

class InterfazGrafica:  # Interfaz grafica principal
    def __init__(self, root, sistema, inventario): 
        self.root = root 
        self.sistema = sistema 
        self.inventario = inventario 
        self.root.title(" MEXICO SI REPARA - desarrollado por israchals") 
        self.root.geometry("1500x800") #Tamaño de la pantalla principal 
        self.crear_menu_principal()

#Esta funcion creara el menú principal, con 2 opciones la de clientes y la de inventario
#En algun futuro se espera poder incorporar uno para ventas 

# ------------MENU PRINCIPAL -----------#   

    def crear_menu_principal(self): 
        for widget in self.root.winfo_children(): 
            widget.destroy()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(pady=20) 
        titulo = tk.Label(frame, text="SISTEMA DE REGISTRO", font=("Helvetica", 20, "bold")) 
        titulo.pack(pady=20) 
        style = ttk.Style() 
        style.configure("TButton", font=("Helvetica", 12), padding=10) 
        ttk.Button(frame, text="Clientes", command=self.crear_menu_cliente).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Inventario", command=self.crear_menu_inventario).pack(fill=tk.X, pady=10) 
        
        ##funcionalidad propuesta para una version futura
        #ttk.Button(frame, text="Ventas", command=self,crear_menu_ventas).pack(fill=tk.X, pady=10)
    
    #Esta función creara el menú para los clientes 
    def crear_menu_cliente(self): 
        for widget in self.root.winfo_children(): 
            widget.destroy()
        frame = tk.Frame(self.root, padx=20, pady=20) 
        frame.pack(pady=20) 
        ttk.Button(frame, text="Tickets", command=self.crear_menu_tickets).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Registros", command=self.crear_menu_registros).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Búsqueda y Reportes", command=self.crear_menu_busqueda_reportes).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Regresar" , command=self.crear_menu_principal).pack(fill=tk.X,pady=10)

    def crear_menu_tickets(self): 
        for widget in self.root.winfo_children():
            widget.destroy() 
        frame = tk.Frame(self.root, padx=20, pady=20) 
        frame.pack(pady=20) 
        ttk.Button(frame, text="Crear Ticket", command=self.crear_ticket).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Ver Tickets de Cliente", command=self.ver_tickets_cliente).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Cambiar Estatus de Ticket", command=self.cambiar_estatus_ticket).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Regresar" , command=self.crear_menu_cliente).pack(fill=tk.X,pady=10)


    def crear_menu_registros(self): 
        for widget in self.root.winfo_children(): 
            widget.destroy() 
        frame = tk.Frame(self.root, padx=20, pady=20) 
        frame.pack(pady=20)
        ttk.Button(frame, text="Registrar Cliente", command=self.registrar_cliente).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Ver Clientes", command=self.ver_clientes).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Regresar" , command=self.crear_menu_cliente).pack(fill=tk.X,pady=10)

    def crear_menu_busqueda_reportes(self): 
        for widget in self.root.winfo_children(): 
            widget.destroy()
        frame = tk.Frame(self.root, padx=20, pady=20) 
        frame.pack(pady=20) 
        ttk.Button(frame, text="Buscar Cliente", command=self.buscar_cliente).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Buscar Ticket", command=self.buscar_ticket).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Generar Reporte", command=self.generar_reporte).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Regresar" , command=self.crear_menu_cliente).pack(fill=tk.X,pady=10)

    def crear_menu_inventario(self): 
        for widget in self.root.winfo_children(): 
            widget.destroy()
        frame = tk.Frame(self.root, padx=20, pady=20) 
        frame.pack(pady=20) 
        ttk.Button(frame, text="Registrar Producto", command=self.registrar_producto).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Ver Inventario", command=self.ver_inventario).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Buscar Producto", command=self.buscar_producto).pack(fill=tk.X, pady=10) 
        ttk.Button(frame, text="Regresar" , command=self.crear_menu_principal).pack(fill=tk.X,pady=10)
    
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

    def registrar_producto(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Producto")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="Producto:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        producto_entry = ttk.Entry(container, font=("Helvetica", 14))
        producto_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Cantidad:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        cantidad_entry = ttk.Entry(container, font=("Helvetica", 14))
        cantidad_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Precio:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        precio_entry = ttk.Entry(container, font=("Helvetica", 14))
        precio_entry.pack(padx=10, pady=5, fill=tk.X)

        def registrar():
            producto = producto_entry.get()
            cantidad = int(cantidad_entry.get())
            precio = float(precio_entry.get())
            self.inventario.registrar_producto(producto, cantidad, precio)
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            top.destroy()

        ttk.Button(container, text="Registrar", command=registrar).pack(pady=20)

    def ver_inventario(self):
        top = tk.Toplevel(self.root)
        top.title("Inventario")
        top.geometry("500x400")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        inventario = self.inventario.ver_inventario()
        for producto in inventario:
            tk.Label(container, text=f"ID: {producto[0]}, Producto: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[3]}", font=("Helvetica", 12), anchor="w").pack(pady=2, fill=tk.X)

    def buscar_producto(self):
        top = tk.Toplevel(self.root)
        top.title("Buscar Producto")
        top.geometry("400x300")

        container = tk.Frame(top, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        criterios = ["producto", "cantidad", "precio"]
        tk.Label(container, text="Buscar por:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        criterio_var = tk.StringVar(value=criterios[0])
        ttk.Combobox(container, textvariable=criterio_var, values=criterios, font=("Helvetica", 14)).pack(padx=10, pady=5, fill=tk.X)

        tk.Label(container, text="Valor:", font=("Helvetica", 14)).pack(padx=10, pady=5)
        valor_entry = ttk.Entry(container, font=("Helvetica", 14))
        valor_entry.pack(padx=10, pady=5, fill=tk.X)

        def buscar():
            criterio = criterio_var.get()
            valor = valor_entry.get()
            productos = self.inventario.buscar_producto(criterio, valor)
            for producto in productos:
                tk.Label(container, text=f"ID: {producto[0]}, Producto: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[3]}", font=("Helvetica", 12), anchor="w").pack(pady=2, fill=tk.X)

        ttk.Button(container, text="Buscar", command=buscar).pack(pady=20)

if __name__ == "__main__":
    sistema = SistemaReparaciones()
    inventario = SistemaInventario()
    root = tk.Tk()
    interfaz = InterfazGrafica(root, sistema, inventario)
    root.mainloop()
