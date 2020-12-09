s = [9, 8, 7, 3, 2, 1, 5, 6]
for i in range(len(s)):
    if (not s[i] % 2):
        s[i] = s[i] ** 2
print(s)
