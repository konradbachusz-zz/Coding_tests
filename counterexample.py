def find_min(A):
    ans = 0
    for i in range(1, len(A)):
        if A[i] < ans:
            ans = A[i]
    
    return ans


def solution(N):
    # write your code in Python 3.6
    arr=[N,N+1,N+2,N+3]
    return arr


for i in range(1,1001):
    if find_min(solution(i))!=0:
        print(find_min(solution(i)))