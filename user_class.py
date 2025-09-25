class User:
    """A user class"""
    def __init__(self, username, password, age, country):
        self.username = username
        self.password = password
        self.age = age
        self.country = country
    
    def describe_user(self):
        print(f"Here are the user\'s details: {self.username, self.password, self.age, self.country}")
    
    def greet_user(self):
        print(f"Hello {self.username}")