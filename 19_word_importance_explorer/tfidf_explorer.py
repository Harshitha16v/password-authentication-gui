from sklearn.feature_extraction.text import TfidfVectorizer
print("=== Word Importance Explorer (TF-IDF) ===")
documents = [
    "machine learning is very powerful",
    "deep learning is part of machine learning",
    "AI and machine learning are related fields",
    "python is widely used in machine learning",
    "data science uses machine learning techniques"
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
print("\n--- Top Keywords per Document ---\n")
for i, doc in enumerate(documents):
    scores = X[i].toarray()[0]
    top_indices = scores.argsort()[-3:][::-1]
    print(f"Document {i+1}: {doc}")
    print("Top Keywords:")
    for idx in top_indices:
        print(f" - {feature_names[idx]} ({scores[idx]:.2f})")
    print("-------------------------")