def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('friedrich', 'brandt',
    location='sasolburg',
    field='programming',
     color='blue',
    height='tall')
print(user_profile)
