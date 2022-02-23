
# str = input("enter your string")
# length = len(str)//2
# print(str[0] + str[length] + str[len(str)-1])
# print(str[0] + str[length] + str[-1])


 #the first way
# str = input("enter the string")
# str1 = int(len(str)/2)-1
# str2 = int(len(str)/2)
# str3 = int(len(str)/2)+1
# print(str[str1] + str[str2] + str[str3] )

#using the slicing
#the second way
# str = input("enter the string")
# mc = int(len(str)/2)
# print(str[mc - 1:mc +2])


# s1 = "navgurukul"
# s2 = "kelly"
# str = len(s1)//2
# print(s1[:str] + s2[:] + s1[str:])

 #another way to the concatenation of the s2 string 

# s1 = input("enter first string")
# s2 = input("enter second string")
# mc = len(s1)//2
# sli = s1[:mc]
# sli = sli + s2
# sli = sli + s1[mc:]
# print("after appening the new string", sli)

#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# s1 = "bharat" #input("enter the string")
# s2 = "india" #input("enter the second string")
# str = s1[0] + s1[len(s1)//2] + s1[-1]

# str1 = s2[0] + s2[len(s2)//2] + s2[-1]
# print(str +str1)

# s1 = "america" #input("enter the string")
# s2 = "japan" #input("enter the second string")
# str = s1[0] + s2[0] +  s1[len(s1)//2]  + s2[len(s2)//2] + s1[-1] + s2[-1]
# print(str)

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

# s1 = "abc"
# s2 = "xyz"
# str = s1[0] + s2[-1] + s1[1:2] +s2[1:2]
# print(str)


#Write a program to find all occurrences of “USA” in a given string ignoring the case.

# s1 = "welcome to the USA. usa is awesome, isn't it?"
# ss = "USA"
# s2 = s1
# print(s2.count(ss))

# s1 = "welcome to the USA. usa is awesome, isn't it?"
# s2 = s1.lower() 
# print(s2.count("usa"))


#reverce the string 
# first way
# str = "dharamshal"
# s2 = len(str)
# print(str[::-1])
# print(str[0 + s2 :: -1])

# #the second way
# str1 = "dharamshal"
# print("".join(reversed(str1)))



# Exercise 12: Find the last position of a given substring
# str = "Emma is a data scientist who knows python. Emma works at the google"
# print(str)
# print(str.rfind("Emma"))


# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# str = "Emma-is-a-data-scientist"
# str1 = str.split("-")
# for sub in str1:
#     print(sub)

# str = "      ahbvihttttttttttttttttttt       "
# print(str)
# # print(str.lstrip())
# # print(str.rstrip())
# print(str.strip())


#use the filter method in the list 
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# new_str_list = list(filter(None,str_list))
# print(new_str_list)


# str = "this is the string"
# str2 = str.title()
# print(str2.istitle())
# print(str)
# print(str2)


# str = "this is the string"
# print( "thee"  not in str)

# str = "navgurukul dharamshala campus"
# print(len(str))
# print(str[28])
# print(str.capitalize())
# print(str[-1].capitalize())
# print(str[0].capitalize() + str[1:len(str)-1] + str[len(str)-1].capitalize() + str[-1].capitalize())
# print(str[len(str)//2].capitalize())
# print(str[0:len(str)//2] + str[len(str)//2].capitalize() + str[len(str)//2 +1 : ])


# string interpolation 
# str1 = "navgurukul"
# str2 = "dharamshala"
# str3 = "campus"
# print(f"my campus name is {str1} {str3} and it is placed at {str2} ")

#interpolate a variables into a string using format() method
# str1 = "navgurukul"
# str2 = "dharamshala"
# str3 = "campus"
# print("my campus name is {2} {0} and it is placed at the {1} ".format(str1,str2,str3))

# str = "hbjhfjhfj"
# str2 = "467384912399"
# print(str2.isnumeric())
# print(str.isalpha())
# # print(str2.islower())
# # print(str2.isupper())
# print(str[0].islower())

