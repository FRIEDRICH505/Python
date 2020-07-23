prompt = "\nTell me something, and I will repeat it back to you:"
age = input("How old are you? ")
age = int(age)
if age < 3:
    print("\nYou're ticket is free!")
if age <= 12:
    print("\nYou're ticket costs R10!")
if age > 12:
    print("\nYou're ticket costs R15!")

