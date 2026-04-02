word=input("Enter a word")
def wordCheck(w):
    const_count=0
    num_count=0
    for each in w:
        if each not in "aeiou0123456789":
            const_count=const_count+1
        elif each in "0123456789":
            num_count=num_count+1

    print("Consonant count:",const_count)
    print("Number count:",num_count)


wordCheck(word)
    
