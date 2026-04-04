print("=== Semantic Similarity Checker ===")

# predefined word pairs
similar_pairs = [
    ("happy", "joyful"),
    ("big", "large"),
    ("car", "vehicle"),
    ("smart", "intelligent"),
    ("fast", "quick")
]

word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if (word1, word2) in similar_pairs or (word2, word1) in similar_pairs:
    print("Result: These words are SEMANTICALLY SIMILAR ✅")
else:
    print("Result: These words are NOT strongly similar ❌")

