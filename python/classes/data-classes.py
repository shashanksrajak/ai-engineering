# --------- Data classes in Python ----------
# You use dataclasses in Python to quickly create classes that are primarily used to store data. 
# They significantly reduce the amount of boilerplate code needed for standard data-holding tasks.

# The library Pydantic serves a similar but more specialized purpose: 
# to define data structures while also providing data validation and settings management, 
# making it essential for web APIs


# ideally we would be doing something like this for a Product, but a Product is a resuable entity 
# and it makes more sense to define its structure separately rather than adding fields in this func and 
# other func incrementally
def create_product(title: str, price: float, description: str = ""):
    new_product = {
        title,
        price,
        description
    }

    print("New Product Created")
    return new_product

# ------ use dataclass
from dataclasses import dataclass

@dataclass
class Product:
    title: str
    price: float
    description: str = ""

def create_product_v2(product: Product):
    new_product = {
        product.title,
        product.price,
        product.description
    }

    print("New Product Created")
    return new_product

if __name__ == "__main__":
    # p = create_product("Shoes", 4500.50, "Trekking shoes")
    # p = create_product("Shoes", 4500.50)

    product = Product("Shoes", 4900, "Sports shoes for men")
    p = create_product_v2(product)
    print(p)