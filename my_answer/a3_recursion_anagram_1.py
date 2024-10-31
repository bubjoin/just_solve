# 애너그램은 주어진 문자열의 구성 알파벳으로 만들 수 있는 모든 문자열이다
# 다음과 같은 순서로 애너그램에 출력되는 함수를 만드시오
#
# Anagram function with a given string
# The output order with input 'abc' is like:
#
# abc
# bac
# bca
# acb
# cab
# cba

def anagrammatize(string):
    anagram = []

    if len(string)==1:
        anagram.append(string)
        return anagram

    for a in anagrammatize(string[1:]):
        a_list = list(a)    
        for i in range(0, len(a_list)+1):
            a_list_copy = a_list.copy()
            a_list_copy.insert(i, string[0])
            anagram.append(''.join(a_list_copy))

    return anagram


anagram = anagrammatize('abcd')

for ana in anagram:
    print(ana)

print(len(anagram))
