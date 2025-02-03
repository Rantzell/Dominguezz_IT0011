
inputs = input("Enter a string: ")


vowel = 0
consonant = 0
space = 0
others = 0


vowels = "aeiouAEIOU"


for char in inputs:
    if char.isalpha():
        if char in vowels:  
            vowel += 1
        else:  
            consonant += 1
    elif char == " ": 
        space += 1
    else:  
        others += 1


print("Vowels:", vowel)
print("Consonants:", consonant)
print("Spaces:", space)
print("Other characters:", others)
