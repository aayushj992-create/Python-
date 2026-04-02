def palindrome(w):
    l = []
    for each in range(len(w)-1, -1, -1):
        l.append(w[each])  
    mystr = ""
    mystr = mystr.join(l)

    if w.lower() == mystr.lower():
        print("It is a palindrome")
    else:
        print("No it is not a palindrome")
palindrome("madam")




