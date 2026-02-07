sentence = input("Enter a sentence: ")

print("\nUppercase:")
print(sentence.upper())

print("\nLowercase:")
print(sentence.lower())

count_a = sentence.lower().count('a')
print(f"\nThe letter 'a' appears {count_a} times.")

if sentence.startswith("Hello"):
    print("\nThe sentence starts with 'Hello'.")
else:
    print("\nThe sentence does not start with 'Hello'.")

print("\nWords in the sentence:")
words = sentence.split()
for word in words:
    print(word)
