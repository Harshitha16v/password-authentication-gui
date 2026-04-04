print("=== Movie Review Sentiment Analyzer ===")
positive_words = ["good", "great", "amazing", "awesome", "nice", "love", "excellent"]
negative_words = ["bad", "worst", "boring", "hate", "terrible", "poor", "awful"]
review = input("Enter your movie review: ").lower()
words = review.split()
pos_count = 0
neg_count = 0
for word in words:
    if word in positive_words:
        pos_count += 1
    elif word in negative_words:
        neg_count += 1
print("\n--- Analysis ---")
print("Positive Words:", pos_count)
print("Negative Words:", neg_count)
if pos_count > neg_count:
    print("Sentiment: Positive 😊")
elif neg_count > pos_count:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")

