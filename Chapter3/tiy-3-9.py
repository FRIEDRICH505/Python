guests = ['gvozden', 'mirko', 'milovan', 'marija']
message1 = 'I am inviting you '
message2 = ' as a guest'

print(guests[0].title() + ' will not make to come')
guests[0] = 'zoran'
print(message1 + guests[0].title() + message2)

number_of_guests = len(guests)
print('I\'m inviting ' + str(number_of_guests) + ' guests to dinner.')
