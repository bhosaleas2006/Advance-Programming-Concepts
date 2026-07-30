# 1. String Length

s = input("Enter a string: ")
count = 0

for ch in s:
    count = count + 1

print("Length of string:", count)


# 2. Character Count

s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

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

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)


# 6. Replace Characters

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("Modified String:", result)


# 7. Remove Spaces

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print("String without spaces:", result)


# 8. Frequency of a Character

s = input("Enter a string: ")
ch = input("Enter character to find: ")

count = 0

for c in s:
    if c == ch:
        count = count + 1

print("Frequency:", count)


# 9. First and Last Character

s = input("Enter a string: ")

print("First Character:", s[0])
print("Last Character:", s[-1])


# 10. ASCII Values

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))

Based on the uploaded experiment, here are **Questions 11–20** using simple Python syntax. 

```python
# 11. Word Count

s = input("Enter a sentence: ")

count = 1

for ch in s:
    if ch == " ":
        count = count + 1

print("Total Words:", count)


# 12. Longest Word

s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


# 13. Shortest Word

s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)


# 14. Title Case

s = input("Enter a sentence: ")

print("Title Case:", s.title())


# 15. Duplicate Characters

s = input("Enter a string: ")

print("Duplicate Characters:")

for i in range(len(s)):
    count = 1
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count = count + 1
    found = False
    for k in range(i):
        if s[i] == s[k]:
            found = True
    if count > 1 and found == False:
        print(s[i])


# 16. Character Frequency

s = input("Enter a string: ")

print("Character Frequency:")

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1

    found = False
    for k in range(i):
        if s[i] == s[k]:
            found = True

    if found == False:
        print(s[i], "=", count)


# 17. Anagram Check

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

a = sorted(s1.lower())
b = sorted(s2.lower())

if a == b:
    print("Anagram")
else:
    print("Not Anagram")


# 18. Remove Duplicate Characters

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print("After Removing Duplicates:", result)


# 19. Substring Search

main = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in main:
    print("Substring Found")
else:
    print("Substring Not Found")


# 20. Count Occurrences of a Word

sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count = count + 1

print("Occurrences:", count)

# 21. Password Validator

password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
    elif ch.isdigit():
        digit = digit + 1
    else:
        special = special + 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")


# 22. Run-Length Encoding

s = input("Enter a string: ")

i = 0
result = ""

while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
        i = i + 1
    result = result + s[i] + str(count)
    i = i + 1

print("Encoded String:", result)


# 23. String Compression

s = input("Enter a string: ")

i = 0
result = ""

while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
        i = i + 1
    result = result + s[i] + str(count)
    i = i + 1

if len(result) < len(s):
    print("Compressed String:", result)
else:
    print("Original String:", s)


# 24. Most Frequent Character

s = input("Enter a string: ")

maxcount = 0
maxchar = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1
    if count > maxcount:
        maxcount = count
        maxchar = s[i]

print("Most Frequent Character:", maxchar)
print("Frequency:", maxcount)


# 25. Second Most Frequent Character

s = input("Enter a string: ")

first = 0
second = 0
firstchar = ""
secondchar = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1

    found = False
    for k in range(i):
        if s[i] == s[k]:
            found = True

    if found == False:
        if count > first:
            second = first
            secondchar = firstchar
            first = count
            firstchar = s[i]
        elif count > second:
            second = count
            secondchar = s[i]

if secondchar != "":
    print("Second Most Frequent Character:", secondchar)
else:
    print("Not Available")


# 26. Caesar Cipher

text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted = encrypted + chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted = encrypted + chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted = encrypted + ch

print("Encrypted Message:", encrypted)


# 27. Email Validator

email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# 28. Word Frequency Dictionary

s = input("Enter a sentence: ")

words = s.split()

for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count = count + 1

    found = False
    for k in range(i):
        if words[i] == words[k]:
            found = True

    if found == False:
        print(words[i], "=", count)


# 29. Sentence Reversal

s = input("Enter a sentence: ")

words = s.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")


# 30. String Rotation

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, String is Rotation")
else:
    print("No, String is not Rotation")
