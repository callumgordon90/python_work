rivers = {'thames' : 'england', 'seine' : 'france' , 'nile': 'egypt', 'euphrates' : 'iraq' }

for key, value in rivers.items():
    print(f"\nThe river {key.title()} runs through {value.title()}")
    print(key.title())
    print(value.title())