# str = input("enter string")
# if not(str.isnumeric() and str.isalpha()):
#     print("hello")
#     # if not(str.isalpha):
#     #     print("not entered alpha")
        
# else:
#     print("bye")

# a=0
# while a>=150:
#     print(a,chr(a))
#     a+=1
    
    

# a = int(input("enter the number"))
# print(type(a))

# print('my','name','is','james', sep='%%')

# num = 458.541315

# print('%.2f' % num)

# name,name2,name3 = input({},{},{})

#the largest number of three number 
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# num3 = int(input("enter the third number"))
# if num1>num2 and num1> num3:
#     print("the larest number is",num1)
# elif num2 > num1 and num2>num3:
#     print("the larest number is",num2)
# elif num3>num1 and num3>num2:
#     print("the larest number is",num3)
# else:
#     print("the number are equal so enter the different number for find the largest number in three numbers")
    
    
# the second larest number in the same two number

# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# num3 = int(input("enter the third number"))
# if num1<num2 and num1>num3 or num1< num3 and num1>num2:
#     print("the second largest number is",num1)
# elif num2<num3 and num2>num1 or num1< num2 and num2 > num3:
#     print("the second largest number is",num2)
# elif num3<num2 and num3>num1 or num3<num1 and num3>num2:
#     print("the second largest number is",num3)
# elif num1==num2 or num2==num3 or num3== num1:
#     if num1 == num2:
#         print("the second largest number is",num2)
#     elif num2 == num3:
#         print("the second largest number is",num2)
#     elif num3 == num1:
#         print("the second largest number is",num3)



#there are the two ways to reverse the given string 
# #the 1st way
# str = "navgurukul"
# print("".join(reversed(str)))

# #the 2nd way 
# print(str[::-1])


# print(str )
# print(str.upper())
# print(str[0].capitalize() + str[1:len(str)-1] + str[-1].capitalize())
# print(str[0].capitalize() + str[1:-1] + str[-1].capitalize())



# Python program to demonstrate
# type Casting
 
# # int variable
# a = "5"
 
# # typecast to str
# n = int(a)
 
# print(n)
# print(type(n)
# 
# 
# 
# )




# str = "dharamshala navgurukul campus"
# print(min("dharamshala"))

# str = "this is ""the"" string"
# str = "\tthis is the \nstring"
# print(str)

# a=5
# if a==5:
#     print("hello")
# elif a==0:
#     print("bye")
# elif a==5:
#     print("hello")

# str = input("please! enter the day")
# if str=="monday":
#     print("rajma chawal")
# elif str=="tuesday":    
#     print("motan kosha")
# elif str=="wednesday":
#     print("pizza")    
# elif str == "thursday":
#     print("dal roti")    
# else:
#     print("please! choose day between monday to thursday ")    





# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# num3 = input("please! enter the condition")
# if num3=="+":
#     print(num1+num2) 
# elif num3=="-":
#     print(num1 - num2 )
# elif num3 == "*":
#     print(num1*num2)
# elif num3 =="/":
#     print(num1/num2)


# print("Please! enter your name")

# a = input("enter your input")
# # print("please! enter your name")
# b= input("enter your input")


# if a == "stone" and b=="paper":
#     print("win", b)
# elif a=="stone" and b == "scissor":
#     print("win",a)
# elif a=="stone" and b == "stone":
#     print("the game is tie")
# elif a == "paper" and b=="paper":
#     print("the match is tie")
# elif a=="paper" and b == "scissor":
#     print("win",b)
# elif a=="paper" and b == "stone":
#     print("win",a)
# elif a == "scissor" and b=="paper":
#     print("win" ,a )
# elif a=="scissor" and b == "scissor":
#     print("the game is tie")
# elif a=="scissor" and b == "stone":
# #     print("win",b)


# a = input("please! choose the stone, paper and scissor")

# # b= input("please! choose the stone, paper and scissor")
# num = int(input("enter number"))
# if num%10 and num//10:
#     print()

           
    
#     if a=="stone" and b == "scissor":
        
#         if a=="stone" and b == "stone":
         
#             if a == "paper" and b=="paper":
             
#                 if a=="paper" and b == "scissor":
                   
