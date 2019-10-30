s = "1001"
st = "0101"
c = 0
hold = 0
b = []
r = []
h = []

for x in range(len(s)):
    r.append(s[x])

for a in range(len(st)):
    h.append(st[a])

for y in range(len(s)):
    if r[y] == 1 and h[y] == 1:
        c = 0
        hold = 1
    if r[y] == 0 and h[y] == 0 and c != 0:
        c = 0
        hold = 1
    elif r[y] == 1 and h[y] != 1 and hold != 1 and c != 0:
        c = 1
        hold = 0
    elif r[y] != 1 and h[y] == 1 and hold != 1 and c != 0:
        c = 1
        hold = 0
    elif r[y] == 1 and h[y] != 1 and hold == 1 and c != 0:
        c = 0
        hold = 0
    elif r[y] != 1 and h[y] == 1 and hold == 1 and c != 0:
        c = 0
        hold = 0

    b.append(c)

print(b)
