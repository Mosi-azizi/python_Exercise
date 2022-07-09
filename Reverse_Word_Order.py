#Write a program (using functions!) that asks the user for a long string
#  containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.


def solution1(L):
    result = L.split()
    result.reverse()
    return " ".join(result)

def solution2(L):
    result = L.split()
    return " ".join(result[::-1])

L = "My name is Sam"
print(solution1(L))
print('---------------------------')
print(solution2(L))
