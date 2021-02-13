def towersHanoi(n, left, mid, right):
    if n == 0:
        return
    elif n == 1:
        right.append(left.pop())
    elif n == 2: # Interschimbarea elementelor, adaugarea lor la right stack
        mid.append(left.pop())
        right.append(left.pop())
        right.append(mid.pop())
    else: # Aplicarea recursive pt combinatiile de stack-uri posibile
        towersHanoi(n - 1, left, right, mid)
        right.append(left.pop())
        towersHanoi(n - 1, mid, left, right)

a = [1, 2, 3, 4, 5]
b = []
c = []  

towersHanoi(5, a, b, c)
print(c)
# print(a.append(1))
# print(len(b) == 0)