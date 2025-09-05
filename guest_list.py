guests = ['julius ceaser' , 'albert einstein' , 'plato' , 'jesus christ']

absentee= guests.pop(1)

absentee= "elvis presley"


message = f"Dear {guests[0].title()} I would like cordially invite you to dinner"
print(message)

message = f"Dear {guests[1].title()} I would like cordially invite you to dinner"
print(message)

message = f"Dear {guests[2].title()} I would like cordially invite you to dinner"
print(message)



news = "i found a bigger motherfucking table!"
print(news.upper())

guests.insert(0, "tupac shakur")
guests.insert(2, "marilyn monroe")
guests.append("bruce lee")

message = f"Dear {guests} I would like cordially invite you to dinner"
print(message)

print("Sorry but now I can only invite two people for dinner")

rejected_guest = guests.pop()
new_message = f"sorry {rejected_guest}, but you are not welcome anymore"
print(new_message)

rejected_guest = guests.pop()
new_message = f"sorry {rejected_guest}, but you are not welcome anymore"
print(new_message)

rejected_guest = guests.pop()
new_message = f"sorry {rejected_guest}, but you are not welcome anymore"
print(new_message)

rejected_guest = guests.pop()
new_message = f"sorry {rejected_guest}, but you are not welcome anymore"
print(new_message)

final_message = f"Don't worry {guests} you are still invited"
print(final_message)

del guests[0]
del guests[0]
guests = guests
guests.append("...")

final_message = f"Don't worry {guests} you are still invited"
print(final_message)

