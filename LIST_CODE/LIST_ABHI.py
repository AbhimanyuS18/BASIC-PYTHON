############################  APPEND #########################

# a=[2,5,2,5,2,6,3,9,7]
# b=[5,9]
# for i in range(len(a)-1,-1,-1):
#     if i == (len(a)-1):
#         a.insert(i+1,b) 
# print(a)

# a=[5,5,66,6,5,65,8]
# b=input("Enter something :-  ")
# for i in range(len(a)):
#     if i <= (len(a)-1):
#         b=a[i]
#     a.append(b)
# print(a)


# a=3
# b=-2
# print(a%b) 


# a=False
# b=True
# c=int(input())
# while a<c:
#     print(a)
#     a+=b

# a=[,6,6,6]
# b=[5,44]
# for i in range(len(a)-1,-1,-1):
# a=['ram',"ram",'shyam']
# b=a.count('ram')

# x=int(input())
# a=len(str(x))
# c=10
# while a>0:
#     b=a%c
#     c=c*10
#     print(b))
#     a-=1

# for r in range(1,9):
#     for c in range(1,5):
#         if c==1 and r in (2,3,4,5,6,7,8):
#             print('@',end='  ')
#         elif c==2 and r in (1,5,6):
#             print('@',end='  ')
#         elif c==3 and r in (2,3,4,7):
#             print('@',end='  ')
#         elif c==4 and r==8:
#             print('@',end='  ')
#         else:
#             print('',end='  ') 
#     print()

# for r in range(1,12):
#     for c in range(1,11):
#         if c==1 and r in (5,6):
#             print('@',end='  ')
#         elif c==2 and r in (4,7):
#             print('@',end='  ')
#         elif c in (3,7) and r in (3,8):
#             print('@',end='  ')
#         elif c==4 and r in (2,9):
#             print('@',end='  ')
#         elif c==5 and r in (1,10):
#             print('@',end='  ')
#         elif c==6 and r in (2,7,9):
#             print('@',end='  ')
#         elif c==8 and r in (4,7,9):
#             print('@',end='  ')
#         elif c==9 and r in (5,6,10):
#             print('@',end='  ')
#         elif c==10 and r==11:
#             print('@',end='  ')
#         else:
#             print(' ',end='  ')
#                                                                                                                                                                                                                                               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, 


# a=[20,39,79,86,55,33,55,69]
# l=len(a)
# indax=0
# total=0
# while indax<=l:
#     total+=a[indax]
#     print(total)
#     indax+=1

# num=[30,10,15,33,22,55,44,60,24,36,39]
# l=len(num)
# indax=0
# count=0
# while indax<l:
#     if num[indax]>=20 and num[indax]<=40:
#         count+=1
#     indax+=1
# print(count)





# num=[20,10,33,22,50,32,70,40]
# a=len(num)
# l=sorted(num)
# print(l[a-1])


# a=['arun','aadi','barat','ujjwal']
# a.reverse()
# print(a)

# EK BDA EK CHOTA ALFABAT

# a=input('name')
# c=len(a)
# h=1
# b=''
# for i in a:
#     if h%2==0:
#         b+=i.upper()
#     else:
#         b+=i
#     h+=1
# print(b)


# # LIST PALINDROME 

# a=list(input(""))
# b=a.copy()
# b.reverse()
# # print(b)
# if b==a:
#     print("palindrome")
# else:
#     print("not palindrome")  

  
# a=list(input("enter: "))
# b=a.copy()
# c=(b[::-1])
# #print(c)
# if c==a:
#     print("paindrome")
# else:
#     print("not palindrome")


#  a=list(input("enter: "))
# #  b=a.copy


# EVEN NUMBER 

# a=list(range(0,100,2))
# print(a)

# a=[i for i in range(0,100,2)]
# # print(a)




# DIFFRENCE BETWEEN 2 LISTS 
# a=[1,2,3,4,5,9]
# b=[1,3,5,6,7,8]
# for i in (b)
#         if i not in  a:
#             print(i)


# ####NESTED LIST SOME 



# a=[[50,60,70],[20,10,40],[30,20,40]]
# c=[]
# total=0
# for i in (a): 
#     for j in (i) :
#         total+=j
#         c.append(j)
# print(total)
# print(c)          


# ###NASTED LIST AVG.....