#                     if a=="paper" and b == "stone":
                     
#                         if a == "scissor" and b=="paper":
                          
#                             if a=="scissor" and b == "scissor":
                              
#                                 if a=="scissor" and b == "stone":
                                  
# else:
#     print("please choose the stone and paper")
    















# user1=input("Please Enter User1 Name:- ")
# user2=input("Please Enter User2 Name:- ")
# a=0
# for a in range(0,len(user1 + user2)):
#     c1=input(user1 +" Please choose (stone/paper/scissor):- ")
#     c2=input(user2 +" Please choose (stone/paper/scissor):- ")
#     if c1=="stone" and c2=="stone":
#         print("Game Tie")
#     elif c1=="stone" and c2=="paper":
#         print(user2,"Won")
#     elif c1=="stone" and c2=="scissor":
#         print(user1,"Won")
#     elif c1=="paper" and c2=="paper":
#         print("Game Tie")
#     elif c1=="paper" and c2=="scissor":
#         print(user2,"Won")
#     elif c1=="paper" and c2=="stone":
#         print(user1,"Won")
#     elif c1=="scissor" and c2=="scissor":
#         print("Game Tie")
#     elif c1=="scissor" and c2=="stone":
#         print(user2,"Won")
#     elif c1=="scissor" and c2=="paper":

#         print(user1,"Won")




# print("amit" >"amitabh")
# b = 34
# a = 4
# print(b and a )






# age = int(input("enter your age"))
# if age>=18 and age>90:
#     print("you are  able to voting")
# else:
#     print("you are  not able to voting")




# num1 = int(input("enter your number"))
# if num1%2==0:
#     print("your number is even number")
# else:
#     print("your number is odd")
    


# num1 = int(input("enter the number"))
# if num1%7==0 and num1 != 0:
#     print("the number is divide of 7")
# else:
#     print("the number is not devide of 7")
    

# num1 = int(input("enter the number"))
# if num1%5==0 and num1 != 0:
#     print("hello")
# else:
#     print("bye")
    
    

# unit = int(input("enter the unit"))
# if unit >=100:
#     print("no charge")
# elif unit >100 and unit>=200:
#     print("the amount is", (unit-100)*5)
# elif unit >200:
#     print("the total bill amount is",500+(unit-200)*10 )
    

# num1 = int(input("enter the number"))
# print("the last disit of the number", num1%10)
    

# num1 = int(input("enter the number"))
# num2 = num1%10
# if num2%3==0 and num2 !=0 :
#     print("the number is divisable by 3")
# else:
#     print("this number is not divisible by 3 ")
    


# marks = int(input("enter your marks"))
# if marks>90:
#     print("grade A")
# elif marks>80 and marks>=90:
#     print("grade B")
# elif marks>=60 and marks >=80:
#     print("grade C")
# elif marks>60:
#     print("grade D")


# cp = int(input("enter the bike prize"))
# if cp>100000:
#     print("your road tax", 15/100*cp)
# elif cp >50000 and cp >=100000:
#     print("the road tax" , 10/100*cp)
# elif cp >=50000:
#     print("the roa tax", 5/100*cp)
    


# day = int(input("enter the number of 1 to 7"))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     print("please! enter the number of 1 to 7")    


    
# city = input("enter the city in delhi, agra and jaipur")
# if city  == "delhi":
#     print("red fort".title())
# elif city  == "agra":
#     print("taj mahal".title())
# elif city  == "jaipur":
#     print("jal mahal".title())
# else:
#     print("please! enter the current city in delhi jaipur and agra".title())




# age  = int(input("enter the number"))
# if age>60 and age >=80:
#     print("you are the senior citizen")
# else:
#     print("you are  no senior citizen")
    

# if num>0:
#     print("the number is negative")
# else:
#     print("the number is positive0")
    
    
# if num%2==0 and num%3==0:
#     print("the number is divide by two and three")
# else:
#     print("the number is not devide by 2and 3")
    

