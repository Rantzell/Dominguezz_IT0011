from datetime import datetime

def convert_date(date_string):
  
    date_obj = datetime.strptime(date_string, "%m/%d/%Y")
    
    
    human_readable_date = date_obj.strftime("%B %d, %Y")
    
    return human_readable_date

date_input = input("Enter the date (mm/dd/yyyy): ")


converted_date = convert_date(date_input)
print(f"Date Output: {converted_date}")
