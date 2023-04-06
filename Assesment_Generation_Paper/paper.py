import sqlite3
import random
from docx import Document
from paper import generate_exam_paper, get_student_weakness
from reportlab.pdfgen import canvas
from docx import Document

from builtins import SomeException
def generate_exam_paper(weakness, num_questions):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Select random concepts from the concepts database
    cursor.execute("SELECT question FROM questions WHERE concept=?", (weakness,))
    concepts = [row[0] for row in cursor.fetchall()]
    print(concepts)

    # Select random questions from the questions database for each concept
    exam_paper = []
    for concept in concepts:
        cursor.execute("SELECT question FROM questions WHERE concept = ?  LIMIT ?", (concept, num_questions))
        questions = [row[0] for row in cursor.fetchall()]
        for question in questions:
            exam_paper.append((concept, question))

    conn.close()
    return exam_paper


def get_student_weakness(name):
    # Connect to the database
    conn = sqlite3.connect('weakness.db')
    cursor = conn.cursor()
    
    # Retrieve the weakness for the given student name
    cursor.execute("SELECT weakness FROM students WHERE SRN=?", (name,))
    result = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    # Return the weakness if found, or None if not found
    if result:
        return result[0]
    else:
        return None

# Example usage
weakness = get_student_weakness(358)
paper = generate_exam_paper(weakness, 1)
print(paper)
