import os # operating system

products = []
if os.path.isfile('products.csv'):
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if 'item,price' in line:
                continue # ignore header
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

