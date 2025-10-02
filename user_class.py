class User:
    """A user class"""
    def __init__(self, name, username, age, country):
        self.name = name
        self.username = username
        self.age = age
        self.country = country
        self.login_attempt = 0
    
    def describe_user(self):
        print(f"Here are the user\'s details: \nname: {self.name} \n username:{self.username} \nage: {self.age} \ncountry {self.country}")
    
    def greet_user(self):
        print(f"Hello {self.username}")

    def increment_login_attempts(self, incrementation):
        self.login_attempt += int(incrementation)
        print(f"{self.username} has attempted to log in {self.login_attempt} times")

    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"{self.username} has attempted to log in {self.login_attempt} times")

class Privileges:
    """Defining privileges outside the Admin class, then using an instance of 'privileges' as admin attribute"""
    def __init__(self, privileges=["Hello you silly sausages", "spank my wasp", "right bleedin stinger"]):
        self.privileges = privileges
        
    def show_privileges(self):
        print(f"Here are the privileges: {self.privileges} \n and here they are listed individually:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Admin is a special type of user. It inherits from the user class and adds priviledges attribute"""
    def __init__(self, name, username, age, country ):
        """Now define the inherited attributes with 'super' and define the new attribute"""
        super().__init__( name, username, age, country )
        self.privileges = Privileges()
        
        
   



cally_admin = Admin(
    "callum",
    "cally90",
    "35",
    "UK",
)

print(cally_admin.privileges.show_privileges())