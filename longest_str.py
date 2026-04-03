# Python code​​​​​​‌‌‌‌​‌‌‌​​​‌‌​​​‌‌‌​​​‌​​ below
# Use print("messages...") to debug your solution.
test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
show_expected_result = False
show_hints = False

def find_largest(test_strings):
    mystr=len(test_strings[0])
    for i in test_strings:
        newstr=len(i)
        if mystr<newstr:
            mystr=newstr
    return mystr
print(find_largest(test_strings))
