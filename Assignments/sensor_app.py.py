import sqlite3
import time
import serial                      # from the pyserial package

PORT = "COM6"                      # <-- CHANGE to your board's port (see Device Manager)
BAUD = 115200


def ask_board(ser, command):
    """Send a one-letter command to the board and return the number it replies with."""
    ser.reset_input_buffer()                  # discard any stale data
    ser.write((command + "\n").encode())      # send command + newline
    # Read lines until one starts with DATA (ignores any boot messages)
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line == "":
            raise TimeoutError("No reply from board")
        if line.startswith("DATA,"):
            return float(line.split(",")[2])

# a class to manage the database connection and operations
class DatabaseManager:
    def __init__ (self,db_name):
        self.con = sqlite3.connect(db_name)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS sensor_data
        ( id Integer PRIMARY KEY,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        sensor_type VARCHAR(30),
        sensor_reading_value FLOAT ) """)
    def log_history(self, sensor_type, sensor_reading_value): # method to log the sensor data into the database
        with self.con:
            self.con.execute(""" INSERT INTO sensor_data(sensor_type, sensor_reading_value) VALUES (?, ?) """, (sensor_type, sensor_reading_value))
    def get_history(self): #method to get the sensor data from the database
        with self.con:
            return self.con.execute("""SELECT * FROM sensor_data""").fetchall()

#  function to ask the board for the temperature/humidity, display it, and log it to the database
def temperature(ser, db_manager):
    temp = ask_board(ser,"T")
    print(f"Temperature: {temp:.1f} C")
    db_manager.log_history("Temperature", temp)

def humidity(ser, db_manager):
    hum = ask_board(ser,"H")
    print(f"Humidity: {hum:.1f} %")
    db_manager.log_history("Humidity", hum)

def main():
    ser = serial.Serial(PORT, BAUD, timeout=5)
    time.sleep(2)
    ser.reset_input_buffer()
    db_manager = DatabaseManager("sensor_data.db")
  # loop to ask the user for input and call the appropriate function
    while True:
        print("Please choose from the following options:")
        print("T- temperature")
        print("H- humidity")
        print("0 - both")
        print("V - view history")
        choice = input("Enter your choice: ").lower()
        if choice == "t":
            temperature(ser,db_manager)
        elif choice == "h":
            humidity(ser,db_manager)
        elif choice == "0":
            temperature(ser,db_manager)
            humidity(ser,db_manager)
        elif choice == "v":
            history = db_manager.get_history()
            for row in history:
                print(row)
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