# num = int(input("enter the number"))
# num1 = int(input("enter the number"))
# num2 = int(input("enter the number"))
# if num>num1 and num>num2:
#     print("the lardest number is the ",num)
# elif num1>num and num1>num2:
#     print("the largest number is ",num1)
# elif num2>num and num2>num1:
#     print("the largest number is", num2)
    

# a = int(input("enter the age"))
# b = int(input("enter the age"))
# c = int(input("enter the age"))
# d = int(input("enter the age"))
# if a>b and a>c and a>d:
#     print("a is the oldest")
# elif b>a and b>c and b>d :
#     print("b is the oldest")
# elif c>a and c>b and c>d:
#     print("c is the oldest")
# elif d>a and d>b and d>c:
#     print("d is the oldest")

# #prime number program
# n= int(input("enter the number"))
# a = n%2==1 and n%3==1
# b = n%3==1 and n%5==1
# c = n%5==1 and n%7==1
# d = n%7==1 and n%9==1
# if a or b or c or d:
#     print("the number is the prime")
# else:
#     print("the number is not prime ")


# n= int(input("enter the number"))
# if n/2==:


# ch = input("enter the character")
# # if len(ch)==1:
# if ch  == "a" or ch =="e" or ch  == "i" or ch  =="o" or ch =="u":
#         print("this character is vowal")
# else:
#         print("this character is not vowel")
# # else:
    # print("please! enter the 1 character")
    

# ch = input("enter the character")
# vov = "aeiou"
# if len(ch)==1:   
#     if ch  in vov:
#         print("this character is vowel")
#     else:
#         print("this character is not vowel")
# else:
#     print("please! Enter the 1 character")    


# td = int(input("enter thetotal number of working days"))
# ad = int(input("enter the total number of days for absent"))
# pop = (td-ad)*100/td
# print("the total percent of present days",pop)
# if pop<75:
#     print("you are not able to sit in exam")
# else:
#     print("you are able to sit in exam")
    

# employee = int(input("please! enter your experience in year"))
# salary = int(input("enter your salary"))
# if employee > 10 :
#     print("your net bonus amount is",10*salary/100)
# elif employee >=6 and employee <=10:
#     print("your net bonus amount is", 8*salary/100) 
# elif employee <6:
#     print("your net bonus amount is",5*salary/100)   


    
# marked_prize = int(input("enter your marked prize"))
# if marked_prize > 10000:
#     print("the total amount is", marked_prize-20/100*marked_prize)
# elif marked_prize > 7000 and marked_prize <=10000:
#     print("the total amount is",marked_prize-15/100*marked_prize)
# elif marked_prize <=7000:
#     print("the total amount is",marked_prize-10/100*marked_prize) 


# marked_prize = int(input("enter your marked prize"))

# if marked_prize >10000:
#     d = 20/100*marked_prize
# elif marked_prize > 7000 and marked_prize<=10000:
#      d =15/100*marked_prize
# elif marked_prize<7000:
#     d = 10//100*marked_prize
# na = marked_prize-d
# print("the net prize is",na)
    
    
# num1 = int(input("enter first number"))
# num2 = int(input("enter first number"))
# operator = input("enter the operator")
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2 )
# elif operator == "//":
#     print(num1 // num2 )
# elif operator == "**":
#     print(num1 ** num2 )
# elif operator == "%":
#     print(num1 % num2 )

    
# a = int(input("enter first number"))
# b = int(input("enter second number"))
# c = int(input("enter third number"))
# if a>b  and b>c or a<b and b<c:
#     print("the second largest number of",b)
# elif b>a and a >c  or c>a and a > b:
#     print("the second largest number of",a)
# elif a>c and c> b or a<c and b>c:
#     print("the second largest number of",c)



# side1 = int(input("enter the first side of tringle"))
# side2 = int(input("enter the second side of tringle"))
# side3 = int(input("enter the third side of tringle"))
# if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
#     print("this is the tringle")
# else:
#     print("this is not tringle")
    

# unit = int(input("enter the electric units"))
# if unit <= 100:
#     print("your electric bill amount is per day 0.0 rupees")
# elif unit > 100 and unit <=300:
#     print("your electric bill amount is per day", (unit-100)*2)
# elif unit > 300:
#     print("your electric bill amount is per day", 400+(unit-300)*5)
    