# a=[[10,20,30,40],[39,20,49],[55,33,47]]
# b=len(a)
# total=0
# for i in (a):
#     for j in (i):
#         total+=j
#         c=total/b
#     print(c)
# # print(total)

# a=30
# b=[10,11,12,13,14,17,18,19]
# c=[[]]
# sum=0
# for i in (b):
#     for j in (i+1,len(b)):
#         d=i+j
#         if d==a:
#             c.append(b)
#             print(c)


# ##ODD EVEN NUM


# a=[23,14,56,12,19,9,15,25,31,42,43]
# b=0
# c=0
# for i in (a):
#     if i%2==0:
#         b+=1
#     else:
#         c+=1
# print(b)
# print(c)

# ###EVEN ODD SUM

# a=[23,14,56,12,19,9,15,25,31,42,43]
# even=0
# odd=0
# for i in a:
#     if i%2==0:
#         even+=i
#     if i%2!=0:
#         odd+=i
# print(even,"this is the sum of number")
# print(odd,"this is the sum of number")



# ###EVEN ODD AVG


    

# a=[23,14,56,12,19,9,15,25,31,42,43]
# even=0
# b=0
# odd=0
# c=0
# for i in (a):
#     if i%2==0:
#          even+=i
#          b+=1
#     else:
#         odd+=i
#         c+=1
# avg1=even/b
# avg2=odd/c
# print(avg1)
# print(avg2)







# a=[23,14,56,12,19,9,15,25,31,42,43]
# b=0
# evensum=0
# c=0
# oddsum=0
# for i in (a):
#     if i%2==0:
#         b+=1
#         evensum+=i
#     else:
#         c+=1
#         oddsum+=i
# avg1=evensum/b
# avg2=oddsum/c
# print(b)
# print(evensum)
# print(avg1)
# print(c)
# print(oddsum)
# print(avg2)





# ####CRORPSTI LSKHPATI




# a=[1,2,3,8,11,15,19,18,12,14,17,44,55,66,46,75,57]
# crorpati=0
# lakhpati=0
# dilwale=0
# for i in (a):
#     if i>10 and i<40:
#         lakhpati+=1
#     elif i<=10:
#         dilwale+=1
#     else :
#         crorpati+=1
# print(lakhpati)
# print(dilwale)
# print(crorpati)


# a=['a','n','t','a','a','t','n','n','a','x','u','g','a','x','a']
# c=[]
# for i in (a):
#     b=a.count(i)
#     if [i,b] not in c:
#         c.append([i,b])
#         # print(i,'=',b)
# print(c)
# for i in (a):
#     b=a.append(i)
#     print(i,'=',b)







# number = 30

# n = [10, 11, 12, 13, 14, 17, 18, 19]

# i=0

# l=[]

# while i < (len(n)-1):

#    l2=[]

#    j=i+1

#    while j<len(n):

#        if n[i] + n[j] == number:

#             l2.append(n[i])

#             l2.append(n[j])

#        j+=1

#    if l2:

#        l.append(l2)

#    i+=1

# print(l)



# table in list upto given range mentor sai kiran


# table between the range mentor

# a=int(input("enter"))

# l=[ ]

# c=1

# for i in range(1,a+1):

#     l.append(i)

#     empty=[]

#     for j in range(1,11):

#         v=i*j

#         empty.append(v)

#     l.append(empty)

# print(l)

# hidden number

# between two number hidden number print mentor

# a=[1,6,9,12,15]

# b=[]

# for i in range(len(a)-1):

#     c = []

#     b.append(a[i])

#     for j in range(a[i]+1, a[i+1]):

#         c.append(j)

#     b.append(c)

# print(b)



# odd even list mentor

# ####odd even list mentor

# size=int(input("enter the size"))

# l=[]

# for i in range(size):

#     if i%2==0:

#         l.append(i)

# for i in range(size):

#     if i %2!=0:

#         l.append(i)

# print(l)



# odd even ,single loop,list

# odd even list mentor

# print("odd")

# i=1

# l=[ ]

# while i<=100:

#    l.append(i)

#    # print(i)

#    if i==99:

#        print("even")

#        i=0

#        # print(i)

#        # l.append(i)

#    i=i+2

# print(l)



# empty list in output mentor sai

