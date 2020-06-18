# print("hey how's it going?")
# response = input()
# while response != 'stop copying me':
#     print(response)
#     response = input()

from random import randint

num = randint(1, 10)
while num != 5:
    print(f'{num} != 5')
    num = randint(1, 10)
print(f'{num} == 5')
