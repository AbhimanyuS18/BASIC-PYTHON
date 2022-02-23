#########################    tttttttuuuuuuuppppppllllllleeeeee   ######################
#############################   COUNT   ##################################

# a = (1, 3, 7, 8, 7, 5, 4, 7, 6, 8, 5)
# b=0
# for i in range(len(a)):
#   if a[i]==7:
#     b+=1
# print(b)

# ##############################     INDEX    ###############################

# a = (1, 3, 7, 8, 7, 5, 4, 7, 6, 8, 5)
# for i in range(len(a)):
#   if a[i]==8:
#     print(i)

# a=(5,5,5,8,2,5,6,7)
# for i in range(len(a)):
#   print(a[i])
########################################################################

# a = {2,4,3,62,45,}
# print(a)

# ###################  ADD   ##################
# a={"orange"}
# fruits = {"apple", "banana", "cherry"}
# fruits.add()
# print(fruits)

######################  CLEAR  #################
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)

#####################  COPY #################

# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)

###################### DIFFERENCE  #################

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y) 
# print(z)

######################   DIFFERENCE UPDATE  ####################

# x = {"apple", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y) 
# print(x)

#################################   DISCARD   #############################

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

#############################  INTERSECTION  #########################

# x = {"yellow","apple", "banana","mango", "cherry"}
# y = {"google", "microsoft", "apple","yellow","mango"}
# z = x.intersection(y) 
# print(z)

#######################  INTERSECTION UPDATE  #################

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

######################  ISDISJOINT  ##################

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft","banana", "facebook"}
# z = x.isdisjoint(y)
# print(z)

# ###################### ISSUBSET  ###############

# x = {"a", "b", "c"}
# y = {"f", "e", "d","a"}
# z = x.issubset(y)
# print(z)

# ########################    ISSUPERSET   #################

# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)

#####################  POP   ##############################

# fruits = {"apple", "banana", "cherry"}
# fruits.pop() 
# print(fruits)

#####################  REMOVE   ############

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("apple")
# print(fruits)
 
##########################   SYMMETRIC DIFFERENCE   ##################

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y) 
# print(z)

###################   SYMMETRIC DIFFERENCE UPDATE  #########

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

#################   UNION   ####################

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z)

#############   UPDATE  ##############

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft","tt7u", "apple"}
# x.update(y)
# print(x)

 
# my_string = ["delhi","bangalore","hyderabad"]
# i = 0
# string = []
# while(i<len(my_string)):
#     string.append(my_string[i].upper())
#     i = i+1

# my_string = string
# print (my_string) 

# line = "Hey, how are you"; 
# print (line.split()) 
# print (line.split(' '))
# print (line.split(','))  

a=[2,1,[2,4,6,[3,2,1],7,8,9],5,7]
e=[]
b=[]
x = len(a)
while x>0:
  for i in a:
    if type(i)==list:
      for j in i:
        if type(j)==list:
          for k in j:
            e.append(k) 
          else:
            e.append(j)
      else:
        e.append(i)

  x-=1
print(a)