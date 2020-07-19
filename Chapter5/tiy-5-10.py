current_users = ['sharon', 'fred']
new_users = ['sharon', 'marie', 'carlos']
for new_users in new_users:
    if new_users in current_users:
        print(f"Adding {new_users}.")
else:
    print(f"Sorry, we don't have {new_users}.")
