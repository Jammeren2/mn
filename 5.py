f = open("input.txt", "r")
t = f.read()
w = t.replace("\n", " ").split()
wo = set(w)
c = len(wo)
print("Количество различных слов:", c)




