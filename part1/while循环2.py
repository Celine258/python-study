sandwich_orders = ['1','2','3']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)
print("All the sandwiches has been made.")
