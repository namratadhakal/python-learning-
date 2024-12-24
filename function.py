## function that performs sum of two lists separately
# list1 = [2,3,4,2,1,2,3]
# list2 = [6,7,8,5,3]
#
# def calc_sum(a):
#     total = 0
#     for item in a:
#         total = total+item
#     print("total sum of selected list is: ",total)
#
#
# calc_sum(list1)
# calc_sum(list2)

## Different arguments

total = 0
def sum(a,b):
    print("a:", a)
    print("b:",b)
    total = a+b
    print("total in a function :",total)
    return total

sum(3,4)


n = sum(7)
print("total outside a function: ",n)






