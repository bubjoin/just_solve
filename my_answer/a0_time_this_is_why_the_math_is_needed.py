# 최근에 수학이 왜 필요한지 느끼게 해주는 문제를 발견했습니다
# f(n) = -1 + 2 –3 + ... + (-1)ⁿn
# n이 1천조(10의 15승)일 때, f(n)을 계산해서 출력하시오
#
# 시간 제한: 파이썬 PyPy-3 64 기준 0.1초(100ms)
# 파이썬 인터프리터는 보통 1초에 2천만번 정도 계산
# 파이파이는 파이썬보다 평균 4배 정도 빠르다고 알려져있습니다
#
# Time is the most important condition
# Solve it in 0.1 second
# This is the problem that shows why the math is needed to sovle problem
# Solve it if the input n is bigger than 1,000,000,000,000,000
#
# Codeforces #287509426
# f(n) = -1 + 2 –3 + ... + (-1)ⁿn
# Think about it without hint

n = int(input())
 
ans = 0
 
if (n%2)==0:
    ans = int(n/2)
else:
    ans = int((n-1)/2) - n
 
print(ans)


# Hint 1: Solve it within O(1)
# Hint 2: Write down some examples from simple one
# f(2) = -1 + 2 = 1
# f(3) = -1 + 2 –3 = -2
# ...
