with open("demo.txt","r" ) as file:
    content = file.read()

print("Total number of words")
words = content.split()
print( len(words) )

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word,0) + 1
print("Frequecy of each word")
print(word_freq)

print("Number of vowels")
count = 0
for ch in content.lower():
    if ch.isalpha():
        if ch in "aeiou":
            count +=1
print(count)

print("Most 3 frequent words")

from collections import Counter 
word_count = Counter(words)
print(word_count.most_common(3))    

