array = [3,1,333,22,345,32,57,86,423,64,5,2,1,77,66,555,425,675,7]

print array

N = len(array)
h=1

while (h < h/3):
    h = 3*h+1

while (h >= 1):
    i = h
    for i in range (h,N):
        j=i

        while j >= h :
           if (array[j] < array[j-h]):
               array[j],array[j-h]=array[j-h],array[j]
           j=j-h
           print array
        i=i+1
    h=h/3

print array
