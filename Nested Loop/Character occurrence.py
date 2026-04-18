word = input("Enter a word : ")

character = input("Enter any one character from the word : ")

count = 0

i = 0

while i < len(word):

    if word[i] == character:

        count = count + 1

    i = i + 1

print("Number of character occurrences:", count)