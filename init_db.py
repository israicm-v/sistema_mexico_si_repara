import sqlite3

# Crear una conexión con la base de datos
def create_connection():
    conn = sqlite3.connect('sistema_reparaciones.db')
    return conn

# Crear las tablas necesarias en la base de datos
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Crear tabla para clientes
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        numero_contacto TEXT)''')

    # Crear tabla para tickets
    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente_id INTEGER,
                        fecha TEXT,
                        descripcion TEXT,
                        estatus TEXT,
                        FOREIGN KEY (cliente_id) REFERENCES clientes (id))''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Base de datos y tablas creadas correctamente.")
