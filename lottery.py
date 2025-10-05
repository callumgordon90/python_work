from random import choice

my_ticket = ["A", "L", "T", "C", "S", 345, 43, 11, 5, 678, 88, 65, 48, 33, 22, 21]
cally_ticket = "L"

print(f"Any ticket matching {my_ticket[1]}, {my_ticket[3]}, {my_ticket[5]}, or {my_ticket[7]} wins!!!!")




counter = 0
while choice(my_ticket) != "L":
    counter += 1
    print(f"You have tried {counter} times!")
else:
    print(f"You win!!! {counter} time lucky!!!!")


