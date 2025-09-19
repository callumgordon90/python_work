base_list = ["Hi", "Fuck you", "Spank my wasp!", "water me bloody ship down"]

def show_messages(message_list):
    for message in message_list:
        print(message)

# show_messages(cally_list)

base_list = ["Hi", "Fuck you", "Spank my wasp!", "water me bloody ship down"]
base_list_copy = ["Hi", "Fuck you", "Spank my wasp!", "water me bloody ship down"]


def send_messages(cally_list):
    sent_messages = []
    while cally_list: # while list isn't empty
        message = cally_list.pop() # safely pop from the list
        print(message)
        sent_messages.append(message)

    return(cally_list, sent_messages)

   
send_messages(base_list)
print(base_list)
print(base_list_copy)
