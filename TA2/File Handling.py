
with open('TA2.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is my Technical Activity 2\n")
    file.write("Topic : File Handling\n")

with open('TA2.txt', 'r') as file:
    for line in file:
        print(line.strip()) 
        
with open('TA2.txt', 'a') as file:
    file.write("Add this on my TXT\n")

with open('TA2.txt', 'r') as file:
    print("\nUpdated file contents:")
    for line in file:
        print(line.strip())

