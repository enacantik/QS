f.read()
print(f.read())
f.read()


f.readline()

f.readline()

f.readline()

for line in f:
    print(line, end='')

f.write('This is a test\n')
print(f.write('This is a test\n'))

value = ('the answer', 42)
s = str(value) 
f.write(s)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)  
f.read(1)
f.seek(-3, 2) 
f.read(1)