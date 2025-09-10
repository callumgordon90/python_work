current_users = ["aDmin", "joHn99", "eMilY12", "baRRy88", "TAnia22", "phILLip33", "Gordon44"]
new_users = ["emmanual", "dardagnan", "charles", "gertrude", "sydney_clairemont", "gordon44"]

lower_current_users = []
for user in current_users:
    user = user.lower()
    lower_current_users.append(user)
print(lower_current_users)

for user in new_users:
    if user.lower() in lower_current_users:
        print(f"I'm sorry, {user}. That username already exists, you will have to create another")
    else:
        print(f"Congratulations! The username {user} is available!")