number=input("Enter numbers")
def total(n):
    total=0
    l=list(n)
    for each in l:
        num=int(each)
        total=total+num
    print(total)
total(number)
