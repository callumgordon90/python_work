
while True:

    num_1 = input("type a number ")
    num_2 = input("type a second number ")
    try:
        result = int(num_1) + int(num_2)
        print(f"The answer is {result}")
        print("\nThank you and good night")
        break
    except ValueError:
        print("Error: Please provide a numerical input. Thank you")
    

