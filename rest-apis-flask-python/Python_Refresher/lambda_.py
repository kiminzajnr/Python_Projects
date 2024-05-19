# def double(x):
#     return x * 2

sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# doubled = map(double, sequence)

# print(list(doubled))

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)