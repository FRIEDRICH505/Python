pets = {
'boeta': ['fred'],
'generaal': ['sanet'],
'frommel': ['sonja'],
}
for name, owners in pets.items():
    print(f"\n{name.title()}'s name's of pets are:")
for owner in owners:
    print(f"\t{owner.title()}")