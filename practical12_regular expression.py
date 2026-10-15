import re
# 1.  Write a Python program using regular expressions to extract all digits from a given string.


text = "My roll number is 126 and marks are 85"
print(re.findall(r'\d', text))


# 2.  Accept a sentence and display all words beginning with the letter A or a.
text = "Adarsha is an active and amazing student"
print(re.findall(r'\b[Aa]\w*', text))


# 3.  Write a program to count the occurrences of vowels in a given string using regular expressions.
text = "Hello Python Programming"
vowels = re.findall(r'[aeiouAEIOU]', text)
print("Vowel Count:", len(vowels))


# 4.  Write a program to extract all uppercase letters from a given string.
text = "Hello PYTHON World"
print(re.findall(r'[A-Z]', text))


# 5.  Write a program to identify all spaces, tabs, and newline characters in a text.
text = "Hello World\tPython\nProgramming"
print(re.findall(r'[ \t\n]', text))


# 6.  Write a program to replace multiple consecutive spaces with a single space.
text = "Python    is   very    easy"
print(re.sub(r' +', ' ', text))


# 7. Accept a sentence and display all words containing exactly five characters.
text = "Hello there Python makes coding easier"
print(re.findall(r'\b\w{5}\b', text))


# 8. Write a program to identify all words ending with the letter s.
text = "Cats dogs birds and horses"
print(re.findall(r'\b\w+s\b', text, re.IGNORECASE))


# 9. Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.
text = "Hello@Python! 123 #Easy."
print(re.sub(r'[^A-Za-z0-9 ]', '', text))


# 10. Write a program to count the number of words in a sentence using regular expressions.
text = "Python is easy to learn"
words = re.findall(r'\b\w+\b', text)
print("Word Count:", len(words))


# 11. Write a program to validate a 10-digit Indian mobile number using a regular expression.
mobile = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# 12. Accept an email address and check whether it follows a reasonable email format.
email = input("Enter email: ")

if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
    print("Valid Email")
else:
    print("Invalid Email")


# 13. Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
text = "Dates are 15-08-2026 and 01-01-2027"
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text))


# 14. Write a program to identify web addresses beginning with http:// or https://.
text = "Visit https://example.com and http://test.com"
print(re.findall(r'https?://[^\s]+', text))


# 15. Write a program to extract all hashtags from a social media post.
text = "Learning #Python and #Programming is #Easy"
print(re.findall(r'#[A-Za-z0-9_]+', text))


# 16. Write a program to check whether a password contains at least eight characters, one uppercase letter, one lowercase letter, one digit, and one special character.
password = input("Enter password: ")

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")


# 17. Write a program to identify consecutive repeated words in a sentence, ignoring case differences.
text = "Python is is easy and AND useful"
print(re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE))


# 18. Write a program to extract six-digit Indian PIN codes from a paragraph.
text = "My PIN is 416001 and another PIN is 400001"
print(re.findall(r'\b[1-9]\d{5}\b', text))


# 19. Write a program to check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.
vehicle = input("Enter vehicle number: ")

if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}', vehicle):
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")


# 20. Write a program to extract file extensions from filenames in a given string.
text = "Files are notes.txt photo.jpg program.py data.csv"
print(re.findall(r'\.([A-Za-z0-9]+)\b', text))


# 21. Write a program to remove HTML tags, extra whitespace, and unwanted punctuation from a text document.
text = "<p>Hello,   Python!</p> <b>Welcome!!!</b>"
text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[^\w\s.]', '', text)
print(text.strip())


# 22. Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions.
text = "Invoice No: INV123 Date: 15-08-2026 Amount: Rs. 2500.50"

print("Invoice Number:", re.findall(r'INV\d+', text))
print("Date:", re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text))
print("Amount:", re.findall(r'Rs\.?\s*[\d,]+(?:\.\d{2})?', text))


# 23. Write a program to identify single-line comments in Python source code. Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
text = "x = 10  # number\ny = 20\n# This is a comment"
print(re.findall(r'(?m)#.*$', text))


# 24. Validate product codes following the pattern ABC-1234-XY, where letters and digits must appear in the specified positions.
code = input("Enter product code: ")

if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', code):
    print("Valid Product Code")
else:
    print("Invalid Product Code")


# 25. Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions.
text = "Name: Adarsh, Roll: 101, Marks: 85"

name = re.findall(r'Name:\s*([A-Za-z ]+)', text)
roll = re.findall(r'Roll:\s*(\d+)', text)
marks = re.findall(r'Marks:\s*(\d+)', text)

print("Name:", name)
print("Roll Number:", roll)
print("Marks:", marks)


# 26. Extract DOI identifiers, publication years, email addresses, and URLs from a collection of research paper references.
text = "Paper DOI: 10.1234/abcd.5678, Year: 2024, Email: abc@example.com, URL: https://example.com"

print("DOI:", re.findall(r'\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text))
print("Year:", re.findall(r'\b(?:19|20)\d{2}\b', text))
print("Email:", re.findall(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', text))
print("URL:", re.findall(r'https?://[^\s,]+', text))
