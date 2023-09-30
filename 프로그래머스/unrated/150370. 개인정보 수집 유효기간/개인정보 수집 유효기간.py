def solution(today, terms, privacies):
    term={}
    
    for i in terms:
        a=list(i.split())
        term[a[0]]=a[1]
    print(term)
    
    fire=[]
    
    year_t=int(today.split('.')[0])
    month_t=int(today.split('.')[1])
    day_t=int(today.split('.')[2])
    
    for i in range(len(privacies)):
        b=list(privacies[i].split())
        mon=int(term[b[1]])
        year=int(b[0].split('.')[0])
        month=int(b[0].split('.')[1])
        day=int(b[0].split('.')[2])
        
        month+=mon
        day-=1
        
        if day==0:
            month-=1
            day+=28
        
        while month>12:
            year+=1
            month-=12

        
        if year<year_t:
            fire.append(i+1)
            
        if year==year_t and month<month_t:
            fire.append(i+1)
            
        if year==year_t and month==month_t and day<day_t:
            fire.append(i+1)
            
    return fire
            
        
        