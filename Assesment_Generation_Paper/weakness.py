import sqlite3

# create or connect to the database
conn = sqlite3.connect('weakness.db')

# create the table
conn.execute('''CREATE TABLE students
                (SRN INT  NOT NULL,
                 weakness TEXT NOT NULL);''')

# insert sample data
conn.execute("INSERT INTO students (SRN, weakness) VALUES (?, ?)", (355, 'Algebra'))
conn.execute("INSERT INTO students (SRN, weakness) VALUES (?, ?)", (356, 'Trigonometry'))
conn.execute("INSERT INTO students (SRN, weakness) VALUES (?, ?)", (357, 'Calculus'))
conn.execute("INSERT INTO students (SRN, weakness) VALUES (?, ?)", (358, 'Algebra'))

# commit changes and close connection
conn.commit()
conn.close()
