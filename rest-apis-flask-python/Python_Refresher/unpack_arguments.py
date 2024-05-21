def multiply(*args):
    # print(args)

    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 4))