import sqlite3
import random

def generate_exam_paper(num_concepts, num_questions):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Select random concepts from the concepts database
    cursor.execute("SELECT concept FROM questions ORDER BY RANDOM() LIMIT ?", (num_concepts,))
    concepts = [row[0] for row in cursor.fetchall()]

    # Select random questions from the questions database for each concept
    exam_paper = []
    for concept in concepts:
        cursor.execute("SELECT question FROM questions WHERE concept = ? ORDER BY RANDOM() LIMIT ?", (concept, num_questions))
        questions = [row[0] for row in cursor.fetchall()]
        for question in questions:
            exam_paper.append((concept, question))

    conn.close()
    return exam_paper

# Example usage
paper = generate_exam_paper(3, 1)
print(paper)
