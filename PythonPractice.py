#list

'''l = list(range(1,10,20))
print(10)
print(type(10))



l= [1,2, 'A','Z']
l.sort()
print(l)

n=[50,20,60]
n.sort(reverse = False)
print(n)'''


# To display unique vowels in a word
vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Enter a word: ")
word_lower = word.lower()
unique_vowels = {char for char in word_lower if char in vowels}

if unique_vowels:
    print("Unique vowels in the word:", ", ".join(sorted(unique_vowels)))
else:
    print("No vowels found in the word.")



#