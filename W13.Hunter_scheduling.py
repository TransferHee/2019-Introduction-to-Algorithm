def hunter_scheduling(n,ci,di):
    
    cumsum = 0
    t=n-1
    
    while(t>0):
        x=[]
        idx=[]
        idx2=0
        
        for i in range(len(ci)):
            if(t<=di[i]):
                x.append(ci[i])
                idx.append(i)
        if(x==[]):
            t-=1
            continue
        
        maxv=0
        for i in range(len(x)):
            if(x[i]>=maxv):
                maxv=x[i]
                idx2=i
        cumsum+=maxv
        #print("cumsum=",cumsum,"maxv=",maxv)
        
        ci[idx[idx2]]=0
        t-=1
    return cumsum


n=5
ci=[7,8,10,20,4]
di=[4,1,3,3,2]


cumsum=hunter_scheduling(n,ci,di)

print("Accepted Result",45)
print("My Result", cumsum)


n3=4
ci3=[10,7,8,2]
di3=[3,5,1,1]
print("second",hunter_scheduling(n3,ci3,di3))

n2=10
ci2=[4,2,2,1,10,10,9,10,3,8]
di2=[4,1,8,2,5,3,5,1,7,4]


print("third",hunter_scheduling(n2,ci2,di2))


"""
처음: t=4         7select
2: t=3 10 & 20   20select
3: t=2 10 & 4    10 select
4: t=1 8 & 4      8 select
"""
