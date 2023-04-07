import tkinter as tk
from tkinter import ttk

# Your dataset and recommend function should be here
import math

dataset = {
    "videos": [
        {
            "title": "Introduction to Machine Learning",
            "description": "This video provides an introduction to machine learning and its applications in different fields.",
            "tags": ["machine learning", "data science", "AI"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=I74ymkoNTnw"
        },
        {
            "title": "Python Tutorial for Beginners",
            "description": "This video provides a comprehensive tutorial on Python programming for beginners.",
            "tags": ["Python", "programming", "beginners"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=_Z1GQj3F5fM"
        },
        {
            "title": "React Native Tutorial",
            "description": "This video provides a step-by-step tutorial on building a mobile app using React Native.",
            "tags": ["React Native", "mobile development", "app development"],
            "category": "Technology",
            "url": "https://www.youtube.com/watch?v=0-S5a0eXPoc"
        },
        {
            "title": "Deep Learning with TensorFlow",
            "description": "This video covers the basics of deep learning with TensorFlow and its applications.",
            "tags": ["deep learning", "TensorFlow", "AI"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=xxpc-HPKN28"
        },
        {
            "title": "HTML and CSS for Beginners",
            "description": "This video tutorial teaches the fundamentals of HTML and CSS for web development.",
            "tags": ["HTML", "CSS", "web development"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=9gTw2D1N4i0"
        },
        {
            "title": "Introduction to Data Visualization with Matplotlib",
            "description": "This video provides an introduction to data visualization using the Matplotlib library in Python.",
            "tags": ["data visualization", "Matplotlib", "Python"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=DAQNHzOcO5A"
        },
        {
            "title": "Django Web Development Tutorial",
            "description": "This video tutorial demonstrates how to build web applications using the Django framework.",
            "tags": ["Django", "web development", "Python"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=F5mRW0jo-U4"
        },
        {
            "title": "Blockchain Explained",
            "description": "This video provides an overview of blockchain technology and its potential applications.",
            "tags": ["blockchain", "technology", "cryptocurrency"],
            "category": "Education",
            "url": "https://www.youtube.com/watch?v=_160oMzblY8"
        }
    ],
    "documents": [
        {
            "title": "Machine Learning Basics",
            "description": "This document provides an introduction to machine learning and its basic concepts.",
            "tags": ["machine learning", "data science", "AI"],
            "category": "Education",
            "url": "https://www.example.com/machine-learning-basics"
        },
        {
            "title": "Python Programming Guide",
            "description": "This document provides a comprehensive guide on Python programming for beginners.",
            "tags": ["Python", "programming", "beginners"],
            "category": "Education",
            "url": "https://www.example.com/python-programming-guide"
        },
        {
            "title": "React Native Documentation",
            "description": "This document provides detailed documentation on building mobile apps using React Native.",
            "tags": ["React Native", "mobile development", "app development"],
            "category": "Technology",
            "url": "https://www.example.com/react-native-documentation"
        },
        {
            "title": "Deep Learning with TensorFlow Guide",
            "description": "This document covers the basics of deep learning with TensorFlow and its applications.",
            "tags": ["deep learning", "TensorFlow", "AI"],
            "category": "Education",
            "url": "https://www.example.com/deep-learning-tensorflow-guide"
        },
        {
            "title": "HTML and CSS for Beginners Guide",
            "description": "This document teaches the fundamentals of HTML and CSS for web development.",
            "tags": ["HTML", "CSS", "web development"],
            "category": "Education",
            "url": "https://www.example.com/html-css-for-beginners"
        },
        {
            "title": "Data Visualization with Matplotlib Guide",
            "description": "This document provides an introduction to data visualization using the Matplotlib library in Python.",
            "tags": ["data visualization", "Matplotlib", "Python"],
            "category": "Education",
            "url": "https://www.example.com/data-visualization-matplotlib"
        },
        {
            "title": "Django Web Development Guide",
            "description": "This document demonstrates how to build web applications using the Django framework.",
            "tags": ["Django", "web development", "Python"],
            "category": "Education",
            "url": "https://www.example.com/django-web-development"
        }
    ]
}

def get_similarity_score(tags1, tags2):
    """
    Calculates the similarity score between two lists of tags using Jaccard similarity.
    """
    set1 = set(tags1)
    set2 = set(tags2)
    return len(set1.intersection(set2)) / len(set1.union(set2))

def recommend(content_type, tags, full_item=False):
    if content_type == "videos":
        dataset_to_use = dataset["videos"]
    elif content_type == "documents":
        dataset_to_use = dataset["documents"]
    else:
        return None

    similarities = {}
    for item in dataset_to_use:
        similarities[item["title"]] = get_similarity_score(tags, item["tags"])

    sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    if sorted_items:
        recommended_title = sorted_items[0][0]
        if full_item:
            # Return the complete dictionary of the recommended item
            for item in dataset_to_use:
                if item["title"] == recommended_title:
                    return item
        else:
            return recommended_title
    else:
        return None

# GUI code starts here

def on_recommend():
    content_type = content_var.get()
    input_tags = tags_entry.get().split(',')

    recommended_item = recommend(content_type, input_tags, full_item=True)
    if recommended_item:
        result_text = f"Recommended {content_type[:-1]}:\n"
        result_text += f"Title: {recommended_item['title']}\n"
        result_text += f"Description: {recommended_item['description']}\n"
        result_text += f"Tags: {', '.join(recommended_item['tags'])}\n"
        result_text += f"Category: {recommended_item['category']}\n"
        result_text += f"URL: {recommended_item['url']}"
    else:
        result_text = "No recommendation found."

    result_label.config(text=result_text)

root = tk.Tk()
root.title("Content Recommendation System")

content_var = tk.StringVar()
content_label = ttk.Label(root, text="Select content type:")
content_label.grid(row=0, column=0, padx=10, pady=10)

content_menu = ttk.OptionMenu(root, content_var, "videos", "videos", "documents")
content_menu.grid(row=0, column=1, padx=10, pady=10)

tags_label = ttk.Label(root, text="Enter tags (comma separated):")
tags_label.grid(row=1, column=0, padx=10, pady=10)

tags_entry = ttk.Entry(root)
tags_entry.grid(row=1, column=1, padx=10, pady=10)

recommend_button = ttk.Button(root, text="Recommend", command=on_recommend)
recommend_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
