# find the first x index

def find_x_idx(s, idx=0):
    if s[idx]=='x':
        return idx
    else:
        return find_x_idx(s, idx+1)

print(find_x_idx('abcdefghijklmnopqrstuvwxyz'))
