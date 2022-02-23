############1

# def ask_que():
#     for i in range(0,100):
#         print('who is the founder of fb')
#         print('1.mark zakerberg')
#         print('2.bill gates')
#         print('3.steve jobs')
#         print('4.abhimanyu singh')
# ask_que()


################2


# num=[3,5,7,34,2,89,2,5]
# b=max(num)
# print(b)


# numbers = [1, 2, 3, 4, 5]
# b=sum(numbers)
# print(b)


# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# unorder_list.sort()
# print(unorder_list)



# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list.reverse()
# print(reverse_list)


# list = [8, 6, 4, 8, 4, 50, 2, 7]
# b=min(list)
# print(b)




################3

# def sum():
#     print(12+13)
# sum()



# def welcome():
#     print("Welcome to function")
# welcome()




# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()




##########4

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))


# a=[1,2,3,4,5,6]
# print(len(a))



# def say_hello(name):
#     print("Hello ", name)
#     print("Aap kaise ho?")
# say_hello("Aatif")



# def add_numbers(number1, number2):
#     print("Main do numbers ko add karunga.")
#     print(number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)




# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")



# def say_hello_people(name_x, name_y, name_z, name_a):
#     print("Namaste ", name_x) # hindi mein
#     print("Alah hafiz ", name_y) # urdu mein
#     print("Bonjour ", name_z) # french mein
#     print("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")



# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")



# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")


# def greet(*names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")



# def info(name,age = ""):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")


# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","abhi")



###################2.1


# def a(name,placement):
#     print("mera naam",name,"hai")
#     print("main navgurukul ka",placement,"hai")
# a("rishab","co-founder")

 

 #################3




# def student(nameofstudent):
#     for name in nameofstudent:
#      print(name)
# student('abhi','arun','dilip')






##################4



# def sum(num1,num2):
#     print(num1+num2)
# sum(56,12)


####********que 
# def sum(num1,num2):
#     for i in range(len(num1)):
#         c=num1[i]+num2[i]
#         print(c)
# sum([10,20], [23,45])


##############5

# def check_num(*num):
#     c=0
#     for i in num:
#         # print(i)
#         if i%2==0:
#             c+=1
#             if c==2:
#                 print('dono even hai')
#         else:
#             print('dono even nhi hai') 
# check_num(2,6)   


# def check_num(num1,num2):
#     c=0
#     for i in range(len(num1)):
#         if num1[i]%2==0 and num2[i]%2==0:
#             print('dono even hai')
#         else:
#             print('dono even nhi hai')
# check_num([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])            

##########RETURN KO DHYAN ME RAKHE######

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum
# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)

# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum
# sum4 = add_numbers_print(4, 5)
# print(sum4)
# print(type(sum4))
# number_b = add_numbers_print(5, 4) / add_numbers_print(2, 1)
# print(number_b)


#######RETURN KE NECHE KA KOI BHI CODE RUN NHI HOGA KYUKI EK BAAR AGAR RETURN USE HO GYA FIR AAGE KA CODE READ NHI HOTA ###########
# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print("Kya main yahan tak pahunchunga?")
#     return number_sum
# sum6 = add_numbers_more(100, 20)


# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#             return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
# print("Kya main print ho payungi? :-(")
# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# print(fri_menu)


# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#         print("Kya main print ho payungi? :-(")
#         return food
#         print("Lekin main toh pakka nahi print hounga :'(")
#         print(menu("monday"))


###############6

# def calculater(num1,num2,opration):
#     if opration=="+":
#         c=num1+num2
#         print(c)
#     elif opration=="-":
#         c=num1-num2
#         print(c) 
#     elif opration=="*":
#         c=num1*num2
#         print(c)
#     elif opration=="/":
#         c=num1/num2
#         print(c)
#     else:
#         print('invalid operation')
# calculater(int(input("num1: ")),int(input('num2: ')),(input('opration: ')))




# def multipal_list(num1,num2):
#     a=[]
#     for i in range(len(num2)):
#         c=num2[i]*num1[i]
#         a.append(c)
#     print(a)
# multipal_list([5, 10, 50, 20], [2, 20, 3, 5])       


# def f1():
#     s="I love navgurukul"
#     def f2():
#         print(s)
#     f2()
# f1()





# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s) 
#     print(s)
#     second_function()
 
# first_function()


######## AGAR AAP EK * KA USE KAROGE TOO VO TUPLE LETA HAI OR AGAR AAP ** KA USE KARTE HO TOO VO DICTIONARY LETA HAI #########


