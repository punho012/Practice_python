
def lista (a):
    b = len(a)
    a[1:b-1] = []
    return a

print(lista([4,5,6,7,15]))

