a = 'Hello Python'
b = 'Ana are mere'
c = 'Pizza Party'
result = a.split()
print(result[0], result[1], sep='_')
print(a.split()[0], a.split()[1], b.replace(' ', '_'), c, sep='_')
print(a.split()[0], a.split()[1], b.replace(' ', '_'), c, '.',sep='_')
print(a + '.', b.replace(' ', '_'), c, '.',sep='_')
print(a.split()[0]*4, a.split()[1], b.replace(' ', '_'), c, sep='_')
x, y = a.split()
print(y, x)