# Exponent are pretty easy

print(pow(2, 3))
print(2**3)
print(4**5)
print(6**9)
print("")


def power(base, powers):
    result = 1
    for abc in range(powers):
        result = result * base
    return result


print(power(4, 6))
print(power(5, 7))
print("")
