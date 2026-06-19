#01 = print the second largest number in the list
#02 = Sort a list without using sort function
#03 = REMOVE AN ELEMENT FROM THE LIST
#04 = check whether a list is empty.  
#05 = Concatenate two lists.
#06 = Repeat a list N times.  
#08 = Check whether an element exists in a list.

#print the second largest number in the list
l = []
n = int(input("Enter number : "))
for i in range(n):
	elements = int(input("Enter in list : "))
	l.append(elements)
print(l)

largest = l[0]
sec_largest = l[0]

for i in l:
	if i > largest:
		sec_largest = largest
		largest = i
	elif i > sec_largest:
		sec_largest = i
print("Largest Number = ",largest)
print("Second Largest = ",sec_largest)

#Sort a list without using sort function
l = [1,4,5,6,8,2,7]

print('Without sort list : ',l)
for i in range(len(l)):
	for j in range(i+1, len(l)):
		if l[i] > l[j]:
			temp = l[i]
			l[i] = l[j]
			l[j] = temp
print('sorted list : ',l)


#REMOVE AN ELEMENT FROM THE LIST

l = [1,2,3,4,5,6,7,8]
# new_l = []

ele = int(input("Enter element : "))

for i in range(len(l)-1):
	if l[i] == ele:
		l.pop(ele-1)
print(l)

#sec way
l = [1,2,3,4,5,6,7,8]
new_l = []

ele = int(input("Enter element : "))

for i in range(len(l)-1):
	if l[i] != ele:
		new_l.append(i)
print(l)
 
l = [1,23,4,5,6,4,2]

new = l.clear()
print(new)


l = [1,2,3,4,5,6,7,8]
l = []
print(l)

#12. Check whether a list is empty.  
l = []
n = int(input("Enter Number : "))
for x in range(n):
	ele = input("Enter elements : ")
	l.append(ele)

if l == []:
	print("Empty list")
else:
	print("Non empty list")

# 13. Concatenate two lists.  
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l = l1 + l2
print(l)

#14. Repeat a list N times.  

l = [1,2,3,4,5]
n = int(input("Enter numbers : "))

new_l = l*n
print(new_l)

#15. Check whether an element exists in a list. 
l = [1,2,3,4,5,6,7,8]
ele = int(input("Enter element : "))
if ele in l:
	print("Element exist in the list")
else:
	print("Element not  exist in the list")

#16. Print all elements using for loop.  

l = ['nitin','nikhil','satyam','shivam','bunty']

for i in l:
	print(i)
