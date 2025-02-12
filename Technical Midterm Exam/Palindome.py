def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def process_file(file_name):
    """Process the file to check if the sum of numbers is a palindrome."""
    try:
        with open(file_name, 'r') as file:
            line_number = 1
            for line in file:
               
                numbers = [int(x) for x in line.strip().split(',') if x.isdigit()]
                
              
                total_sum = sum(numbers)
                
              
                if is_palindrome(total_sum):
                    print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - Palindrome")
                else:
                    print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - Not a palindrome")
                
                line_number += 1
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        

process_file('numbers.txt')

