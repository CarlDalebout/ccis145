a = 'd'
b = 'e'
c = 'a'


def sort(a, b, c):
    if(a > b):
        a, b = b, a 
    if(a > c):
        a, c = c, a
    if(b > c):
        b, c = c, b

print(sort(int(a),int(b),int(c)))

# if(a <= b and b <= c):
#     print(a, b, c)
# elif(b <= c and c <= a):
#     print(b, c, a)
# elif(c <= b and b <= a):
#     print()
