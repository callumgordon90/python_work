people ={
    'pat' : {'first_name' : 'Pat', 'last_name' : 'Thistle', 'age' : 62, 'city' : 'Middlebourough'}, 
    'diedre' : {'first_name' : 'Dierdre', 'last_name' : 'Thistle', 'age' : 60, 'city' : 'Middlebourough'}, 
    'roger' : {'first_name' : 'Roger', 'last_name' : 'Fairfax', 'age' : 52, 'city' : 'Middlebourough'}, 
    'janet' : {'first_name' : 'Janet', 'last_name' : 'Fairfax', 'age' : 54, 'city' : 'Middlebourough'} 
}

# for name, info in people.items():
    # print(name, info['city'])


dog = {'owner_name' : 'pet', 'pet_name' : 'Rover', 'colour' : 'brown', 'food' : 'sausages'}
cat = {'owner_name' : 'Dierdre', 'pet_name' : 'Pussypoo', 'colour' : 'ginger', 'food' : 'catnip'}
rabbit = {'owner_name' : 'Roger', 'pet_name' : 'Thumper', 'colour' : 'grey', 'food' : 'carrots'} 
goldfish = {'owner_name' : 'Janet', 'pet_name' : 'Leviathon', 'colour' : 'gold', 'food' : 'algae'} 


pets=[dog, cat, rabbit, goldfish]


for pet in pets:
    print(pet)