#library charge program
# days = int(input("enter the number of days"))
# if days <= 5:
#     charge= days*2
# elif days  >= 6 and days <= 10:
#     charge = days*3
# elif days >= 11 and days <= 15:
#     charge = days*4
# else:
#     charge = days*5
# print("the library charge is",charge ,"rupees")


# km = int(input("enter the kilometer"))
# if km <= 10:
#     pay = 11*km
# elif km >10 and km <= 100:
#     pay = 110 + (km-10)*10
# else:
#     pay = 900 + 100+ (km-100)*9
# print("The kilometer bill is", pay)
    

# eng = int(input("enter the english subject marks"))
# math = int(input("enter the math subject marks"))
# sci = int(input("enter the science subject marks"))
# ss = int(input("enter the social studies subject marks"))
# if eng > 80 and math >80 and sci>80 and ss >80:
#     print("you select science stream")
# elif eng >80 and  math >80 and sci > 50 and ss <80:
#     print("you select the commerce stream")
# elif (eng >80 and ss > 80) and math <80 :
#     print("you select the humanities")
# else:
#     print("you are not select for any stream")   

# eng = int(input("enter the english subject marks"))
# math = int(input("enter the math subject marks"))
# sci = int(input("enter the science subject marks"))
# ss = int(input("enter the social studies subject marks"))
# if eng >80 and math >80 and sci>80 and ss > 80:
#     print("you select science stream")
# elif (eng  and math > 80) and sci > 50:
#     print("you select the commerce stream")
# elif eng and ss > 80 and math and sci <80:
#     print("yuo select the humanities")

    
##################this question from codedopes##############
# emp = int(input("enter the number of year of service"))
# sal = int(input("enter the salary"))
# if emp > 5:
#     print("the net bonus is", 5/100*sal)
# else:
#     print("your number of year service of less than 5")
    


# L = int(input("enter the length of rectangle"))
# b = int(input("enter the breadth of rectangle"))
# if L==b :
#     print("it is square")
# else:
#     print("it is rectangle / it is not square")    


# n1 = int(input("enter the first number"))
# n2 = int(input("enter the second number"))
# if n1>n2:
#     print("first number is greatest")
# elif n2>n1:
#     print("second number is greatest")
# else:
#     print("both number are equal")


# quantity = int(input("enter the quantity which you purchased on shop"))
# coq = 100*quantity
# if coq > 1000:
#     print("the cost is",coq-10/100*coq)
# else:
#     print("the total cost is",coq)
    

        
    






# meraki question###############################
# day = input("enter the days")
# if day == "monday":
#     print("rajama chawal")
# elif day == "tuesday":
#     print("pao bhaji")
# elif day == "wednesday":
#     print("chole bhature")
# elif day == "thursday":
#     print("dosa")
# elif day == "friday":
#     print("litti chokha")
# elif day == "saturday":
#     print("thupka")
# else:
#     print("poha")


# value = "  "
# guess = input("sheher ka naam guess karo")
# if value == guess:
#     print("hello")
# else:
#     print("bye")

# value = "rajsthan"
# guess = input("sheher ka naam guess karo")
# if guess == value:
#     print("aapka guess right hai")
# else:
#     print("aapka guess galat hai")

# value = "rajsthan"
# guess = input("sheher ka naam guess karo")
# if  guess != value:
#     print("aapka guess galat hai")
# else:
#     print("aapka guess right hai")


# speeds = int(input("enter the vehicle speed"))
# if speeds <= 60:
#     print("it will not be considered as overspeeding")
# else:
#     print("it will be considered as overspeeding")
    
# day = input("enter the day name")
# if day  == "monday":
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("poha")
#     elif time == "lunch":
#         print("rajma chawal")    
#     elif time == "dinner":
#         print("roti sabzi")
# elif day  == "tuesday":
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("meggi")
#     elif time == "lunch":
#         print("chaal-dal")    
#     elif time == "dinner":
#         print("paneer")
    
