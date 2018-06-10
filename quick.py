array = [222,3,1,2,7,1,44,33,22,33,42,66,45,65]

i = len(array)
a= i/2

arrays =[]
arrayl =[]
arrayx = []

for k in range (0,i):
    if (array[k]<array[a]):
        arrays.append(array[k])
    else :
        arrayl.append(array[k])


def insertion(arrayi):
    b = len(arrayi)
    for i in range (1,b):

        j = i
        while j > 0 :

            if (arrayi[j] < arrayi[j-1]):
                arrayi[j],arrayi[j-1]=arrayi[j-1],arrayi[j]
            j=j-1

    return arrayi


insertion(arrays)
insertion(arrayl)

arrays.extend(arrayl)
print arrays
