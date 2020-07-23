prompt = "\nTell me how old you are:"
age = input("How old are you? ")
age = int(age)
if age < 3:
    print("\nYou're ticket is free!")
if age <= 12:
    print("\nYou're ticket costs R10!")
if age > 12:
    print("\nYou're ticket costs R15!")
while True:
    age = input(prompt)
    if age == 'quit':
        break
else:
    print(f"Enjoy your movie {age.title()}!")