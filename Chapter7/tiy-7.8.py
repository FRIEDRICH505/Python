sandwich_orders = ['ham & cheese', 'ham', 'dagwood']
finished_orders = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Sandwich orders: {current_sandwich.title()}")
    finished_orders.append(current_sandwich)
print("\nThe following orders was finished:")
for finished_orders in finished_orders:
    print(finished_orders.title())
