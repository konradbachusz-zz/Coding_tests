
from collections import Counter
def solution(A):
    mydict=Counter(A)
    return list(mydict.keys())[list(mydict.values()).index(1)]


solution([1,1,3,3,5,5,9,9,7])