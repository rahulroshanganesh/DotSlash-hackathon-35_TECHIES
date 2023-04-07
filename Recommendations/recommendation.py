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


def get_similarity_score(tags1, tags2):
    """
    Calculates the similarity score between two lists of tags using Jaccard similarity.
    """
    set1 = set(tags1)
    set2 = set(tags2)
    return len(set1.intersection(set2)) / len(set1.union(set2))


def recommend(content_type, tags):
    """
    Recommends videos or documents based on the input tags.
    """
    # Select the dataset based on content_type
    if content_type == "videos":
        dataset_to_use = dataset["videos"]
    elif content_type == "documents":
        dataset_to_use = dataset["documents"]
    else:
        return None
    
    # Calculate similarity score for each item in the dataset
    similarities = {}
    for item in dataset_to_use:
        similarities[item["title"]] = get_similarity_score(tags, item["tags"])
    
    # Sort the items in decreasing order of similarity score
    sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top recommendation
    if sorted_items:
        return sorted_items[0][0]
    else:
        return None


# Example usage
tags = ["machine learning"]
recommendation = recommend("videos", tags)
document=recommend("documents",tags)
print(f"Recommended video: {recommendation}")
print(f"Recommended video: {document}")