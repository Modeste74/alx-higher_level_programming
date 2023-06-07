#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(4.5))
print(add_integer(100.3, -2))
print(add_integer(2.5, 4.6))
print([add_integer(i, i ** 2) for i in range(3)])
print(add_integer(999999999998888, 987))
print(add_integer(2.5, 4.6))
print(add_integer(5.78, float('inf')))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