# a=[1,2,3,4,5,6]

# while True:

#     if not a:

#         break

#     a.pop()

# print(a)


# binary to decimal

# ##binary to decimal mentor

# a=1010

# b=len(str(a))

# sum=0

# p=0

# m=0

# while p<b:

#     rem=a%10

#     j=rem*(2**p)

#     m=j+m

#     p+=1

#     a=a//10

# print(m)



# pattern by use only integer

# pattern mahendra only integers

# a=int(input("enter"))

# m=0

# for i in range(1,(a+1)):

#     d=m*10+1

#     m=d

#     print(d)





# remove duplicates

#  meraki Duplicates submission_type: Duplicates

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]

# l=[ ]

# b=0

# while b<len(n):

#     if n[b] not in l:

#         l.append(n[b])

#     b+=1

# print("duplicates items:- ",l)





# remove duplicates in for loop

# a=[1,2,1,3,4,2,2,5,4,3]

# l=[ ]

# for i in a:

#     if i not in l:

#         l.append(i)

# print(l)




# meraki question 1


# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]

# l=[ ]

# for i in numbers:

#    if i>5 and i<40:

#        l.append(i)

# print(l)




# MERAKI QUESTION2 MAXIMUM NUMBER

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]

# maximun=numbers[0]

# for i in range(1,len(numbers)):

#    if maximun < numbers[i]:

#        maximun=numbers[i]

# print(maximun



# pallindrome meraki question 4

# palindome list meraki

# name=[ 'n', 'i', 't', 'i', 'n' ]

# b=len(name)-1

# c=[]

# while b>=-1:

#     c.append(name[b])

#     b+=-1

#     if c==name:

#         print('palindrome')

#     else:

#         print("not palindrome")
#     #u1+=1

###2universal table list


# a=int (input("num"))
# b=int (input("num2"))
# list=[]
# for i in range (a,b):
#     for j in range (i,i*11):
#         if j%i==0:
#              list.append(j)

# print(list)

####NESTED LIST HIGHEST SUM 

# a=[[2,4,6],[5,6,7],[6,5,33]]
# b=0
# c=[]
# for i in a :
#     for j in i :
#         b+=j
#     c.append(b)
#     b=0
# d=max(c)
# e=c.index(d)
# print(a[e])

# a={1,2,3,4,5}
# b={1,20,30,4}
# a.difference(b)
# print(a-b)
  

# a=[1,2,3,4,5]
# b=a[::]
# b.remove(2)
# print(a)
# print(b)


# ##########################################
# a=[5,1,4,2,8]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             b=a[j]
#             a[j]=a[j+1]
#             a[j+1]=b
# print(a)

#################################################

# a="suBHasH IS SImple BOy"
# count=0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if "S"in a[j]or "U"in a[j]or "B"in a[j]or "H"in a[j]or "A" in a[j]or "C"in a[j]or"D"in a[j]or"E"in a[j]or"F"in a[j]or"G"in a[j]or"H"in a[j]or"I"in a[j]or"J"in a[j]or"K"in a[j]or"L"in a[j]or"N"in a[j]or"O"in a[j]or"P"in a[j]or"Q"in a[j]or"R"in a[j]or"T"in a[j]or"V"in a[j]or"W"in a[j]or"X"in a[j]or"Y"in a[j]or"Z"in a[j]:
#             print(a[j],"capi")
#         else:
#             print(a[j])
    

    # print(b)

#############################################################


# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,289,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# a=1
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i==1:
#             continue
#         prime.append(i)          
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")
#####################################################################################################

# #############################################  second max  max minimum  ############3
# num=[200,10,80,90,105,10000,7,6,1000,1,500,54,100,2,3,4,5,95,6]
# total=num[2:]
# if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
# else:
#    s=num[1]
#    s1=num[0]
# for i in total:
#     if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#     mi=num[0]
#     for i in num:
#         if i<mi:
#             mi=i






#############################################  second max    ############3
# num=[1,200,10,80,90,105,10000,7,6,1000,500,54,100,3,4,5,95,6]
# total=num[2:]
# x=[]
# if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
# else:
#    s=num[1]
#    s1=num[0]
# for i in total:
#     if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#     if num[0]<num[1]:
#         men=num[0]
#         secm=num[1]
#     else:
#         men=num[1]
#         secm=num[0]
#     for i in total:
#         if i<secm:
#             if i<men:
#                 secm=men
#                 men=i
#             else:
#                 secm=i
# x.append(men)
# x.append(secm)
# x.append(s)
# x.append(s1)
# print(men,"minimum")
# print(secm,"sec minimum")
# print(x)
# #print(mi,"minimum")
# print(s,"maximum")
# print(s1,"second maximum")

