from datetime import datetime

def convert_date(date_string):
    # Convert the input string to a datetime object
    date_obj = datetime.strptime(date_string, "%m/%d/%Y")
    
    # Convert to human-readable format: "Month day, year"
    human_readable_date = date_obj.strftime("%B %d, %Y")
    
    return human_readable_date

# Get the date input from the user
date_input = input("Enter the date (mm/dd/yyyy): ")

# Convert the date and print the result
converted_date = convert_date(date_input)
print(f"Date Output: {converted_date}")
