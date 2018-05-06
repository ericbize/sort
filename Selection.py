array = [3,1,2,44,32,33,222,134,134,122,11,1]
print array

a = len(array)

for i in range (a) :
    min = array[i]
    #print min

    j = i+1
    while j < a:
        #print j
        #print " here"
        if (array[j] < min):
           min,array[j]=array[j],min
        array[i] = min
        print array
        j = j+1
print array