########################################## magig squre nested  list 
# summ=0
# x=[]
# a=[
#     [56,8,5,],
#     [65,8,6,9],
#     [96,36,55,66,55],
# ]
# for i in a:
#     for j in range(len(a)):
#         ss=(i[j])
#         summ+=ss
#         x.append(ss)
# print(summ)        
# print(x)

# #####################################################  nested list sum 
# # numm=0
# kumm=0
# summ=0
# x=[]
# a=[
#     [4,8,3],
#     [74,65,63,5],
#     [12,55,88,5,3],
# ]
# for i in a:
#     for j in range (len(i)):
#         summ+=(i[j])
#         if j==(len(i)-1):
#             x.append(summ)
#             summ=0
# print(summ)
# print(x)
            
#######################################

# numm=0
# kumm=0
# summ=0
# aa=0
# x=[]
# y=[]
# z=[]
# humm=0
# tumm=0
# pumm=0
# g=[]
# a=[
#     [1,1,1],
#     [1,1,1],
#     [1,1,1],
# ]
# n=0
# u=2
# for i in a:
#     for ll in range(1):
#         numm+=i[aa]
#     for kk in range(1):
#         kumm+=i[1]
#     for hh in range(1):
#         humm+=i[2]
#     for dd in range(1):
#         tumm+=i[n]
#     n+=1
#     for oo in range(1):
#         pumm+=i[u]
#     u-=1
#     for j in range (len(i)):
#         summ+=(i[j])
#         if j==(len(i)-1):
#             x.append(summ)
#             summ=0
# if numm==pumm == kumm == tumm == humm:
#     print("magic square")
# else:
#     print("not magic square")
# print(x,numm,kumm,humm,tumm,pumm)
################################################ nested list to flat list and sum    
# summ=0
# x=[]
# y=[]
# a=[[4,5,6],[8,68,9],[555]]
# for i in a:
#     for j in range(len(i)):
#         ss=(i[j])
#         summ+=ss
#         y.append(ss)
#         if j ==(len(i)-1):
#             x.append(summ)
#             summ=0
# print(summ)        
# print(x)
# print(y)
##############################################3


# pumm,tumm,humm,aa,summ,kumm,numm=0,0,0,0,0,0,0
# x=[]
# a=[
#     [8,6,5],
#     [5,6,8],
#     [6,5,8],
# ]
# n=0
# u=2
# for i in a:
#     for l4l in range(1):
#         numm+=i[aa]
#     for kk in range(1):
#         kumm+=i[1]
#     for hh in range(1):
#         humm+=i[2]
#     for dd in range(1):
#         tumm+=i[n]
#     n+=1
#     for oo in range(1):
#         pumm+=i[u]
#     u-=1
#     for j in range (len(i)):
#         summ+=(i[j])
#         if j==(len(i)-1):
#             x.append(summ)
#             summ=0
# if numm==pumm == kumm == tumm == humm:
#     print("magic square")
# else:
#     print("not magic square")
# print(x,numm,kumm,humm,tumm,pumm)

#############################################################3


# i = 10
# a = []
# while i>0:
#   num = input()
#   a.append(num)
#   i = i-1
# # reverse elements of a
# a.reverse()
# #copied to new list
# b = a
# #again back to initial order
# a.reverse()
# print(a)


# count=1
# a=[0,1,1,0,0,0,1]
# for i in range(len(a)-1,0,-1):
#    for j in range(i):
#        if a[j]>a[j+1]:
#            b=a[j]
#            a[j]=a[j+1]
#            a[j+1]=b
#            count+=1
# print(a,count)


# s=["daadvaaa"]
# counter = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         temp = s[i:j]
#         if temp == temp[::-1]:
#             counter+=1
# print(temp)
# print(counter)

# def longestPalSubstr(string): 
# 	maxLength = 1

# 	start = 0
# 	length = len(string) 

