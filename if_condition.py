x,y=1000,100

if(x<y):
    print("x is less than y")
else:
    print("x is greater than y")


x,y=100,100

if(x<y):
    print("x is less than y")
elif(x==y):
    print("x is equal to y")
else:
    print("x is greater than y")

result="x is less than y" if(x>y) else "y is greater than x"
print(result)