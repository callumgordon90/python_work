filename = 'poll.txt'

with open (filename, 'w') as file_object:
   
    while True:
         message = input("Why do you like programming? \nPress 'q' to quit")
        
         if message != 'q':
                file_object.write(f"{message}\n")
                print("Thanks for telling us!")
         else:
            break
    
