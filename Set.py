#D21CE171 - Hetvi Meghani

#Practical - 1
# Write a Python program to add member(s) in a set and clear a set

#Declaration
a = {10,20,40,50}
#Add element in set
a.add(39)
#Print
print(a)
#clear the set
a.clear()
#Prnt
print(a)

# Set Practical - 2
# Write a Python program to remove an item from a set if it is present in the set.

#Declaration
a = {5,8,3,4,45,96,25}
b = 96
#remove element form set
a.discard(b)
#Print
print(a)

#Practical - 3
# Write a Python program to create an intersection, Union, difference of sets.

#Declaration
a = {1,2,3,4,5,6,7,8,9}
b = {10,11,12,13,14,15,16,17,18}
#Print
print("Union : ", a | b)
print("Intersection : ", a & b)
print("Difference : ", a - b)

# Set Practical - 4
# Write a Python program to find maximum and the minimum value in a set.

#Declaration
a = (90,0,630,44,159,100)
#Print minimum and maximum values
print("Minimum value is : ",min(a))
print("Maximum value is : ",max(a))

# Set Practical - 5
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# Delcaration
a=['kiwi', 'rose', 'banana', 'rose','rose','apple']
b = (1,2,3,4,5,1,3,1,1,4,1,1)
c = {"car": "Maruti","car":"Maruti","year":"2001"}
# Logic
from collections import Counter
l = Counter(a)
l.most_common(1)
t = Counter(b)
t.most_common(1)
d = Counter(c)
d.most_common(1)
# Print Common Element In List
print ("",l.most_common(1))
# Print Common Element In Tuple
print ("",t.most_common(1))
# Print Common Element In Dictionary
print ("",d.most_common(1))
