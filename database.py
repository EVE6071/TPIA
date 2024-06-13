import duckdb

def create_database():
    con = duckdb.connect(database='attendance.db', read_only=False)
    con.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY,
            person_name TEXT,
            timestamp TIMESTAMP
        )
    ''')
    con.close()

def insert_attendance_record(person_name, timestamp):
    con = duckdb.connect(database='attendance.db', read_only=False)
    con.execute('''
        INSERT INTO attendance (person_name, timestamp) VALUES (?, ?)
    ''', (person_name, timestamp))
    con.close()

def generate_report():
    con = duckdb.connect(database='attendance.db', read_only=True)
    report = con.execute('''
        SELECT person_name, COUNT(*) as appearances FROM attendance GROUP BY person_name
    ''').fetchall()
    con.close()
    return report
