def store_cars(make, model, colour='black', **car_info):
    car_info['make'] = make
    car_info['model'] = model
    car_info['colour'] = colour
    return car_info

callum_car = store_cars('Volkswagen', 'Bora', mileage = 124253, year='2003')

print(callum_car)