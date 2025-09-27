import restaurant_class as rs

my_restaurant = rs.Restaurant("Cally's Pasty Shop", "Cornish Pasty")

sumny_restuarant = rs.Restaurant("Restaurante de Sumny", "Arroz con judias negras, avocate y platano" )
pat_thistle_restaurante = rs.Restaurant("Pat's Sausage Emporium" , "Cumberland Sausage")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.num_served()
# my_restaurant.set_num_served()

my_restaurant.increment_num_served("22")

# sumny_restuarant.describe_restaurant()
# pat_thistle_restaurante.describe_restaurant()
