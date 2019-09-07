from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
print(total)

penny = Decimal('0.01')
total = total.quantize(penny)
print(total)