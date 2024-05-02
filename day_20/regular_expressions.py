### REGULAR EXPRESSIONS ###

# Exercises Level 1

#1.
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\b\w+\b', paragraph.lower())

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = max(word_count, key=word_count.get)
frequency = word_count[most_frequent_word]

print(f'The most frequent word is "{most_frequent_word}" with a frequency of {frequency}.')

#2.
import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction." 
pattern = r"[-]?\d+" 
points = re.findall(pattern, text)

sorted_points = sorted([int(point) for point in points]) 
distance = sorted_points[-1] - sorted_points[0]

print(distance)


#Exercises Level 2

#1.
def is_valid_variable(s): 
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$') 
    return bool(pattern.match(s))


#Exercises Level 3

#1.
def clean_text(text): cleaned_text = "".join([char for char in text if char.isalnum() or char.isspace()]) 
    return cleaned_text

cleaned_text = clean_text(sentence) words = cleaned_text.split() word_count = {}

for word in words: if word in word_count: word_count[word] += 1 else: word_count[word] = 1

most_frequent = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3] print(most_frequent) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
