def check(j1,j2,cap): #function checks jug1 and jug2 capacity is equal to actual capacity or not!
    r=0
    if(j1==cap or j2==cap):
        r=1
    return r

def even(j1_cap,j2_cap,cap): #this function is used for check even capacity of jugs
    j1=0
    j2=0
    c1=j1_cap
    c2=j2_cap  
    while(j1!=cap and j2!=cap and (j1+j2)!=cap):
        j1=c1
        h=check(j1,j2,cap)
        if(h==1):
            return j1,j2
        print(j1,j2)
        x=c2-j2
        j2=x+j2
        j1=j1-x
        print(j1,j2)
        j2=0
        if(j1==cap):
            return j1,j2
        elif(j2==cap):
            return j1,j2
        else:
            j2=j1
            j1=0
            print(j1,j2)
       
        
    


def odd(j1_cap,j2_cap,cap):#this function is used for check odd capacity of jugs
    j1=0
    j2=0
    c1=j1_cap
    c2=j2_cap
    while(j1!=cap and j2!=cap and (j1+j2)!=cap):
        j2=c2
        h=check(j1,j2,cap)
        if(h==1):
            return j1,j2
        print(j1,j2)
        x=c1-j1
        if(x>=j2):
            j1=j1+j2
            j2=0
        else:
            j1=j1+x
            j2=j2-x

        h=check(j1,j2,cap)
        if(h==1):
            return j1,j2
        print(j1,j2)
        j2=c2
        h=check(j1,j2,cap)
        if(h==1):
            return j1,j2
        print(j1,j2)

        x=c1-j1
        if(x>=j2):
            j1=j1+j2
            j2=0
        else:
            j1=j1+x
            j2=j2-x
             
        print(j1,j2)  

        j1=0   
        if(j1==cap):
            return j1,j2
        elif(j2==cap):
            return j1,j2
        else:
            j1=j2
            j2=0
            print(j1,j2)   
        
    

      


j1=int(input("Enter the jug1 capacity:"))
j2=int(input("Enter the jug2 capacity:"))
if(j2>j1):
    j1,j2=j2,j1

capacity=int(input("Enter the capacity you want to measure:"))
c=0
if(capacity>j1):
    capacity=capacity-j1
    c=j1
if(capacity%2==0):
    if(capacity==j1):
        print(j1,"0")
    elif(capacity==j2):
        print(c,j2) 
    else:
        oe1,oe2=even(j1,j2,capacity)
        if(c!=0):
            print(0,oe1)
            print(c,oe1)
        else:
             print(oe1,oe2)    
       
else:
    if(capacity==j2):
        print(c,j2)
    elif(capacity==j1):
        print(j1,"0") 
    else:
      oo1,oo2=odd(j1,j2,capacity)
      if(c!=0):
          print(oo2,"0")
      else:
            print(oo1,oo2)
