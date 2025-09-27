class User:
    """A user class"""
    def __init__(self, name, username, age, country):
        self.name = name
        self.username = username
        self.age = age
        self.country = country
    
    def describe_user(self):
        print(f"Here are the user\'s details: \nname: {self.name} \n username:{self.username} \nage: {self.age} \ncountry {self.country}")
    
    def greet_user(self):
        print(f"Hello {self.username}")