# desired_car = input("What car would you like?")
# print(f"you would like a {desired_car}. We can all dream!")

magic_number = input("give me a number you silly goose:")
magic_number = int(magic_number)

if magic_number % 10 == 0 and magic_number != 0:
    print(f"{magic_number} IS divisible by 10")
else:
    print(f"{magic_number} IS NOT divisible by 10")

