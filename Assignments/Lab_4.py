import sqlit3
input("Please choose from the following options T -temperature, H - humidity, 0 - both, V - veiw log history")
class DatabaseManager:
    def __init__(self):
        conn = sqlite3.connect("sensor_data.db")
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS sensor_data")
        cur.execute("""
            CREATE TABLE sensor_data (
            id INTEGER PRIMARY KEY,
            timestamp INTEGER,
            sensor_type VARCHAR(30),
            sensor_reading_value INTEGER )
            """)
            conn.commit()
            conn.close()
    def reading(self, timetamp,sensor_type,sensor_reading_value):
        conn = sqlite3.connect("sensor_data.db")
        cur.execute("""
            INSERT INTO sensor_data
            (timestamp, sensor_type, sensor_reading_value)
            VALUES(?, ?, ?)
            """, (timestamp, sensor_type, sensor_reading_value))
            conn.commit()
            conn.close()
    def get_readings(self):
        con = sqlite3.connect("sensor_data.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM sensor_data")
        reaings = cur.fetchall()
        conn.close()
        return readings
    def display_readings(self):
        readings = self.get_readings()
        if not readings:
            print("No sensor readings found.")
            return
        for reading in readings:
            print(
                f"ID: {reading[0]}, "
                f"Timestamp: {reading[1]}, "
                f"Sensor: {reading[2]}, "
                f"Value: {reading[3]}" )
            
            
        
                
        