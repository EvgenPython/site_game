# Підрахувати кількість цілих
# чисел у діапазоні від 100 до 999, у яких є дві однакові цифри.


count = 0
for i in range(100, 1000): # 100 101 102 103
    # i = 100
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a == b:
        count += 1
    elif b == c:
        count += 1
    elif a == c:
        count += 1

print(count)

# print(345 // 100)
# print(345 // 10 % 10)
# print(345 % 10)