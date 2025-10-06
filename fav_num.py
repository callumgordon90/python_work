import json

fav_num = input("Spank my wasp.. What's your favourite number? ")

filename = 'favourite_number.json'
with open(filename, 'w') as f:
    json.dump(fav_num, f)
    print(f"Well my wasp'll be spanked if we didn't stick your number in the skip!!!")

with open(filename, 'r') as f:
    fav_noom = json.load(f)
    print(f"Well my wasp'll be spanked. Your favourite number is {fav_noom}!!!!")