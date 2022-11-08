name = input("What is your name?: ")
age = int(input("How old are you?: "))
number = 100
year = 2022
count = (number - age) + year
message = f'Hi {name}! You will be in {count} 100 years old'

reply = int(input("How many times do you want to see that message?: "))

for x in range(reply):
    print(message)
