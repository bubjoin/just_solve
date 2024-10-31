# r row lines, c column lines
# from (0,0) to (r-1, c-1)
# count the number of all the shortest paths
# i.e. you can go right, go down only

# def count_shortest(x, y):
#     if (x==0) or (y==0): # 'or'! if it is 'and', it never ends
#         return 1
    
#     c = count_shortest(x-1, y) + count_shortest(x, y-1)
#     return c


# # for 3 row lines, 7 column lines
# print(count_shortest(2, 6))

# for (1000, 1000) maximum recursion depth exceeded
# how about make a map in advance?
# how about make a memo and use it again? ---> "Memoization"

def count_shortest(x, y, m={}):
    if (x==0) or (y==0):
        return 1
    
    if m.get((x,y)) is None:
        m[(x,y)] = count_shortest(x-1, y) + count_shortest(x, y-1)
    
    return m[(x,y)]

# for 3 row lines, 7 column lines
print(count_shortest(2,6))