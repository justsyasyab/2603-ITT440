import random
 
random.seed(1)
 
def generate_orders(n):
    orders = []
    for i in range(n):
        orders.append({
            "id": i,
            "food": random.choice(["Burger", "Pizza", "Nasi Lemak", "Fries"]),
            "price": round(random.uniform(5, 30), 2),
            "status": "success" if i % 4 != 0 else "failed"
        })
    return orders
