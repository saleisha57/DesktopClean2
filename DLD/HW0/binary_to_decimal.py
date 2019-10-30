f = open('file.txt')
file_stuff = f.read()
st = [p.strip() for p in file_stuff.splitlines()]
f.close()
#s = "11110110100001100101101101101011100000100101111110001110011"
s = st[0]
re = s[::-1]
c = 0

for x in range(len(re)):
    c += ((2**x)*int(re[x]))

o = open('out.txt', 'w')
o.write(str(c))
print(c)
