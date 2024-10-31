# make an number array the even-number array
# do it recursive way
#
# recursive selection

def pick_even(narr):
    if narr==[]:
        return []
    if (narr[0]%2)==0:
        new_arr = [narr[0]] + pick_even(narr[1:])
    else:
        new_arr = pick_even(narr[1:])
    return new_arr

print(pick_even([1,2,3,4,5,6,7,8]))
