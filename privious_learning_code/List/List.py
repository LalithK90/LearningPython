print(" Python - Lists\n")
print("\nAccessing Values in Lists\n")
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print("\nUpdating Lists\n")
list3 = ['physics', 'chemistry', 1997, 2000];
print("Value available at index 2 : ")
print(list3[2])
list3[2] = 2001;
print("New value available at index 2 : ")
print(list3[2])
print("\nDelete List Elements\n")
list4 = ['physics', 'chemistry', 1997, 2000];
print(list4)
del list4[2];
print("After deleting value at index 2 : ")
print(list1)

print("\nCompares elements of both lists.\n")
print("\nGives the total length of the list.\n")
print("\nReturns item from the list with max value.\n")
print("\nReturns item from the list with min value.\n")
print("\nConverts a tuple into list.\n")


print("\nAppends object obj to list\n")
print("\nReturns count of how many times obj occurs in list\n")
print("\nAppends the contents of seq to list\n")
print("\nReturns the lowest index in list that obj appears\n")
print("\nInserts object obj into list at offset index\n")
print("\nRemoves and returns last object or obj from list\n")
print("\nRemoves object obj from list\n")
print("\nReverses objects of list in place\n")
print("\nSorts objects of list, use compare func if given\n")