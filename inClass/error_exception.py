x = 5
y = 0

try:
    s = x / y
    print("result = ", s)
except (ZeroDivisionError) as e:
    print(e)

print("Goodby ... ")