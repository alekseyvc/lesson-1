def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 60:
        raise ValueError('Превышена максимальная скидка на товары')
    if discount >= max_discount:
       price_with_discount = price
    else:  
       price_with_discount = price - price * discount / 100
    return price_with_discount

product = {
    'name': 'Iphone 15 PRO MAX', 
    'stock': 10, 
    'price': 120000,
    'discount': 49
}

product['with_discount'] = discounted(product['price'], product['discount'])

print(discounted(100, 60))