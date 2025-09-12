sandwich_orders = ['ham and cheese', 'tuna', 'pastrami', 'crab', 'pastrami', 'marmite', 'pastrami']
finished_sandiches = []

error_message = 'I\'m sorry but we\'ve run out of pastrami'
print(error_message)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for order in sandwich_orders:
    print(f'I made you a {order} sandwhich')
    finished_sandiches.append(order)


print(f'the following sandwiches have been made: {finished_sandiches}')

