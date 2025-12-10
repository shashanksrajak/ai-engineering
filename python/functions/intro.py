# in python if we do not pass an arg, it throws error unlike JS where it gets undefined by default, so 
# better to assign a default value for optional parameters
# this is more strict in python
def create_product(title: str, price: float, description: str = ""):
    new_product = {
        title,
        price,
        description
    }

    print("New Product Created")
    return new_product

if __name__ == "__main__":
    # p = create_product("Shoes", 4500.50, "Trekking shoes")
    p = create_product("Shoes", 4500.50)
    print(p)