# elif day  == "wednesday":
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("kheer")
#     elif time == "lunch":
#         print("choole-bhatoore")    
#     elif time == "dinner":
#         print("dal-roti")
    
# elif day  == "thursday":
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("channa")
#     elif time == "lunch":
#         print("aalu ki sabzi and roti")    
#     elif time == "dinner":
#         print("bengan")
    
# elif day  == "friday":
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("sandwich")
#     elif time == "lunch":
#         print("hari mirch and roti")    
#     elif time == "dinner":
#         print("bhindi")
    
# elif day  == "saturday":
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("milk and paneer")
#     elif time == "lunch":
#         print("thukpa")    
#     elif time == "dinner":
#         print("soyabeen")

# else :
#     time = input("enter the time for example breckfast, lunch and dinner")
#     if time == "breckfast":
#         print("pasta")
#     elif time == "lunch":
#         print("noodles")    
#     elif time == "dinner":
#         print("gajer ka halwa")

    

# number = int(input("enter the number"))
# if number % 2 == 0:
#     print("entered numberi s completely divisible by 2")
# else:
#     print("entered number is not completely divisible by 2")


# var1 = int(input("enter the first number"))
# var2 = int(input("enter the second number"))
# if var1 % var2 ==0 :
#     print("divisible")
# else:
#     print("not divisible")
    
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second  number"))
# if num1 > num2:
#     print("the gretest number is",num1)
# else:
#     print("the gretest number is",num2)
    
    
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second  number"))
# if num1 < num2:
#     print("the gretest number is",num2)
# else:
#     print("the gretest number is",num1)
    



# num1 = int(input("enter the first number"))
# if num1 % 5 == 0 and num1 %15 == 0:
#     print("the entered number is divisible by 5 and 15")
# else:
#     print("the entered number is not  divisible by 5 and 15")
    
# usin the nested if else 

# num1 = int(input("enter the first number"))
# if num1 % 5 ==0:
#     if num1 % 15 ==0:
#         print("the entered number is divisible by 5 and 15")
#     else:
#         print("the entered number is not divisible bt 5 and 15")   
# else:
#     print("the entered number is not divisible bt 5 and 15")   
       

# age = int(input("enter the age of people"))
# if age >= 5 and age <= 100:
    
#     if age >= 5:
#         print("you can go to school")
#         if age >= 18:
#             print("you can vote in elections")
#             if age >= 21:
#                 print("you can drive a car")
#                 if age >= 24:
#                     print("you can merry")
#                     if age >= 25:
#                         print("you can legally drink")
# else:
#     print("please! Enter the right age")



####################to reverse the number for 4 digits ##########################3
# number = int(input("enter the number"))
# if number%2==1 and (number%3 ==1 or number %3 == 2) :
#     if (number % 5==1 or number%5 == 4) or (number%5==2 or number%5==3):
#         print("prime number")
#     else:
#         print("not prime number")
# else:
#     print("Not prime number")   

# print(type(number))

    
# A = (number[::-1])
# B = int(A)
# print(B)






#strong password
# import random
# a1 = input("enter the password") 
# password   = ("a" or "b" or  "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t"or "u" or "v" or "w" or "x" or "y" or "z") and ("A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T"or "U" or "V" or "W" or "X" or "Y" or"Z") and ("1" or "2" or "3" or "4" or "5" or  "6" or "7" or "8" or "9" or "0") and ("~" or "!" or "@" or "#" or "$" or "%" or  "^" or "&" or  "*" or  "(" or ")" or "o_" or "-" or "=" or "+" or "`" or "," or "." or"/" or"?" or "|" or  "\"" or ":" or ";" or "'")
# if a1 in password :
#     print("strong password")
# else:
#     print("weak password")


# password = input("enter your password")
# pas = "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" 
# pas1 = "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z"
# pas2 = "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"
# pas3 = "~" or "`" or "!" or "@" or"#" or "$" or"%" or"^" or"&" or"*" or "(" or ")" or "_" or "-" or "+" or "=" or ":" or ";" or "<" or "'" or ">" or "/" or "?" or "." or "," or " "
# if password ==  pas :
#     print()



# strong password ?
