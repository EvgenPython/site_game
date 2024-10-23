count = 0
for i in range(100, 10000):
    if i < 1000: # 102
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a != b and a != c and b != c:
            count += 1
    else:
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a != b and a != c and a != d and b != c and b != d and c != d:
            count += 1
print(count)
c2 = 0
for i in range(100, 10000):
    if len(set(str(i))) == len(str(i)):
        c2 += 1
print(c2)