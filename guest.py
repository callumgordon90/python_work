filename = 'guest.txt'

message=input("Tell us your name\n")
print(f"Welcome {message}")

with open (filename, 'a') as file_object:
    file_object.write(f"{message} has been added to the guestbook\n")