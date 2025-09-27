import restaurant_class as rs

class IceCreamStand(rs.Restaurant):
    """A type of restaurant.. it inherits from restaurant, but adds more characteristics"""
    def __init__(self, restaurant_name, cuisine_type, flavours):
        """Initialise attributes of the parent class (ONLY PASS PARENT CLASS ATTRIBUTES)"""
        super().__init__(restaurant_name, cuisine_type )
        self.flavours = flavours  # child-specific attribute defined here

    def show_flavours(self):
        print(f"{self.restaurant_name} offers the following ice cream flavours:")
        for flavour in self.flavours:
            print(f"- {flavour}")

    