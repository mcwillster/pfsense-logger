import sqlite3

def insert(client_ip, pfsense_ip, session_id):
    connection = sqlite3.connect("pfsense_session_IDs.db")
    cursor = connection.cursor()
    ip_lst = pfsense_ip.split('.')
    table_name = "Team " + ip_lst[2]
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_address VARCHAR(15) NOT NULL,
            pfsense_address VARCHAR(15) NOT NULL,
            session_id TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute(
        f"INSERT INTO '{table_name}' (client_address, pfsense_address, session_id) values(?, ?, ?)", 
        (client_ip, pfsense_ip, session_id)
    )
    connection.commit()

def main():
    insert("192.168.1.10", "192.168.1.254", "Test1")
    insert("192.168.2.10", "192.168.2.254", "Test2")
    insert("192.168.3.11", "192.168.3.254", "Test3")

if __name__ == "__main__":
    main()