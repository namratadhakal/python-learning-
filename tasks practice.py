
# 1.  program to tell a number is odd or even

# var = int(input("Enter a number: "))
# if var%2 == 0:
#     print("Even number")
# else:
#     print("odd number")

# 2. program to enter a dish name and print which cuisine is it.

# Nepali = ["Dhindo","Gundruk", "MOMOS"]
# Indian = ["samosa", "roti","Chicken tikka"]
# Italian = ["Pizza", "pasta","risotto"]
#
# name = input("enter a dish name: ")
#
# if name in Nepali:
#     print("Nepali dish")
# elif name in Indian:
#     print("Indian dish")
# elif name in Italian:
#     print("Italian dish")
# else:
#     print("Not in data sorry !!")

# 3. program to list monthly exp and find its sum using loop
# list1 = [1200,3400,2000,1300]
# total =0
# for i in list1:
#     total = total + i
# print(total)

#4.
# exp = [2309, 3421, 4567]
# total = 0
# for i in range(len(exp)):
#     print('Month:',(i+1), 'Expense:',exp[i])
#     total = total+exp[i]
#     print(total)

# searching lost key in home and when found stop searching

My_key = "bag"
locations = ["chair", "Table", "Bed", "locker","bag","under_pillow"]
for i in locations:
    if i == My_key:
        print("key found in:",i)
        break
    else:
        print("Key is not found in :",i)




