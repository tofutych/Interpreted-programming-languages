def make_buyers_db():
    data = list()
    with open('input.txt') as f:
        for line in f.readlines():
            data.append(line.rstrip().split())

    return data


def make_customers_db():
    data = sorted(make_buyers_db(), key=lambda elem: elem[0])
    customers = dict()
    for elem in data:
        customers[elem[0]] = dict()

    for elem in data:
        if elem[1] in customers[elem[0]].keys():
            customers[elem[0]][elem[1]] += int(elem[2])
        else:
            customers[elem[0]][elem[1]] = int(elem[2])

    return customers


def printer():
    customers = make_customers_db()
    with open('output.txt', 'a') as f:
        for key in customers.keys():
            f.write(f'{key}:\n')
            for product in customers.get(key).keys():
                f.write(f'{product} {customers.get(key).get(product)}\n')


printer()
