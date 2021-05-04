import io

massage = 'This is a normal string.'

f = io.StringIO(massage)
print(f.read())

print(f.write(" Second line written to file like object"))

print(f.read())
