def build_profile(first, last, age, colour, hobby, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    user_info['colour'] = colour
    user_info['hobby'] = hobby
    return user_info

callum = build_profile('Callum', 'Gordon', 35, 'green', 'programming')
print(callum)
