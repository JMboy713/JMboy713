from itertools import combinations
def solution(nums):
    comb=[]
    for i in combinations(nums,3):
        comb.append(sum(i))
    count=len(comb)
    for i in comb:
        for j in range(2,i):
            if i%j==0:
                count-=1
                break
    return count

    