
input = input("Enter a string with digits: ")

digit_sum = 0

for char in input:
    if '0' <= char <= '9':  
        digit_sum += int(char)  


print("Sum of digits:", digit_sum)
