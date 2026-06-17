"""
1. Create a list and print it.  
2. Input N elements into a list.  
3. Print all elements of a list using a loop.  
4. Find length of a list without using len().  
5. Access first element of a list.  


# 1. Create a list and print it.  
l = ['nitin', 20, 3.12, ['Nitin',20,3.13]]
print(l)

#===================================================================================================================================================================================================================
#2. Input N elements into a list.  

l = []
for i in range(5):
	name = input("Enter names : ")
	l.append(name)
rint(l)

#===================================================================================================================================================================================================================
#3. Print all elements of a list using a loop.  
l = ['nitin','nikhil','shagun','anshika','verma','arpita']

for x in l:
	print(x)

#==================================================================================================================================================================================================================

#4. Find length of a list without using len().  
l = []
n = int(input("Enter number to loop running : "))
for x in range(n):
	num = int(input("Enter numbers in the list : "))
	l.append(num)
print(l)

count = 0
new_l = []
for x in l:
	if x not in new_l:
		new_l.append(x)
		count += 1
print('LENGTH OF THE LIST = ',count)


# Second Way

l = ['nitin',20,18.5,True,'Verma']
count = 0

for x in l:
	count += 1
print(count)
"""
#==================================================================================================================================================================================================================

# 5. Access first element of a list.  
l = ['nitin','nikhil','shagun','anshika','verma','arpita']

print(l[0])
