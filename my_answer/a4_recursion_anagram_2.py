
# abc
# acb
# bac
# bca
# cab
# cba


def anagrammatize(string):
    anagram = []

    # base condition
    if len(string)==1:
        anagram.append(string)
        return anagram

    # recursion
    string_list = list(string)
    for i in range(len(string)):
        string_list_copy = string_list.copy()
        string_list_copy.pop(i)

        for ana in anagrammatize(''.join(string_list_copy)):
            s = string[i] + ana
            anagram.append(s)

    return anagram

    
anagram = anagrammatize('abcd')

for ana in anagram:
    print(ana)

print(len(anagram))