# 	low = 0
# 	high = 0
# 	for i in range(1, length): 
# 		low = i - 1
# 		high = i 
# 		while low >= 0 and high < length and string[low] == string[high]: 
# 			if high - low + 1 > maxLength: 
# 				start = low 
# 				maxLength = high - low + 1
# 			low -= 1
# 			high += 1
# 		low = i - 1
# 		high = i + 1
# 		while low >= 0 and high < length and string[low] == string[high]: 
# 			if high - low + 1 > maxLength: 
# 				start = low 
# 				maxLength = high - low + 1
# 			low -= 1
# 			high += 1

# 	print ("Longest palindrome substring is:") 
# 	print (string[start:start + maxLength]) 

# 	return (maxLength) 
 
# string = ("forgeeksskeegfor")
# print ("Length is: " + str(longestPalSubstr(string)


# ########## This code is contributed by BHAVYA JAIN 


# a=[[1,2,3],[4,5,6]]
# i = 0
# while i<len(a):
#   j = 0
#   while j < len(a[i]):
#     print (a[i][j])
#     j = j+1
#   i = i+1



# a = [1,2,3,3,2,1,]
# i = 0
# mid = (len(a))/2
# same = True
# while i<mid:
#   if a[i] != a[len(a)-i-1]:
#     print ("No")
#     same = False
#     break
#   i = i+1
# if same == True:
#   print ("Yes")


# a = [1,2,3,2,1,3,12,12,32]
# i = 0
# while i < len(a):
#   j = i+1
#   while j < len(a):
#     if a[i] == a[j]:
#       del(a[j])
#     j=j+1
#   i = i+1
# print (a)

#python way
# a = [1,2,3,2,1,3,12,12,32]
# a = list(set(a))
# print (a)

# 
 
# maxLength = 1
# string = ("forgeeksskeegfor")
# start = 0
# length = len(string) 

# low = 0
# high = 0
# for i in range(1, length): 
# 	low = i - 1
# 	high = i 
# 	while low >= 0 and high < length and string[low] == string[high]: 
# 		if high - low + 1 > maxLength: 
# 			start = low 
# 			maxLength = high - low + 1
# 		low -= 1
# 		high += 1
# 	low = i - 1
# 	high = i + 1
# 	while low >= 0 and high < length and string[low] == string[high]: 
# 		if high - low + 1 > maxLength: 
# 			start = low 
# 			maxLength = high - low + 1
# 		low -= 1
# 		high += 1

# print ("Longest palindrome substring is:") 
# print (string[start:start + maxLength]) 


########################################


# a=int(input( ))
# if ((a%1000)//10)==47:
#     print("yes")
# else:
#     print("no")
# b=1
# a=int(input())
# while b<=a:
#     if b%3==0:
#         a+=1
#     print(b)
#     b+=1
# b=0
# a=[1,15,17,9,15,13]
# total=[]
# for i in a:
#     for j in range(len(a)-1):
#         if a[b]+a[j+1]==30:
#             print(a[b])
#             total.append(a[j+1])
        

#     b+=1
# print(total)

# a=[1,15,17,9,15,13]
# total=[]
# b=0
# for i in a:
#     for j in range(len(a)-1):
#         if i+a[j+1]==30:
#             print(i)
#             total.append(a[j+1])
#             a.pop(i)
#     b+=1
# print(total)
# b=0
# a=[1,15,17,9,15,13]
# total=[]

# for i in range(len(a)):
#     for j in range(len(a)-1):
#         print(j)
#         if a[i]+a[j+1]==30:
#             print(a[i])
#             total.append(a[j+1])

# print(total)

# nums = [1,15,17,9,15,13]
# target = 
# l = []
# x = 1
# length = len(nums) - 1
# for i in nums: 
#     l.append(nums.index(i))
#     if (target - i) in nums[x:]:
#        l.append(length - nums[::-1].index(target - i))
#        break
#     else:
#        l = []
#        x = x + 1
# print(l)


# nums = [1,15,17,9,15,13,26,4]
# target = 30
# l = []
# x = 1
# length = len(nums) - 1
# for i in nums: 
#     l.append(nums.index(i))
#     if (target - i) in nums[x:]:
#        l.append(length - nums[::-1].index(target - i))
#        break
#     else:
#        l = []
#        x = x + 1
# print(l)


