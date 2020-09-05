import collections
def solution(A, K):
    # write your code in Python 3.6
    A=collections.deque(A)
    A.rotate(K)
    shifted=list(A)
    return shifted

solution([3,4,5,6,7,8],3)