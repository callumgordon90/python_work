active = True


while active:
    prompt = input("Tell me your favourite pizza topping:")
    if prompt.lower() != 'exit':
        print(f"\nYou have selected {prompt.upper()}. \nTo exit program, type 'exit'\n")
    else:
        print("exiting program")
        break