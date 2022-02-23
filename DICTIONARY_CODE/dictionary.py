# dic1={1:10,2:20}
# dic2={3:30,2:40}
# dic3={4:40,5:50}
# dic1[7]=70
# print(dic1)
# a=dic1.keys()
# print(a)
# b=dic1.values()
# print(b)
# c=dic1.items()
# print(c)
# dic1.update( dic2)
# dic1.update(dic3)
# print(dic1)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   "year":1997
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   "point":2020
# }
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   "point":2020
# }
# print(len(thisdict))

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", 12345678, "blue"]
# }
# print(thisdict["colors"][1])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)

#################     values of dict  ###########

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.values()
# print(x)

################   keys of dict   ##################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# print(x)

#############     DICT METHODS     #########
##########     clear  ########

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

#######   copy    ####

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.copy()
# print(x)

############   FROMKEYS  ##########

# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# y = 4,5
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

###########     GET    ###########

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("model")
# print(x)

############    ITEMS  ###############

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# print(x)

# ############  KEYS  ############
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.keys()
# print(x)

#############    POP  #############

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop("model")
# print(car)

#####   popitem  #####

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.popitem()
# print(car)
 
#########   update   #######

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.update({"color": "White"})
# print(car)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.values()
# print(x)

# for i in dic1:
#     for j in dic2:
#         if i ==j:
#             print(dic1[i]+dic2[j])
#             # print(dic1.values()+dic2.values())
 
 #####2

# a={'name':'raju', 'marks':50}
# b=input('enter')
# if b in a:
#     print('exist')
# else :
#     print('not exite')


#####3

# a={'data1':100,'data2':-54,'data3':247}
# b=a.values()
# c=0
# for i in b:
#     print(i)
#     c+=i
# print(c)

######4



# a={1:'navgurukul',2:'in',3:{'a':'welcome','b':'to','c':'dharmshala'}}
# del a[3]['a']
# print(a)



######5

# a=['one','two','three','four','five']
# b=[1,2,3,4,5]
# c={}
## c=dict(zip(a,b))
## print(c)
# for i in range(len(a)):
#     c[a[i]]=b[i]
# print(c)




# # #######6
# a={'ball':'red','bat':4,'wicket':8,'ball':'green','bat':3}
 

# #### print(a)
# l=[]
# l1=[]
# dic={}
# for i,j in a.items():
    
#     l.append(i)
#     l1.append(j)
# l.pop(0)
# l1.pop(0)
# # print(dict(zip(l,l1)))
# for k in range(len(l)):
#     dic[l[k]]=l1[k]
# print(dic)


# ##########7

# a=[{'first':'1'},{'second':'2'},{'third':'1'},{'four':'4'},{'five':'5'},{'six':'9'}]
# b=[]
# for i in a:
#     for j in i:
#         if i[j] not in b:
#             b.append(i[j])
#             print(b)





#######8

# c={}
# for i in range (10):
#     a=input('name')
#     b=int(input('marks'))
#     c[a]=b
# print(c)



#########9



# a='mississippi'
# c={}
# for j in a:
#     b=a.count(j)
#     c[j]=b
# print(c)



#########10


# a={'alex':['subj1','subj2','subj3'],'david':['subj1','subj2']}
# c=0
# for j in a.values():
#     c+=1
#     print(c)    




#############ROMAN NUMBER#############



# a=int(input("num"))
# value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
# symble=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
# roman=""
# i=0
# while a>0:
#     b=a//value[i]
#     a=a%value[i]
#     while b:
#         roman=symble[i]
#         b-=1
#     i+=1
# print(roman)



# r = { 1:'I',4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M', 4000:'MV̅', 5000:'V̅', 9000:'MX̅', 10000:'X̅', 40000:'X̅L̅', 50000:'L̅', 90000:'X̅C̅', 100000:'C̅' }
# v = [ 100000,90000,50000,40000,10000,9000,5000,4000,1000,900,500,400,100,90,50,40,10,9,5,4,1 ]
# f = ''
# usr = int(input('Enter number: '))
# # usr=79
# for i in v:
#     if usr!=0 and usr<300000:
#         c=usr//i
#         if c!=0:
#             for j in range(c):
#                 f+=r[i]
#         usr%=i
# else:
#     print('This programme only works for 3 Lakhs Numbers')
# print(f)

    




    

