import sqlite3

connection = sqlite3.connect("pfsense_session_IDs.db")

cursor = connection.cursor()

def insert(client_ip, pfsense_ip, session_id):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS '{pfsense_ip}' (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_address VARCHAR(15) NOT NULL,
            pfsense_address VARCHAR(15) NOT NULL,
            session_id TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute(
        f"INSERT INTO '{pfsense_ip}' (client_address, pfsense_address, session_id) values(?, ?, ?)", 
        (client_ip, pfsense_ip, session_id)
    )
    connection.commit()

def main():
    insert("192.168.1.10", "192.168.1.254", "Test1")
    insert("192.168.1.10", "192.168.2.254", "Test2")
    insert("192.168.1.11", "192.168.3.254", "Test3")

if __name__ == "__main__":
    main()