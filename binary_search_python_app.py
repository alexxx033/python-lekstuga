

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
target = 23

# Här gör vi samma sak men genom linjär sökning, vilken måste gå igenom all data tills resultatet är funnet. Nackdelen med detta sätt är tiden och systemresurser det kräver, speciellt då det är mycket data som skall processas...
#
# for i in my_list:
#    if i == 23:
#        print("found")
#

binary_search(my_list, target)
