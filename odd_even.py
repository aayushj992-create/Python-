def odd_even(n):
    total=0
    for each in range(1,n):
        if(each%2==0):
            total=total+each
    return total
number=int(input("enter a number"))
print(odd_even(number))
        
    
