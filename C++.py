
def calculate_product(tup):
    if not tup:  
        return 1
    product = 1
    for num in tup:
        if not isinstance(num, (int, float)): 
            raise ValueError("All elements must be numbers")
        product *= num
    return product

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

try:
    product_tup1 = calculate_product(tup1)
    product_tup2 = calculate_product(tup2)

    print("Product of elements in tup1:", product_tup1)
    print("Product of elements in tup2:", product_tup2)

except ValueError as e:
    print(f"Error: {e}")
