active = True

while active:
    guest_age = input("How old are you?")
    guest_age = int(guest_age)

    if guest_age < 3:
        print("The ticket is free")
        active = False
    elif guest_age >= 3 and guest_age <= 12:
        print("The ticket is ten dollars") 
        active = False
    elif guest_age > 12:
        print("The ticket is fifteen dollars")
        active = False