playlist = {
    'title': 'Patagonia Bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song 1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song 2', 'artist': ['kitty', 'djcat'], 'duration': 5.5},
        {'title': 'song 3', 'artist': ['garfield'], 'duration': 2.5}
    ]
}

total_duration = 0
for song in playlist['songs']:
    total_duration += song['duration']

print(total_duration)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0, len(list1))}

# answer = dict(zip(list1, list2))

print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer2 = {k: v for k, v in person}

# answer2 = dict(person)

print(answer2)

answer3 = {k: 0 for k in 'aeiou'}
# answer3 = dict.fromkeys('aeiou', 0)
print(answer3)

answer4 = {num: chr(num) for num in range(65, 91)}
print(answer4)
