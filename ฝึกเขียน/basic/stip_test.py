text = "2019-05-26,15 ,18"

c , v, t = text.strip().split(",")

print(c)
print(v)
print(t)
skip_n_rows=2
with open(r'rio2016.csv',newline= "" , encoding= 'utf8' ) as f :
    for i in range(skip_n_rows):
        f.readline()
    data = f.read()
print(data)
