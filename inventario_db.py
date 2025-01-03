import sqlite3

class SistemaInventario:
    def __init__(self):
        self.conn = sqlite3.connect('inventario.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS inventario (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            producto TEXT,
                            cantidad INTEGER,
                            precio REAL)''')
        self.conn.commit()

    def registrar_producto(self, producto, cantidad, precio):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO inventario (producto, cantidad, precio) VALUES (?, ?, ?)",
                       (producto, cantidad, precio))
        self.conn.commit()

    def ver_inventario(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM inventario")
        return cursor.fetchall()

    def buscar_producto(self, criterio, valor):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM inventario WHERE {criterio} LIKE ?"
        cursor.execute(query, (f"%{valor}%",))
        return cursor.fetchall()
