prompt = "\nPlease enter a pizza topping you want :"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You have chosen the following pizza topping {topping.title()}!")
