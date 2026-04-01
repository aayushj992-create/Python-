numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

def count_numbers(which, numbers):
    count_even = 0
    count_odd = 0

    if which != "even" and which != "odd":
        return -1

    for each in numbers:
        if each % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    if which == "even":
        return count_even
    else:
        return count_odd


result1 = count_numbers("even", numbers)
print(result1)

result2 = count_numbers("odd", numbers)
print(result2)

result3 = count_numbers("Blarg", numbers)
print(result3)