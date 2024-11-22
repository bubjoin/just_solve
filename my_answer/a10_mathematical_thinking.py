# Mathematical thikning
# from problem to caculatable thing

# Codeforces submit #290478548

# [O, ... ,o]
# How many times needed to change two people
# to move max to left end and min to right end

n=int(input())
a = list(map(int,input().split()))
 
maxidx = a.index(max(a))
minidx = n-1 -a[::-1].index(min(a))
 
ans = 0
ans += maxidx
 
if maxidx > minidx:
    ans += n-1-minidx-1
else:
    ans += n-1-minidx
 
print(ans)