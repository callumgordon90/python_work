alien_colour = 'purple'

if alien_colour == 'green':
    print('you just eant 5 points for shooting the alien')
elif alien_colour == 'yellow':
    print('you just earnt 10 points')
else:
    print('you just earnt 15 points')


age = 4

if age < 2:
    print("you are a baby")
elif age >= 2 and age < 4:
    print("you are a toddler")
elif age >= 4 and age< 13: 
    print("you are a child")
elif age >=13 and age < 20:
    print("you are a teenager")
elif age >= 20 and age < 65:
    print("you are an adult")
else: 
    print("you are an elderly person")