newlist = ['Steve', 'Roger', 'Shawn', 'Karli', 'Novak', 'Randy']
message = f"I would like to invite you to dinner {newlist[0].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[1].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[2].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[3].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[4].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[5].title()}."
print (message)
newmessage = f"I am sorry the table will arrive too late, only place for 2 guests!!"
print (newmessage)

newlist = ['Steve', 'Roger', 'Shawn', 'Karli', 'Novak', 'Randy']
list = newlist.pop(0)
print(f"Sorry, i can't invite you anymore for dinner {list.title()}.")
print (newlist)
list = newlist.pop(2)
print(f"Sorry, i can't invite you anymore for dinner {list.title()}.")
print (newlist)
list = newlist.pop(3)
print(f"Sorry, i can't invite you anymore for dinner {list.title()}.")
print (newlist)
list = newlist.pop(1)
print(f"Sorry, i can't invite you anymore for dinner {list.title()}.")
print (newlist)

message = f"I would like to invite you to dinner {newlist[0].title()}."
print (message)
message = f"I would like to invite you to dinner {newlist[1].title()}."
print (message)

del newlist[0, 1]
print(newlist)





