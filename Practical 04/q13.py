import datetime

# Get user input
year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))

try:
    # Create a date object
    given_date = datetime.date(year, month, day)

    # Calculate the next day
    next_date = given_date + datetime.timedelta(days=1)

    # Display the result
    print(f"The next date is [yyyy-mm-dd] {next_date.year}-{next_date.month}-{next_date.day}")

except ValueError:
    print("Invalid date! Please enter a valid year, month, and day.")
