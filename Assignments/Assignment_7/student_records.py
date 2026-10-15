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

  
