import sqlite3

def initialize_database():
    # Initalize database.
    conn = sqlite3.connect('data/metrics.db')
    cursor = conn.cursor()

    # Create the metrics table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu_usage REAL,
            memory_usage REAL,
            disk_usage REAL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()