def solution(dartResult):
    answer=[]
    number=''
    for i in dartResult:
        if i.isdigit():
            number+=i
        elif i=='S':
            answer.append(int(number))
            number=''
        elif i=='D':
            number=int(number)**2
            answer.append(number)
            number=''
        elif i=='T':
            number=int(number)**3
            answer.append(number)
            number=''
        elif i=='*':
            first=answer.pop()*2
            if answer!=[]:
                second=answer.pop()*2
                answer.append(second)
            answer.append(first)
            
        elif i=='#':
            first=answer.pop()*-1
            answer.append(first)
    return sum(answer)
           
            
        