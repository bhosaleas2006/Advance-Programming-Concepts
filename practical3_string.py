#1.	String Length
str =input("Enter the string")
length =len(str)
print(length)


# 2. Character Count

s = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)

# 3. Reverse a String

s = input("Enter a string: ")

rev = ""
for ch in s:
    rev = ch + rev

print("Reversed String:", rev)

# 4. Palindrome Check

s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 5. Uppercase and Lowercase Count

s = input("Enter a string: ")
upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

# 6. Replace Characters

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("Modified String:", result)

# 7. Remove Spaces

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("String without spaces:", result)

# 8. Frequency of a Character

s = input("Enter a string: ")
ch = input("Enter character to find: ")

count = 0

for c in s:
    if c == ch:
        count += 1

print("Frequency:", count)

# 9. First and Last Character

s = input("Enter a string: ")

print("First Character:", s[0])
print("Last Character:", s[-1])

# 10. ASCII Values

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))

from collections import Counter
import re


# 11. Word Count
sentence = input("Enter a sentence: ")
words = sentence.split()
print("11. Word Count:", len(words))

# 12. Longest Word
print("12. Longest Word:", max(words, key=len))

# 13. Shortest Word
print("13. Shortest Word:", min(words, key=len))

# 14. Title Case
print("14. Title Case:", sentence.title())

# 15. Duplicate Characters
text = input("\nEnter a string for duplicate characters: ")
freq = Counter(text)
duplicates = [ch for ch, count in freq.items() if count > 1]
print("15. Duplicate Characters:", duplicates if duplicates else "No duplicates")

# 16. Character Frequency
print("16. Character Frequency:")
for ch, count in freq.items():
    print(f"{repr(ch)} : {count}")

# 17. Anagram Check
s1 = input("\nEnter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()
print("17. Anagram:", "Yes" if sorted(s1) == sorted(s2) else "No")

# 18. Remove Duplicate Characters
text = input("\nEnter a string: ")
seen = set()
result = ""
for ch in text:
    if ch not in seen:
        seen.add(ch)
        result += ch
print("18. After Removing Duplicates:", result)

# 19. Substring Search
main = input("\nEnter main string: ")
sub = input("Enter substring: ")
print("19. Substring Exists:", "Yes" if sub in main else "No")

# 20. Count Occurrences of a Word
sentence = input("\nEnter a sentence: ")
word = input("Enter word to count: ")
count = sentence.lower().split().count(word.lower())
print("20. Occurrences:", count)

# 21. Password Validator
password = input("\nEnter password: ")
valid = (
    len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"\d", password) and
    re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
)
print("21. Password Valid:", "Yes" if valid else "No")

# 22. Run-Length Encoding
text = input("\nEnter string for Run-Length Encoding: ")
encoded = ""
i = 0
while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    encoded += text[i] + str(count)
    i += 1
print("22. Run-Length Encoding:", encoded)

# 23. String Compression
text = input("\nEnter string for compression: ")
compressed = ""
i = 0
while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    compressed += text[i] + str(count)
    i += 1
print("23. String Compression:", compressed if len(compressed) < len(text) else text)

# 24. Most Frequent Character
text = input("\nEnter string: ")
freq = Counter(text)
most = freq.most_common(1)[0]
print("24. Most Frequent Character:", most[0], "Frequency:", most[1])

# 25. Second Most Frequent Character
if len(freq) >= 2:
    second = freq.most_common(2)[1]
    print("25. Second Most Frequent Character:", second[0], "Frequency:", second[1])
else:
    print("25. Second Most Frequent Character: Not available")

# 26. Caesar Cipher
message = input("\nEnter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""
for ch in message:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        decrypted += chr((ord(ch) - base - shift) % 26 + base)
    else:
        decrypted += ch

print("26. Encrypted:", encrypted)
print("26. Decrypted:", decrypted)

# 27. Email Validator
email = input("\nEnter email: ")
pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
print("27. Valid Email:", "Yes" if re.match(pattern, email) else "No")

# 28. Word Frequency Dictionary
paragraph = input("\nEnter paragraph: ")
word_freq = Counter(paragraph.lower().split())
print("28. Word Frequency:")
for word, count in word_freq.items():
    print(word, ":", count)

# 29. Sentence Reversal
sentence = input("\nEnter sentence: ")
print("29. Reversed Sentence:", " ".join(sentence.split()[::-1]))

# 30. String Rotation
str1 = input("\nEnter first string: ")
str2 = input("Enter second string: ")
if len(str1) == len(str2) and str2 in (str1 + str1):
    print("30. String Rotation: Yes")
else:
    print("30. String Rotation: No")
