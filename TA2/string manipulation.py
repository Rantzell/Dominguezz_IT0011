with open('TA2.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list

processed_lines = []
for line in lines:
    cleaned_line = line.strip()  
  
    upper_line = cleaned_line.upper()
    
   
    lower_line = cleaned_line.lower()
    
  
    words = cleaned_line.split()
    
  
    sliced_line = cleaned_line[:3]  
    
  
    replaced_line = cleaned_line.replace("Python", "Java")
    
  
    processed_result = (
        f"Original: {cleaned_line}\n"
        f"Uppercase: {upper_line}\n"
        f"Lowercase: {lower_line}\n"
        f"Words: {words}\n"
        f"Sliced (first 3 chars): '{sliced_line}'\n"
        f"Replaced 'Python' with 'Java': {replaced_line}\n"
        "-----------------------------------"
    )
    
    processed_lines.append(processed_result)  # Add to the list of processed lines


final_output = '\n'.join(processed_lines)


with open('TA2Output.txt', 'w') as file:
    file.write(final_output)  # Write the final output to the file

print("Check TA2Output for result")