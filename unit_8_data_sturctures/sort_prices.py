def price(item):
    return float(item[1])


def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=price, reverse=True)


items = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(items))

