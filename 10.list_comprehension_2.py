a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = []

#for i in b:
    #if i in a and b:
        #x.append(i)
#print(x)


if len(a) > len(b):
    for i in a:
        if i in b:
            x.append(i)
elif len(b) > len(a):
    for k in b:
        if k in a:
            x.append(k)

print(x)

