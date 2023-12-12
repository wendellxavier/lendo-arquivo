file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')
file.seek(0,0)

print(file.read())
print(30*'#')

file.seek(0,0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(30*'#')

file.seek(0,0)
for linha in file.readlines():
    print(linha, end='')

file.close()