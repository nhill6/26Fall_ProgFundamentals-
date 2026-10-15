.\sqlite3 studentrecords.db
CREATE TABLE studentrecords 
  ( id WHOLE NUMBER PRIMARY KEY,
  name TEXT,
  age WHOLE NUMBER,
  major TEXT );
students = [
  (1, "Amy", 18, "Poltical Science")
  (2, "Kennedy", 20, "Engineering")
  (1, "Gabby", 19, "Kinesology")
  (1, "Jaeden", 22, "Psychology")
  (1, "Julyah", 18, "Nursing")
]
for student in students:
  print(f'Name: {student[1]}, Age: {student[2]}, Major: {student[3]}")
while True:
  answer = input("Do you want to add a new student?(yes/no):  ").lower()
  if answer == "yes":
   while True:
    name = input("Enter student's name: ")
    if name != "":
      break
    print("Name cannot be empty.")
    while True:
    age = int(input("Enter student's age: "))
    break
  except ValueError:
    print("Age must be a whole number")
    while True: 
      major = input("Enter student's major: ")
      if major != "":
      break
      print ("Major can not be empty")
    break
  elif answer == "no":
    print("No new student added.")
  else:
    print("Please enter yes or no.")

  cursor.execute("SELECT MAX(id) FROM studentrecords")
  new_id = cursor.fetchone()[0] + 1
  cursor.execute(
    "INSERT INTO studentrecord (id, name, age, major) VALUES (?,?,?,?)",
    (new_id, name, age, major)
  )
  conn.commit()
  conn.close



  
