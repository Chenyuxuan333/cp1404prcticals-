"""
Word Occurrences
Estimate: 25 minutes
Actual:  21  minutes
"""

text = input("Text: ").strip().lower()
words = text.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

max_word_length = max(map(len, word_counts))

for word in sorted(word_counts):
    print(f"{word:{max_word_length}} : {word_counts[word]}")
