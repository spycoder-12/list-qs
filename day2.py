"""
1. Access last element of a list.  
2. Add an element to a list using append().  
3. Insert an element at a specific position.  
4. Remove an element from a list.  
5. Delete an element using index. 
"""  
#6. Access last element of a list.  
l = []

n = int(input("Enter Number : "))
for x in range(n):
	elements = input("Enter elements in the list : ")
	l.append(elements)
nl = l[-1]
print(nl)

#7. Add an element to a list using append().

l = ['nitin', 12, 'kundanganj','raebareli',23.3]
l += ['shagun']
print(l)

#8. Insert an element at a specific position.  
l = ['niitn',1,2,3,4,5,6]
n = int(input("Enter an index number you want to add your element at that position : "))
l[n] = 'shagun'
print(l)


#9. Remove an element from a list.  
# Create a list
l = [10, 20, 30, 20, 40]

# Input element to remove
ele = int(input("Enter element to remove: "))

# Create a new list
new_l = []

# Traverse the original list
for x in l:

    # Add only those elements that are not equal to ele
    if x != ele:
        new_l.append(x)

# Display updated list
print("New List =", new_l)


#10. Delete an element using index.
# Create a list
l = [10, 20, 30, 40, 50]

# Input index to delete
index = int(input("Enter index to delete: "))

# Create a new list
new_l = []

# Traverse list using index
for i in range(len(l)):

    # Skip the element at the given index
    if i != index:
        new_l.append(l[i])

# Display updated list
print("New List =", new_l)