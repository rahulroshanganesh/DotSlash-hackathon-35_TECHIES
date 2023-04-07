import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

# Train a CountVectorizer on the descriptions of the videos and documents
corpus = [item["description"] for item in dataset["videos"] + dataset["documents"]]
vectorizer = CountVectorizer().fit_transform(corpus)

def recommend_videos(tags):
    # Filter videos by tags
    videos = [video for video in dataset["videos"] if any(tag in video["tags"] for tag in tags)]
    
    # If there are no matching videos, return None
    if not videos:
        return None
    
    # Convert the descriptions of the videos to a matrix of feature vectors
    video_descriptions = [video["description"] for video in videos]
    video_vectors = vectorizer.transform(video_descriptions).toarray()
    
    # Calculate the cosine similarities between the user's interests and the videos' descriptions
    tag_vector = vectorizer.transform([" ".join(tags)]).toarray()
    similarities = cosine_similarity(tag_vector, video_vectors)
    
    # Sort the videos by their similarity to the user's interests
    video_similarities = list(zip(videos, similarities[0]))
    video_similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Return the most similar video
    return video_similarities[0][0]

def recommend_documents(tags):
    # Filter documents by tags
    documents = [document for document in dataset["documents"] if any(tag in document["tags"] for tag in tags)]

    # If there are no matching documents, return None
    if not documents:
        return None

    # Convert the descriptions of the documents to a matrix of feature vectors
    document_descriptions = [document["description"] for document in documents]
    document_vectors = vectorizer.transform(document_descriptions)

    # Calculate the cosine similarities between the user's interests and the documents' descriptions
    tag_vector = vectorizer.transform([" ".join(tags)])
    similarities = cosine_similarity(tag_vector, document_vectors)

    # Sort the documents by their similarity to the user's interests
    document_similarities = list(zip(documents, similarities[0]))
    document_similarities.sort(key=lambda x: x[1], reverse=True)

    # Return the most similar document
    return document_similarities[0][0]
# User's interests
tags = ["machine learning", "data science"]

# Recommend a video
video = recommend_videos(tags)
if video:
    print(f"Recommended video: {video['title']} ({video['url']})")

# Recommend a document
document = recommend_documents(tags)
if document:
    print(f"Recommended document: {document['title']} ({document['url']})")

