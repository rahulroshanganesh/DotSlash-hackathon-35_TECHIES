import sqlite3

# Create the concepts database with sample data
concepts_conn = sqlite3.connect('concepts.db')
concepts_cursor = concepts_conn.cursor()

concepts_cursor.execute('CREATE TABLE IF NOT EXISTS concepts (id INTEGER PRIMARY KEY, name TEXT)')
concepts_cursor.execute('INSERT INTO concepts (name) VALUES ("Algebra")')
concepts_cursor.execute('INSERT INTO concepts (name) VALUES ("Geometry")')
concepts_cursor.execute('INSERT INTO concepts (name) VALUES ("Trigonometry")')
concepts_cursor.execute('INSERT INTO concepts (name) VALUES ("Calculus")')
concepts_cursor.execute('INSERT INTO concepts (name) VALUES ("Statistics")')

concepts_conn.commit()
concepts_conn.close()

#Create the questions database with sample data
questions_conn = sqlite3.connect('questions.db')
questions_cursor = questions_conn.cursor()

questions_cursor.execute('CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY, concept TEXT, question TEXT, answer TEXT)')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Algebra", "What is the value of x in the equation 2x + 5 = 13?", "4")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Algebra", "What is the slope of the line y = 2x + 1?", "2")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Geometry", "What is the area of a square with a side length of 5?", "25")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Geometry", "What is the sum of the angles in a triangle?", "180")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Trigonometry", "What is the sin of 30 degrees?", "0.5")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Trigonometry", "What is the value of tan(pi/4)?", "1")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Calculus", "What is the derivative of x^2?", "2x")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Calculus", "What is the integral of 2x?", "x^2 + C")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Statistics", "What is the mean of the numbers 3, 5, and 7?", "5")')
questions_cursor.execute('INSERT INTO questions (concept, question, answer) VALUES ("Statistics", "What is the standard deviation of the numbers 2, 4, and 6?", "sqrt(2)")')

questions_conn.commit()
questions_conn.close()
