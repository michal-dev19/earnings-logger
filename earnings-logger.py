import datetime
import json
import sys

STANDARD_PAY = 60
current_date = False

# open and read from 'earnings.json'
try:
    with open("earnings.json", "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}

def verify_date(date):
    """Provides verification to the date format
    
    :param date: str - the input date
    :return: str - verified date"""
    while True:
        try: 
            datetime.date.fromisoformat(date)
            break
        except ValueError:
            print("Input requires proper format (YYYY-MM-DD)")
            date = input()
    return date

def verify_pay(pay, date):
    """Provides verification and amount to the 'pay' and writes it the key date
    
    :param pay: str - 'Y' or 'N' depending on the answer to previously asked question"""

    if pay == 'Y':
        data[date] = STANDARD_PAY
    else:
        print("How much was recieved?")
        data[date] = int(input())
        while data[date] < 0:
            print("Input can't be smaller than 0.")
            data[date] = int(input())

def write_to_memory(data):
    """Writes given data to 'earnings.json'
    
    :param data: dict - empty, or loaded data from earnings.json"""

    json_str = json.dumps(data, indent=4)
    with open("earnings.json", "w") as f:
        f.write(json_str)


# checks the sum in 'earnings.json'
try:
    if sys.argv[1] == '--summary':
        print(sum(data.values()))
        exit()
except IndexError:
    pass

# keeps taking date and its pay for input into 'data'
while True:

    # takes date input
    print("YYYY-MM-DD: ")
    date = input()

    # verifies correct date format
    verify_date(date)

    # if the date is current, signals just 1 loop
    if date == str(datetime.date.today()):
        current_date = True
    
    # takes pay input for said date
    print("Did you recieve standard pay? [Y/N]")

    # if input doesn't match required answer(s), loop begins
    pay = input().upper()
    while pay != 'Y' and pay != 'N':
        print("Please provide valid response [Y/N]")
        pay = input().upper()

    # verifies pay amount
    verify_pay(pay, date)

    # the new key-value pair is written to 'earnings.json'
    write_to_memory(data)

    if current_date:
        break

