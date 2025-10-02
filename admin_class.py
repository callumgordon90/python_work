import user_class as uc

class Admin(uc.User):
    """Admin is a special type of user. It inherits from the user class and adds priviledges attribute"""
    def __init__(self, name, username, age, country, privileges ):
        """Now define the inherited attributes with 'super' and define the new attribute"""
        super().__init__( name, username, age, country )
        self.privileges = privileges
        
    def show_privileges(self):
        print(f"Here are the privileges: {self.privileges} \n and here they are listed individually:")
        for privilege in self.privileges:
            print(f"- {privilege}")