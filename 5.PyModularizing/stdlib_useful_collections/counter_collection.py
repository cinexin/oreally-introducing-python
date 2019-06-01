from collections import Counter
breakfast = ['orange juice', 'bacon', 'bacon', 'bacon', 'bacon', 'egg', 'egg', 'milk', 'tea']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

lunch = ['coca-cola', 'spaguetti', 'bacon', 'bacon', 'bacon', 'fruit', 'fruit', 'tea']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)