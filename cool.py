shop = [
    {
        "name": "Verity from Minecraft",
        "price": 39.99,
        "description": "Your personal helper friend! He knows everything."
    },
    {
        "name": "Tung Tung Tung Sahur",
        "price": 1.99,
        "description": "His bat go tung his body go tung and he is a tung."
    },
    {
        "name": "Benjamin Wu",
        "price": 1000000,
        "description": "I am here too, don't buy me plez"
    },
    {
        "name": "Ethan Chen",
        "price": 0.10,
        "description": "Your sleave"
    },
    {
        "name": "weezer album",
        "price": 39.99,
        "description": "A weezer album"
    },
    {
        "name": "1 banana",
        "price": 4.66,
        "description": "Kris, get the banana"
    }
]

def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])
cart=[]
costsp=[]

def choose_item():
    show_items(shop)
    x = int(input("Which item number do you want to buy?"))
    if x >= 5:
        x=5
    print(f"{shop[x]["name"]} has been added to the cart.")
    cart.append(f"{shop[x]["name"]}, ${shop[x]["price"]}")
    costsp.append(shop[x]["price"])

def shope():
    pricesp=0
    while True:
        choose_item()
        x = input("Do you wish to continue?")
        if x == "no":
            break
    print("---------------------------------------------")
    print("This is your cart:")
    for items in cart:
        print(items)
    for i in range(len(costsp)):
        pricesp += costsp[i]
    print(f"Your subtotal is ${pricesp}")
    print(f"TAX: ${pricesp*0.08}")
    print(f"Your total is ${pricesp*1.08}")
    print("---------------------------------------------")

shope()