# def greet(*names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")


# def a(**abhi):
#     print("my name is",abhi)
# a(abhi='arun',dilip='kabaddi')


########### If we call the function without argument, it uses the default value


# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(food)
#     print(food[x])#####food[x] yha value ko print karega

# fruits = {"A":"apple","B": "banana","C" :"cherry"}
# ####### YHA HUM FRUITS NAAM KE VARIABLE ME LIST,DIC,SET,TUPLE KUCH BHI PAAS KAR SACTE HAI 
# my_function(fruits)



##############2.1

# def vote(age):
#     if age>=18:
#         print('eligible for vote')
#     else:
#         print('not eligible for vote')
# vote(int(input('age')))
    

##############2


# def perfect(b):
#     c=1
#     for i in range(2,b):
#         if b%i==0:
#             c+=i
#     if b==c:
#         print('yes perfect')
#     else:
#         print('not perfect')
        
# perfect( b=int(input('upper ')))


#######RANGE

# def perfect(b):
#     c=1
#     for num in range(2,b):
#         for i in range(2,num):
#             if num%i:
#                 c+=i
#         if c==num:
#             print(num)
# perfect(int(input('upper')))

###############3


# def sum_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(sum)
#     print(avg)
# sum_avg(int(input('num1')),int(input('num2')),int(input('num3')))


################4


# def odd_even(b):
#     for i in range(0,b):
#         if i%2==0:
#             print("EVEN",i)
#         else:
#             print("ODD",i)
# odd_even(int(input('upper')))



###############5


# def num(b):
#     c=0
#     for i in range(0,b+1):
#         if i%3==0 or i%5==0:
#             c+=i
#     print(c)
# num(int(input('upper')))



##############6


# def driver(speed):
#     if speed<=70:
#         print('ok')
#     elif speed>70:
#         c=speed-70
#         d=c//5
#         print('your point is',d)
#         if d>=12:
#             print('license suspend')
#     else:
#         print('be safe')
# driver(int(input('speed')))
    

################7


# def string(a,b):
#     if len(a)==len(b):
#         print(a)
#         print(b)
#     elif len(a)>len(b):
#         print(a)
#     else:
#         print(b)
# string(input('a'),input('b'))



##############8

# def square(b):
#     c={}
#     for i in range(1,b+1):
#         d=i*i
#         c[i]=d
#     print(c)
# square(int(input('upper')))



###################3.1

# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")


######################2

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)



#######################3

# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")


####################4



# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#         return sum
# print(sumofdigits(123))

##############5

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))

##############6

# def checkKey():
#     car ={"brand":  "ford","model":  "mustang","year":  1964}
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")

# checkKey()


#################4.1


# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)


###################2

# def multi(a,b):
#     multiply=a*b
#     return multiply
# print(multi(3,4))


###################3

# def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(avg)
# Avg(1,3,2)


###################4

# def voter(age):
#     if age>=18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)


###################5

# def distance(*kms):
#     if kms<20:
#         print("close")
#     elif kms < 50:
#         print('median')
#     else:
#         print('far')
# distance(20,30)



###########prathamesh que



# def sum(a):
#     c=0
#     for i in range(a):
#         c+=i
#     print(c)
# sum(int(input('upper'))) 



# def squre(a,b):
#     c=0
#     for i in range(a,b+1):
#         for j in range (i):
#             c+=i
#         print(c)
#         c=0
# squre(int(input('lower')),int(input('upper')))


###################### PROGRESS TRACKING

# def multipal(a,b,c,d):
#     e=b,c,d
#     f=0
#     for i in e:
#         for j in range(i):
#             f+=a
#         print(f)
#         a=f
#         f=0 ########### REMEMBER F=0 AGAIN
# multipal(int(input('1st num')),int(input('2nd num')),int(input('3rd num')),int(input('4th num')))



# def max(a,b,c):
#     if a>b and b>c or c>b and b>a:
#         print('2nd max is',b)
#     elif b>a and a>c or c>a and a>b:
#         print('2nd max is',a)
#     else:
#         print('2nd max is',c)
# max(int(input('1st num')),int(input('2nd num')),int(input('3rd num')))


############# MOST IMP


# a=[1,2,4,5,6]
# # a[2]='e'
# b=int(input('b'))
# c=input('jo')
# a[b:b]=c
# print(a)


# a=[1,2,3,4]
# b=[5,6,7,8]
# a.append(b)
# print(a)










