import os # operating system

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if 'item,price' in line:
                continue # ignore header
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

def add_item(products):
    while True:
        name = input('please enter product name: ')
        if name == 'q':
            break
        price = input('please enter product price: ')
        products.append([name, price])
    return products

def write_file(filename, products):    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('item,price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('file is exists.')
        products = read_file(filename)
    else:
        print('file is not exists.')
        products = []
    products = add_item(products)
    write_file(filename, products)

main()
