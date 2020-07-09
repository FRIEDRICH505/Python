guestlist = ['Roger', 'Karli', 'Rafa']
print('Rafa')

del guestlist[2]
print(guestlist)

guestlist.insert(0, 'Novak')
print(guestlist)

newlist = ['Roger', 'Karli', 'Novak']
message = f"I would like to invite you to dinner {newlist[0].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[1].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[2].title()}."
print (message)





