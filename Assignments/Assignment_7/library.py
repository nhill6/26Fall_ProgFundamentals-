import sqlite3
conn = sqlite3.connect("library.db") 
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS books")
cur.execute("""
  CREATE TABLE books (
    id INTEGER PRIMARY KEY, 
    title VARCHAR(30) NOT NULL, 
    author VARCHAR(30) NOT NULL, 
    year INTEGER, 
    genre VARCHAR(30), 
    copies INTEGER, 
    rating INTEGER
  )
  """)
cur.execute(
  "INSERT INTO books VALUES (1, 'The Great Gatsby', 'F Scott Fitzgerald', 1925, 'Fiction', 5, 4)"
  )
books = [
(2, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 3, None),
(3, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 1, 3),
(4, "The Alchemist", "Paulo Coelho", 1988, "Fiction", 8, 4),
(5, "The Silent Patient", "Alex Michaelides", 2019, "Mystery", 15, 4),
(6, "The Silk Roads: A new history of the world", "Peter Frankopan", 1855, "History", 1, None),
(7, "Before the Big Bang: The Origin of the Universe and What Lies Beyond", "Laura Mersini-Houghton", 2022, "Science", 3, 5),
(8, "All American Boys", "Jason Reynolds", 2015, "Fiction", 28, 5),
]
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?,?)", books)
print("title and author of books published after 1990:")
for row in cur.execute("SELECT title, author FROM books WHERE year >= 1990"):
  print(f"Title:{row[0]}  Author: {row[1]}")
print("title of fiction books with more than 2 copies:")
for row in cur.execute("SELECT title FROM books WHERE genre = 'Fiction' AND copies >= 2"):
  print("Title: ", row)
print(" title of books published before 1900 or rated 5:")
for row in cur.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5"):
  print("Title, year, and/or rating: ", row)
print("title of books that are not in the Mystery genre:")
for row in cur.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'"):
  print("Title: ", row)
print("title of books in either the Science or History genre :")
for row in cur.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')"):
  print("Title and genre: ", row)
letter = input("Enter a letter: ")
cur.execute(
  "SELECT author from books where author LIKE ?" ,
  (letter + "%",)
)
results = cur.fetchall()
for row in results:
  print("Author: ", row[0])
print("title of books that have no rating:")
for row in cur.execute("SELECT title FROM books WHERE rating IS NULL"):
  print("Title and rating: ", row)
conn.commit()
conn.close()
