products = []
while True:
    name = input('please enter product name: ')
    if name == 'q':
        break
    price = input('please enter product price: ')
    products.append([name, price])
with open('products.csv', 'w') as f:
    f.write('item,price\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
