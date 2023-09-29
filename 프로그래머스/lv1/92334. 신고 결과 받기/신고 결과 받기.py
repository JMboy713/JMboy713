def solution(id_list, report, k):
    black_list={i:0 for i in id_list}
    ban_count={i:0 for i in id_list}
    for i in set(report): 
        a=i.split()
        black_list[a[1]]+=1
    banned=[]
    for i in black_list:
        if black_list[i]>=k:
            banned.append(i)
    
    for i in set(report):
        a=i.split()
        if a[1] in banned:
            ban_count[a[0]]+=1
    
    answer=[]
    for i in ban_count:
        answer.append(ban_count[i])
    return answer