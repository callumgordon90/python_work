class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise the attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 22

    def describe_restaurant(self):
        print(f"The name of the restaurant is: {self.restaurant_name}")
        print(f"The type of cuisine served is: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business, and spank my wasp if it won\'t be serving {self.cuisine_type} all day!")

    def num_served(self):
        print(f"This restaurant has served {self.number_served} customers")
    
    def set_num_served(self):
        """This function allows the user to input a number to define the no. of customers"""
        while True:
            self.number_served = input("\nHow many customer\'s have we had today pat? \npress 'q' to quit")
            if self.number_served.lower() == 'q':
                print("Exiting input.")
                break
            print(f"\nwell spank my wasp! we\'ve had {self.number_served} customers!!!")
    
    def increment_num_served(self, inc_served):
        self.number_served += int(inc_served)
        print(f"Current number of customer\'s in {self.restaurant_name} is {self.number_served}")
          

            