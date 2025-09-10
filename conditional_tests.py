car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car.upper() == 'Subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi') 

magic_number = 99

print(f"magic number predictions: {magic_number != 909 and magic_number > 22} ")

animal_list = ["frog", "dog", "cat", "mouse", "snake", "fish", "horse", "chicken", "pig", "cow"]

if "frog" not in animal_list:
    print("alas there is no frog")
else:
    print("have a good froggy day")
