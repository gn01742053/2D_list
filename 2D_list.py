products = []
while True:
    name = input('please enter product name: ')
    if name == 'q':
        break
    price = input('please enter product price: ')
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)
