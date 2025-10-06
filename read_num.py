import json

filename = 'favourite_number.json'

with open(filename) as f:
    fav_noom = json.load(f)
    print(f"Well my wasp'll be spanked. Your favourite number is {fav_noom}!!!!")