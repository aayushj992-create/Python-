word1=input("Enter first word")
word2=input("Enter second word")
def common(w1,w2):
    l1=list(w1)
    l2=list(w2)
    l3=[]
    for each in l1:
        if each in l2:
            l3.append(each)
    print(l3)
common(word1,word2)
