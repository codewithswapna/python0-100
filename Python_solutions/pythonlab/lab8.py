'''1.Write a Python program to count the occurrences of each word in a
given sentence
string = “To change the overall look of your document. To change the look
available in the gallery'''

string = "To change the overall look of your document. To change the look available in the gallery"
words = string.lower().replace(".", "").split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")



'''2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n'''

string = "\nBest \nDeeptech \nPython \nTraining\n"

cleaned_string = string.replace("\n", " ").strip()

print("String after removing newlines:")
print(cleaned_string)


'''3. Write a Python program to reverse words in a string
String = “Deeptech Python Training'''

string = "Deeptech Python Training"

reversed_string = " ".join(string.split()[::-1])

print("Reversed words in the string:")
print(reversed_string)



'''4. Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training'''

string = "Welcome to python Training"

string_lower = string.lower()

vowels = "aeiou"

vowel_count = {v: string_lower.count(v) for v in vowels if v in string_lower}

print("Vowels and their counts:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
