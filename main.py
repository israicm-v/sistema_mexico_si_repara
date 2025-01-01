import sqlite3
from datetime import datetime

# Crear una conexión con la base de datos
def create_connection():
    conn = sqlite3.connect('sistema_reparaciones.db')
    return conn

# Registrar un nuevo cliente
def registrar_cliente(nombre, numero_contacto):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO clientes (nombre, numero_contacto) VALUES (?, ?)", 
                   (nombre, numero_contacto))
    
    conn.commit()
    conn.close()

# Crear un nuevo ticket
def crear_ticket(cliente_id, descripcion):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    estatus = "Pendiente"
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO tickets (cliente_id, fecha, descripcion, estatus) VALUES (?, ?, ?, ?)", 
                   (cliente_id, fecha, descripcion, estatus))
    
    conn.commit()
    conn.close()

# Ver los tickets de un cliente
def ver_tickets_cliente(cliente_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tickets WHERE cliente_id = ?", (cliente_id,))
    tickets = cursor.fetchall()
    
    for ticket in tickets:
        print(f"ID Ticket: {ticket[0]} - Fecha: {ticket[2]} - Descripción: {ticket[3]} - Estatus: {ticket[4]}")
    
    conn.close()

# Cambiar el estatus de un ticket
def cambiar_estatus_ticket(ticket_id, nuevo_estatus):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tickets SET estatus = ? WHERE id = ?", 
                   (nuevo_estatus, ticket_id))
    
    conn.commit()
    conn.close()

# Ver todos los clientes
def ver_clientes():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    
    for cliente in clientes:
        print(f"ID Cliente: {cliente[0]} - Nombre: {cliente[1]} - Número de Contacto: {cliente[2]}")
    
    conn.close()

# Menú principal
def menu():
    while True:
        print("\nSistema de Reparaciones")
        print("1. Registrar cliente")
        print("2. Crear ticket")
        print("3. Ver tickets de un cliente")
        print("4. Cambiar estatus de un ticket")
        print("5. Ver clientes")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Ingresa el nombre del cliente: ")
            numero_contacto = input("Ingresa el número de contacto del cliente: ")
            registrar_cliente(nombre, numero_contacto)
            print("Cliente registrado correctamente.")
        
        elif opcion == '2':
            cliente_id = int(input("Ingresa el ID del cliente: "))
            descripcion = input("Descripción del servicio o reparación: ")
            crear_ticket(cliente_id, descripcion)
            print("Ticket creado correctamente.")
        
        elif opcion == '3':
            cliente_id = int(input("Ingresa el ID del cliente: "))
            ver_tickets_cliente(cliente_id)
        
        elif opcion == '4':
            ticket_id = int(input("Ingresa el ID del ticket: "))
            nuevo_estatus = input("Nuevo estatus del ticket (Ej. En reparación, Reparado, etc.): ")
            cambiar_estatus_ticket(ticket_id, nuevo_estatus)
            print("Estatus de ticket actualizado.")
        
        elif opcion == '5':
            ver_clientes()
        
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu()
