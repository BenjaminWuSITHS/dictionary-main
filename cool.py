toilet = [
    {
    "poop": "cool",
    "pee": "No_cool",
    "John": [4,5,6,7],
    },
    {
    "JOHN 2": ["crazy", 56],
    "return of green liquid": 6883838.22232222,
    "COMMUNIST REVOLUTION": "zeeireuieriur",
    }
]
print(toilet[0]["John"][0])

best_buy_items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "Sony Noise Cancelling Headphones",
        "price": 299.99,
        "department": "Audio",
        "description": "Wireless over-ear headphones with industry-leading noise cancellation."
    },
    {
        "name": "Apple iPhone 15",
        "price": 999.99,
        "department": "Mobile Phones",
        "description": "Latest Apple smartphone with A17 chip and advanced camera system."
    }
]

def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

show_items(best_buy_items)