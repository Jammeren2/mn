l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

a1 = set(l1)
a2 = set(l2)

n = sorted(list(a1 & a2))

print("одинаковые", n)