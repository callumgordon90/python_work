class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise the attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is: {self.restaurant_name}")
        print(f"The type of cuisine served is: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business, and spank my wasp if it won\'t be serving {self.cuisine_type} all day!")