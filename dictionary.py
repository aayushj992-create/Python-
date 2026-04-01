mydict={"one":1,"two":2,3:"three",4.5:["four","point","five"]}
print(mydict)

print(mydict["one"])
print(mydict[3])


mydict["seven"]=7
print(mydict)


print("two" in mydict)
print("blarg" in mydict)


print(mydict.keys())
print(mydict.values())

for key,val in mydict.items():
    print(key,val)  