number = {
'fred': ['44', '9'],
'sharon': ['35', '11'],
'sanet': ['49', '88'],
'roger': ['38']
    }
for name, numbers in number.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number.title()}")