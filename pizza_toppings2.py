active = True
toppings = []

while active == True:
    print(f"Your pizza currently has the following toppings: {toppings}")
    prompt = input("\nAdd a topping to your pizza " "(or type 'exit' to quit): ")

    if prompt.lower() !='exit':
        print(f"\nYou have added {prompt} to the pizza! ")
        toppings.append(prompt)

    else:
        print("exiting program")
        break




            