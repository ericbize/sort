array = [3,1,2,7,1,44,33,222,22,33,42,66,45,65]
print array

a = len(array)

for i in range (1,a):

    j = i
    while j > 0 :

        if (array[j] < array[j-1]):
            array[j],array[j-1]=array[j-1],array[j]
        j=j-1
        print array
