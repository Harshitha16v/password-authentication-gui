print("=== Text Challenge Analyzer ===")

# sample slang words
slang_words = ["u", "r", "wt", "lol", "omg", "btw"]

# sample emojis
emojis = ["😂", "🔥", "😊", "😅", "😍"]

sentence = input("Enter a messy sentence: ").lower()

print("\n--- Analysis ---")

# detect slang
found_slang = [word for word in slang_words if word in sentence]
print("Slang Words Found:", found_slang)

# detect emojis
found_emojis = [e for e in emojis if e in sentence]
print("Emojis Found:", found_emojis)

# detect repeated letters (typo style)
import re
typos = re.findall(r'(.)\1{2,}', sentence)

print("Repeated Letter Issues:", typos)

print("\n--- Suggested Cleaning ---")
print("→ Convert to lowercase")
print("→ Remove emojis")
print("→ Expand slang words")
print("→ Correct spelling mistakes")
