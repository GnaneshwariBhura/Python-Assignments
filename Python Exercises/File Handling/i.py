from collections import Counter
import re

def most_frequent_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Clean and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())  # Using regex to extract words, converting to lowercase

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Find the word(s) with maximum occurrence
    max_occurrence = max(word_counts.values())
    most_frequent = [word for word, count in word_counts.items() if count == max_occurrence]

    return most_frequent, max_occurrence

# Example usage:
file_path = 'Python Exercises\File Handling\poem.txt'  # Make sure this file exists in the working directory
words, occurrence = most_frequent_words(file_path)
print(f"Words with maximum occurrence: {words}, Count: {occurrence}")
