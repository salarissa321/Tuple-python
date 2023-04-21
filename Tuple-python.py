


#----------
#--- Tuple Methods-----
#----------
# [1] Tuole Items Are Enclosed in Parentheses
# [2] You can Remove The Parentheses If You Want
# [3] Tuple Are Ordered , To Use Index To Accsess Item
# [4] Tuple Are Immutable => You can not Add Or Delete
# [5] Tuple Items is not Unique
# [6] Tuple Can Have different Data Types 
# [7] Operators Used In String and Lists Available in Tuples
#----------------

# Tuple Syntax & Type Test

myTuple1 = ("Salar" , "Issa")
myTuple2 = "Salar" , "Issa"

print(myTuple1) # ('Salar', 'Issa')
print(myTuple2) # ('Salar', 'Issa')

print(type(myTuple1)) # <class 'tuple'>
print(type(myTuple2)) # <class 'tuple'>

# Tuple Indexing

myTuple3 = (1,2,3,4,5)
print(myTuple3[0]) # 1
print(myTuple3[-1]) # 5
print(myTuple3[-3]) # 3

# Tuple Assign Values

myTuple4= (1,2,3,4,5,6,7,8)
# myTuple4[2] = "Three"  
print(myTuple4) # TypeError: 'tuple' object does not support item assignment


# Tuple Items

myTuple5 = ("Salar" , "Salar" , 1, 2, 40.42 , True)
print(myTuple5[1]) # Salar
print(myTuple5[-1]) # True