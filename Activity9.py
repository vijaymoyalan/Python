# Activity 9

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print("First List ", list1)
print("Second List ", list2)
List3 = []
for num in list1:
    if (num % 2 != 0):
        List3.append(num)
for num in list2:
    if (num % 2 == 0):
        List3.append(num)
print("Resulted List is:")
print(List3)