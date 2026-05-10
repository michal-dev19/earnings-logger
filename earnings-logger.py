import datetime
# track earnings of every day at my job

# detail the month/day and day of the week

# establish an extra - eg. double runs
## USE A DICTIONARY TO STORE DATES: PAY

STANDARD_PAY = 60

# take input - what is the date?
print("YYYY/MM/DD: ")

# make sure input matches required date format (YYYY/MM/DD)
try: 
    verified_date = datetime.date.fromisoformat(input())
    print(verified_date)
except ValueError as ve:
    print("Input requires proper format (YYYY-MM-DD)")
