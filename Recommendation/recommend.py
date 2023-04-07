import random

# Example dataset of videos and documents
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
        }
    ]
}

def recommend_videos(tags):
    # Filter videos by tags
    videos = [video for video in dataset["videos"] if any(tag in video["tags"] for tag in tags)]
    
    # Return a random video from the filtered list, or None if no videos match the tags
    return random.choice(videos) if videos else None

def recommend_documents(tags):
    # Filter documents by tags
    documents = [doc for doc in dataset["documents"] if any(tag in doc["tags"] for tag in tags)]
    
    # Return a random document from the filtered list, or None if no documents match the tags
    return random.choice(documents) if documents else None


# User's interests
tags = ["machine learning", "data science"]

# Recommend a video
video = recommend_videos(tags)
if video:
    print(f"Recommended video: {video['title']} ({video['url']})")

# Recommend a document
doc = recommend_documents(tags)
if doc:
    print(f"Recommended document: {doc['title']} ({doc['url']})")
