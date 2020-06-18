for number in range(1, 21):
    if number == 13 or number == 4:
        print(f'{number} is unlucky')
    elif number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


for num in range(1, 11):
    print('\U0001f600' * num)

x = 1
while x <= 10:
    print('\U0001f600' * x)
    x += 1
