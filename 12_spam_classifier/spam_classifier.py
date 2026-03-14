print("Smart Spam Detection System")
print("----------------------------")

# Spam indicators
spam_words = ["win", "free", "offer", "click", "money", "prize", "urgent"]
spam_symbols = ["$", "!!!", "http", "www"]

# User input
message = input("Enter the message: ").lower()

score = 0

# Check spam keywords
for word in spam_words:
    if word in message:
        score += 1

# Check spam symbols
for symbol in spam_symbols:
    if symbol in message:
        score += 1

# Calculate spam probability
probability = (score / (len(spam_words) + len(spam_symbols))) * 100

print("----------------------------")
print(f"Spam Probability: {probability:.2f}%")

# Classification
if probability > 40:
    print("Result: This message is likely SPAM.")
elif probability > 15:
    print("Result: This message looks suspicious.")
else:
    print("Result: This message appears SAFE.")

print("----------------------------")