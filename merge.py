array = [3,1,44,22,34,32,0,4,3,55,100,20]

i = len(array)

a = i/2

array1 = array[:a]
array2 = array[a:]

print array

def insertionx(arrayx):
    b = len(arrayx)
    for k in range(1,b):
       j = k
       while j > 0 :
           if (arrayx[j] < arrayx[j-1]):
               arrayx[j],arrayx[j-1]=arrayx[j-1],arrayx[j]
           j=j-1
    return arrayx



insertionx (array1)
insertionx (array2)



def arrayend(array3,array4):
    arrayy = [ ]
    while (len(array3) > 0 and len(array4) > 0):

        if array3[0] > array4[0]:
            arrayy.append(array4[0])
            array4.pop(0)
        else :
            arrayy.append(array3[0])
            array3.pop(0)

    if (len(array3)>0):
        arrayy.extend(array3)
    else:
        arrayy.extend(array4)

    print arrayy

arrayend(array1,array2)
