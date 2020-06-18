names = ['Ellie', 'Matt', 'Tim']

answer = [name[0] for name in names]

print(answer)

numbers = [1, 2, 3, 4, 5, 6]

answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

numbers1 = [1, 2, 3, 4]
numbers2 = [3, 4, 5, 6]

answer3 = [num for num in numbers1 if num in numbers2]
print(answer3)

answer4 = [name[::-1].lower() for name in names]
print(answer4)

answer5 = [num for num in range(1, 101) if num % 12 == 0]
print(answer5)

answer6 = [letter for letter in 'amazing' if letter not in 'aeiou']
print(answer6)

answer7 = [[i for i in range(0, 3)]for num in range(0, 3)]
print(answer7)

answer8 = [[i for i in range(0, 10)]for num in range(0, 10)]
print(answer8)