# b=0
# a=[1,15,17,9,15,13]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]+a[j+1]==30:
#             print(a[i])
#             total.append(a[i])
# print(total)

# xx=[]
# n=int(input("enter number"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     xx.append(z)
#     x=y
#     y=z
#     z=x+y
# b=int(input())
# print(xx[b],"index")
# b=1
# a=int(input())
# while b<=a:
#     if b%3==0:
#         a+=1
#     print(b)
#     b+=1


##############################
# b=0
# a=[1,15,17,9,15,13]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]+a[j+1]==30:
#             print(a[i])
#             total.append(a[i])
# print(total)

# a="educatiohn"
# b="duecation"
# for i in a:
#     for j in range(len(a)-1):
#         if i in b:
#             print("yes")
#         else:
#             print("no")
#             break

############################################3

# a=input()
# b=input()
# c=list(a)
# d=list(b)
# d.sort()
# #print(d)
# c.sort()
# #print(c)
# if d==c and len(a)==len(b):
#     print("yes")
# else:
#     print("no")




# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
# if list1==list2:
#     print("enagram")
# else:
#     print("no enagram")
# print(list1,list2)
        

# for i in range(len(list1)-1):
#     for j in range(len(list1)-1):
#         if list1[j]>list1[j+1]:
#             n=list1[j]
#             list1[j]=list1[j+1]
#             list1[j+1]=n
# print(list1)

# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
# x=0
# count=0
# for n in list1:
#     for m in range(1):
#         if len(list1)==len(list2):
#             if list1[x] == list2[x]:
#                 continue
#             else:
#                 count+=1
#         else:
#             print("no length")
#             break
#     x+=1
# if count==0 and inp==inp2:
#     print("enagram")
# else:
#     print("no enagram")


# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
###########################################################################3
# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
# print(list1)
# print(list2)
# if list1 ==list2 and inp==inp2:
#     print("enagram")
# else:
#     print("no enagram")





##############################################3




# inp1=input()
# inp2=input()
# if len(inp1)<len(inp2):
#     for i in inp1:
#         if i in inp2:
#             print(i)
# elif len(inp1) == len(inp2):
#     for i in inp1:
#         if i in inp2:
#             print(i)
# else:
#     for i in inp2:
#         if i in inp1:
#             print(i)



# inp1=input()
# inp2=input()
# counter1=0
# for i in inp1:
#     if i in inp2:
#         counter1+=1
    
# if counter1 == len(inp2):
#     print("yes")
# else:
#     print('NO')

# b=0
# a=[1,15,17,9,15,13]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]+a[j+1]==30:
#             print(a[i],a[j+1])
#             # a.remove(a[i])
#             # a.remove(a[j+1])
#             total.append(a[i])
# #print(total)


# a="educatiohn"
# b="duecation"
# for i in a:
#     for j in range(len(a)-1):
#         if i in b:
#             print("yes")
#         else:
#             print("no")
#             break




# a=[1,15,17,9,15,13]
# for i in a:
#     for j in a:
#         if i+j==30:
#             print([i,j])
#             a.remove(i)
#             a.remove(j)


# a=[-1,0,1,2,-1,4]
# for i in a:
#     for j in a:
#         for k in a:
#             if i+j+k==0:
#                 print([i,j,k])
                
                
#                 a.remove(k)
#         a.remove(j)
#     a.remove(i)


# a=[-1,0,1,2,-1,4]
# for i in a:
#     for j in a:
#         for k in a:
#             print(i,j,k)
#             if i+j+k==0:
#                 #print([i,j,k])
                
                
#                 a.remove(k)
#         a.remove(j)
#     a.remove(i)

# quotint=0
# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
#     quotint+=1
# print(dividend)


# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
# print(dividend)



# count=0
# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
#     count+=1
# print(count)

    # summ=0
    # x=[]
    # count=0
    # a=[[4,5,6],[8,68,9],[555]]
    # for i in a:
    #    for j in range(len(i)):
    #        ss=(i[j])
    #        summ+=ss
    #        x.append(ss)
    #        count+=1
    # print(summ,"average",summ/count)
    # print(x)



