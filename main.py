z = input()
m = z.replace(' ', '')
l = int(m)
x = l.split()
c = x[-1]
a = 0
b = 1
d = x[a]
p = None
for i in range(a, b):
    if d % 2 == 0 and c % 2 == 0 and d > c:
        ' '.join(p)
    if d % 3 == 0 and c % 3 == 0 and d > c:
        ' '.join(p)
        a += 1
        b += 1
print(p)

