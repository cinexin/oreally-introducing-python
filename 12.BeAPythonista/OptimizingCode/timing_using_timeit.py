from timeit import timeit, repeat

print(timeit('num = 5; num *= 2', number=1))
print(repeat('num = 5; num *= 2', number=1, repeat=3))
