"""
16. Print all elements using for loop.  
17. Print all elements using while loop.  
18. Print elements at even indices.  
19. Print elements at odd indices.  
20. Count total elements without using len().
"""
#16. Print all elements using for loop.  

l = ['nitin','nikhil','satyam','shivam','bunty']

for i in l:
	print(i)



#17. Print all elements using while loop. 
l = ['nitin','nikhil','satyam','shivam','bunty']
i = 0
while(i < len(l)):
	print(l[i])
	i += 1

# 18. Print elements at even indices.  
l = ['nitin','nikhil','satyam','shivam','bunty']
for i in range(len(l)):
	if i %2 == 0:
		print(l[i])

#19. Print elements at odd indices.  
l = ['nitin','nikhil','satyam','shivam','bunty']
for i in range(len(l)):
	if i %2 != 0:
		print(l[i])

#20. Count total elements without using len().  
l = ['nitin','nikhil','satyam','shivam','bunty']
new_l = []
count = 0

for i in l:
	if i not in new_l:
		count += 1
print("Total elements in the list is ",count)
