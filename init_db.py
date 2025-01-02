import sqlite3
from datetime import datetime

class SistemaReparaciones:
    def __init__(self):
        self.conn = sqlite3.connect('sistema_reparaciones.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT,
                            numero_contacto TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cliente_id INTEGER,
                            fecha TEXT,
                            descripcion TEXT,
                            estatus TEXT,
                            FOREIGN KEY (cliente_id) REFERENCES clientes (id))''')
        self.conn.commit()

    def registrar_cliente(self, nombre, numero_contacto):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO clientes (nombre, numero_contacto) VALUES (?, ?)",
                       (nombre, numero_contacto))
        self.conn.commit()

    def crear_ticket(self, cliente_id, descripcion):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estatus = "Pendiente"
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tickets (cliente_id, fecha, descripcion, estatus) VALUES (?, ?, ?, ?)",
                       (cliente_id, fecha, descripcion, estatus))
        self.conn.commit()

    def ver_tickets_cliente(self, cliente_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tickets WHERE cliente_id = ?", (cliente_id,))
        return cursor.fetchall()

    def cambiar_estatus_ticket(self, ticket_id, nuevo_estatus):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tickets SET estatus = ? WHERE id = ?",
                       (nuevo_estatus, ticket_id))
        self.conn.commit()

    def ver_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

    def buscar_clientes(self, criterio, valor):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM clientes WHERE {criterio} LIKE ?"
        cursor.execute(query, (f"%{valor}%",))
        return cursor.fetchall()

    def buscar_tickets(self, criterio, valor):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM tickets WHERE {criterio} LIKE ?"
        cursor.execute(query, (f"%{valor}%",))
        return cursor.fetchall()
    
    def generar_reporte(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tickets"
        cursor.execute(query)
        tickets = cursor.fetchall()
        reporte = "Reporte de Tickets:\n"
        for ticket in tickets:
            reporte += f"ID Ticket: {ticket[0]}, Cliente ID: {ticket[1]}, Fecha: {ticket[2]}, Descripción: {ticket[3]}, Estatus: {ticket[4]}\n"
        return reporte
