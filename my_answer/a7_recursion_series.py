# 1, 3, 6, 10, 15, 21, 28, ...
# n + prev

def make_nth(n):
    if n==1:
        return 1
    nth = n + make_nth(n-1)
    return nth
    
print(make_nth(7))