pizzas = ["pepperoni", "hawaian", "ham and cheese", "bbq"]

friend_pizzas = pizzas[:]

pizzas.append(2)

friend_pizzas.append('napoli')

print('my favourite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nmy friends favourite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)