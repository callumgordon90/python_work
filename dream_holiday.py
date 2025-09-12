polling_active = True

dream_destinations = {}

while polling_active == True:
    name = input("What is your name?")
    response = input("What is your dream holiday destination?")

    dream_destinations[name] = response

    print(f"The current list of poll participants and their dream holidays: {dream_destinations}")

    repeat = input("Would you like to let someone else take the poll? (yes/no)")
    while repeat.lower() != "yes" and repeat.lower() != "no":
        repeat = input("Enter a valid response: (Yes/No)")
    if repeat.lower() == "no":
        print("End of poll. Exiting program")
        polling_active = False

