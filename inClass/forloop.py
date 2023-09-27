n = int(input("give me n: "))
m = int(input("give me m: "))

print('Number\tSquare')
print('------\t-------')

for i  in range(n, m+1):
    print(i, '\t', i * i, sep= '')