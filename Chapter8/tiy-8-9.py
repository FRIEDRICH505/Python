def show_messages(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['Louis', 'Kevin', 'Darryl']
show_messages(usernames)
