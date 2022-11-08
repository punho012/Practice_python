num = int(input('please, give me a number: '))
num2 = int(input('please, give me another number: '))

if num % 4 == 0:
    print(f"{num} is a multiple of 4!")
elif num % 2 == 0:
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")

if num2 % num == 0:
    print(f'{num2} can be divided by {num}')
