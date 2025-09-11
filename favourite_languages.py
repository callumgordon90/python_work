favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}

to_take_poll=['pat','roger','phil','jen']

for name in to_take_poll:
    if name not in favourite_languages.keys():
        print(f"Dear {name}, you should take the poll!")
    else:
        print(f"{name}, you have already taken the poll.")