# summ=0
# x=[]
# y=[]
# count=0
# a=[[4,5,6],[8,68,9],[555]]
# for i in a:
#    for j in range(len(i)):
#        ss=(i[j])
#        summ+=ss
#        y.append(ss)
#        count+=1
#        if j ==(len(i)-1):
#            x.append(summ)
#            print("average",summ/count)
#            count=0
#            summ=0
        
# print(summ)        
# print(x)
# print(y)


# pumm,tumm,humm,aa,summ,kumm,numm=0,0,0,0,0,0,0
# x=[]
# a=[
#    [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# n=0
# u=2
# for i in a:
#    for ll in range(1):
#        numm+=i[aa]
#    for kk in range(1):
#        kumm+=i[1]
#    for hh in range(1):
#        humm+=i[2]
#    for dd in range(1):
#        tumm+=i[n]
#    n+=1
#    for oo in range(1):
#        pumm+=i[u]
#    u-=1
#    for j in range (len(i)):
#        summ+=(i[j])
#        if j==(len(i)-1):
#            x.append(summ)
#            summ=0
# if numm==pumm == kumm == tumm == humm:
#    print("magic square")
# else:
#    print("not magic square")
# print(x,numm,kumm,humm,tumm,pumm)
###################################################3

# a=1
# total=int(input())
# b=1
# while a<total:
#     b=1
#     while b<=10:
#         if a%b==0:
#             if b==10:
#                 print(a,"devide h")
#                 break
#         else:
#             break
#         b+=1
#     a=a+1

# even=[]
# odd=[]
# counteven=0
# countodd=0
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# for i in elements:
#     if i%2==0:
#         even.append(i)
#         counteven+=1
#     else:
#         odd.append(i)
#         countodd+=1
# print(counteven,"even",even)
# print(countodd,"odd",odd)


# cc=0
# count=0
# count2=0
# even=[]
# odd=[]
# counteven=0
# totalsum=0
# countodd=0
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# for i in elements:
#     if i%2==0:
#         even.append(i)
#         counteven+=i
#         count+=1
#     else:
#         odd.append(i)
#         countodd+=i
#         count2+=1
#     totalsum+=i
#     cc+=1
# print(totalsum,"totalsum")
# print(totalsum/cc,"total average")
# print("average",counteven/count,"even",even)
# print(count,"count")
# print(counteven,"even sum")
# print("average",countodd/count2,"odd",odd)
# print(count2,"count2")
# print(countodd,"odd sum")




# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
# for i in kitna_paisa_hai:
#     if i>9999999 and i<999999999:
#         print(i,"coredpati")
#     elif i>99999 and i<9999999:
#         print(i,"lakhpati")
#     elif i>1 and i<99999:
#         print(i,"dilwale")




# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
# for i in kitna_paisa_hai:
#     if i>9999999 and i<999999999:
#         print(i,"coredpati")
#     elif i>99999 and i<9999999:
#         print(i,"lakhpati")
#     elif i>1 and i<99999:
#         print(i,"dilwale")
# x=[]
# y=[]
# time=0
# z=[]
# list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 

# for i in list1:
#     d=list1.index(i)
#     for j in list1:
#         if i==j:
#             x.append(j)
#             c=list1.index(j)
#             list1.pop(c)s
# print(x)
# a=1
# b=1
# for i in list1:
#     a=0
#     for j in list1:
#         if i==j and i not in z:
#             a+=1
#     if i not in z:  
#         z.append(i)
#         print(i,":",a)
        


 # print(j)


#    for j in a:
#        for k in a:
#            if i+j+k==0:
#                print([i,j,k])
               
               
#                a.remove(k)
# for i in a:
#     if i<=0:
#         print(i)
    #    a.remove(j)
#    a.remove(i)//
# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
#    for j in range(len(list1)-1):
#        for k in range(len(list1)-1):
#            if list1[k]>list1[k+1]:
#                n=list1[k]
#                list1[k]=list1[k+1]
#                list1[k+1]=n
#            if list2[k]>list2[k+1]:
#                n=list2[k]
#                list2[k]=list2[k+1]
#                list2[k+1]=n
# print(list1)
# print(list2)
# if list1 ==list2 and len(inp)==len(inp2):
#    print("enagram")
# else:
#    print("no enagram")





# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
#    for j in range(len(list1)-1):
#        for k in range(len(list1)-1):
#            if list1[k]>list1[k+1]:
#                n=list1[k]
#                list1[k]=list1[k+1]
#                list1[k+1]=n
#            if list2[k]>list2[k+1]:
#                n=list2[k]
#                list2[k]=list2[k+1]
#                list2[k+1]=n
# x=0
# count=0
# for n in list1:
#    for m in range(1):
#        if len(list1)==len(list2):
#            if list1[x] == list2[x]:
#                continue
#            else:
#                count+=1
#        else:
#            print("no length")
#            break
#    x+=1
# if count==0 and len(inp)==len(inp2):
#    print("enagram")
# else:
#    print("no enagram")



# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
# list1.sort()
# list2.sort()
# print(list1)
# print(list2)
# if list1 ==list2 and len(inp)==len(inp2):
#    print("enagram")
# else:
#    print("no enagram")





# time=0
# z=[]
# list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
# a=1
# b=1
# for i in list1:
#     a=0
#     for j in list1:
#         if i==j and i not in z:
#             a+=1
#     if i not in z:  
#         z.append(i)
#         print(i,":",a)
#######################################################3



# b=0
# a=[1,15,17,12,13,15]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in a:
#    for j in         if i+j ==30 and i not in list1:
#            print(i,j)
#            total.append(i)
#     # if i not in list1:
#     #     list1.append(i)
# print(total)

# x=[]
# a=["hello","guys"]
# for i in a:
#     for j in range(1,len(i)+1):
#         x.append(i[-j])
# print(x)


# aa=int(input())
# i=0
# a=1
# n=0
# b=0
# while n<=aa:
#     n+=1
#     print(b)
#     i=a
#     a=b
#     b=i+a
# for i in range(1,26,):
#     if i%5==0:
#         print(i)

# counter=520
# a=1
# while a<=counter:
#     counter=520-500
#     print(a)
#     a+=1

# a=1
# sum=0
# count=0

# while a<=100:
#     if a%2==0:
#         print(sum,"even")
#         sum=sum+a
#     else:
#         count+=a
#     a+=1
    
# print(count,"odd")
  
# print("suraj"*100,end=" ")




######KONE BANEGA CAROPATI 


# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]

# options_list = [
#     #pehle question ke liye options
#     ["four", "nine", "seven", "eight"],
#     #second question ke liye options
#     ["chandigarh", "bhopal", "chennai", "delhi"],
#     #third question ke liye options
#     ["software engineering", "counseling", 
#     "tourism", "agriculture"]]
# s1=[3,4,1]
# c1=1
# n,u,tr=0,0,0
# u1=0
# for i in question_list:
#     print(i)
#     c2=1
#     s2=s1[u1]
#     for j in options_list:
#         if c1==c2:
#             g=1
#             for k in j:
#                 print(g,k)
#                 g+=1
#             a=input("do you want 50/50 life line YES or NO \n enter your answer  ")
#             if a=="yes" and u==0:
#                 b=int(input("select one of them ["+str(s2)+"  "+str(c1)+"] enter number  "))
#                 u=1
#                 if s1[u1]==b:
#                     print("you win")
#                 else:
#                     print("you lost")
#                     n=1 
#             elif a=="no":
#                 b=int(input("enter number  "))
#                 if b==s1[u1]:
#                     print("you win")
#                 else:
#                     print("you lost")
#                     n=1
#             else:
#                 print("you already used this lifeline")
#                 b=int(input("enter number  "))
#                 if s1[u1]==b:
#                     print("you win")
#                 else:
#                     print("you lost")
#                     n=1 
#         c2+=1
#     if n==1 :
#         break
#     c1+=1
#     u1+=1

     
 
 ###########PROGRESS TRACKING ########



# # n = int(input("enter the number"))
# # a =1
# # while a <=n:
# #     b = 1
# #     while b <=a:
# #         print(b, end="")
# #         b = b+1
# #     print()
# #     a = a+1


# # n = int(input("enter the number"))
# # a = 1
# # while a<=n:
# #     b = 1
# #     while b <= a:
# #         print((((10**a)-1)//9)**2,end=" ")
# #         b = b+9
# #     print()
# #     a = a+1





# str = input("ente the string ")
# upper = 0
# lower = 0
# alpha = "abcdefghijklmnopqrstuvwxyz"
# while len(str)>0:
#     if alpha in str  :
#         lower = lower +1
