import sqlite3
conn = sqlite3.connect("studentrecords.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS studentrecords")
cur.execute("""
CREATE TABLE studentrecords ( 
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  major TEXT 
  )
  """)
students = [
  (1, "Amy", 18, "Political Science"),
  (2, "Kennedy", 20, "Engineering"),
  (3, "Gabby", 19, "Kinesiology"),
  (4, "Jaeden", 22, "Psychology"),
  (5, "Julyah", 18, "Nursing")
]
cursor.executemany(
  "INSERT INTO studentrecords (id,name, age, major) VALUES (?, ?, ?, ?)",
  students
)
for student in students:
  print(f"Name: {student[1]}, Age: {student[2]}, Major: {student[3]}")
while True:
    answer = input("Do you want to add a new student? (yes/no): ").lower()
    if answer == "yes":
        while True:
            name = input("Enter student's name: ")
            if name != "":
                break
            print("Name cannot be empty.")
        while True:
            try:
                age = int(input("Enter student's age: "))
                break
            except ValueError:
                print("Age must be a whole number")
        while True:
            major = input("Enter student's major: ")
            if major != "":
                break
            print("Major cannot be empty")
        cursor.execute("SELECT MAX(id) FROM studentrecords")
        new_id = cursor.fetchone()[0] + 1
        cursor.execute(
            "INSERT INTO studentrecords (id, name, age, major) VALUES (?, ?, ?, ?)",
            (new_id, name, age, major)
        )
        break
    elif answer == "no":
        print("No new student added.")
        break
    else:
        print("Please enter yes or no.")
conn.commit()
conn.close()



  
