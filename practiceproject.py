def myfunction(n):
    # O(n)
    for i in range(0,n+1):
        print("First Loop")
    
    # O(log n)
    j=1
    while(j<=n+1):
        print("Second Loop ",j)
        j=j*2
    
    # O(1)
    for i in range(0,100):
        print("Third loop")

# O(n)
myfunction(2)