def a(x):
    s=len(x)
    b=[]
    for i in range (s):
        k=i+1
        for j in range(k,s):
            if x[i]==x[j] and x[j] not in b :
                b.append(x[i])
    print(b)
a([1,2,3,'c',4,5,6,7,'a',8,9,1,'c',1,2,4,4,5,6,7,7])
a((1,2,3,4,4,5,5,6,6,'a',3,4,5,'b'))
    
