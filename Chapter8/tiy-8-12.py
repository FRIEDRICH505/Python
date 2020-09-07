def make_sandwich(*kind):
    print("\nMaking the following sandwiches:")
    for kind in kind:
        print(f"- {kind}")
make_sandwich('cheese', 'peanut butter', 'polony')