def greeting_user():
    """This function greets the user"""
    message = "Spank my wasp"
    print(message)

def favourite_book(title):
    """This function prints the user's favourite book"""
    print(f"My favourite book is:{title}")

def make_shirt(size="large", text="I love python"):
    """This function takes inputs to make a shirt"""
    return(f"The size of this shirt is: {size} \nand the text of the shirt says:{text}\n")

shirt_1 = make_shirt()
shirt_2 = make_shirt(size="medium")
shirt_2 = make_shirt(text="Python is okay I suppose")

# print(shirt_1, shirt_2)
    




def describe_city(name, country ="Spain"):
    print(f"{name} is in {country}")

describe_city("Valencia")   
describe_city("Barcelona") 
describe_city("London", "UK")

# favourite_book("The wind in the bloomin willows")
# greeting_user()