# count the number of characters in string array
# ['ab', 'cdef', 'g', 'hijk', 'lmnop']
# do it recursive way

def count(arr, nc=0):
    if len(arr)==0:
        return nc
    nc+=len(arr)
    new_arr=[]
    for a in arr:
        if a[1:]!='':
            new_arr.append(a[1:])
    print(new_arr)
    return count(new_arr, nc)


c = count(['ab', 'cdef', 'g', 'hijk', 'lmnop'],0)

print(c)