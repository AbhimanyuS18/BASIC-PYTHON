################FOR WRITE A DATA

# f=open('abhi.txt','w')
# for i in range(5):
#     name= input('name')
#     age=int(input('age'))
#     value=name+';'+str(age)+'\n'
#     f.write(value)
#     f.close


##################FOR READ A DATA


# f=open('abhi.txt','r') ########IMP TO READ########
# str=" "
# while str:
#     str=f.readline()
#     print(str)
#     f.close

# f=open('abhi.txt')
# data=f.read()
# print(data)


#######################1

# f=open('people.txt','w')
# for i in range(12):
#     name=input('name')
#     city=input('city')
#     value=name+'-'+city+'\n'
#     f.write(value)
#     f.close




# a=open('quetion3.txt','w')
# for i in range(5):
#     name=input('name')
#     city=input('city')
#     value=name+';'+city+'\n'
#     a.write(value)

# a.close()


####################MOST IMP IN FILES 


# with open("quetion3.txt", "r") as b:
#     content = b.readlines()
# for i in content:
#     if "bikaner" in i:
#         with open("bikaner.txt", "a") as f:
#             f.write(i)
#     elif "jaipur" in i:
#         with open("jaipur.txt","a") as d:
#             d.write(i)
#     else:
#         with open('other.txt','a') as s:
#             s.write(i)

######################3(ALSO IMP IN FILES)

# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# # value=str(banks_list)+'\n'
# with open('list.txt','a') as v:
# #     v.writelines(value)
#     for i in banks_list:
#         v.write(i+'\n')

#########USE OF APPEND IN FILES########

# with open('ab.txt','a') as y:
#     for i in range(2):
#         name=(input('name'))
#         y.write(name)


################JSON#########


###############USE OF JSON IN DIC ###########

#################python obj to json str == use dumps###########
################# json str to python obj == ude lods###########


# import json
# a={'a':20,'b':30,'c':30}
# j=json.dumps(a)
# print(j)
# print(type(j))
# b=json.loads(j)
# print(b)
# print(type(b))


#############USE OF JSON IN LIST#############


# import json
# a=[2,3,4,5]
# j=json.dumps(a)
# print(j)
# print(type(j))
# b=json.loads(j)
# print(b)
# print(type(b))

# import json
# a=(1,2,3,4)
# j=json.dumps(a)
# print(j)
# print(type(j))
# b=json.loads(j)
# print(b)
# print(type(b))

###############HOW TO MAKE FILE IN JSON###########

# import json
# c=[]       #############FILE CREATE BY LIST
# f=open('abhi.json','w')
# for i in range(3):
#     name=input('name')
#     age=input('age')
#     x={}
#     x.update({name:age})
#     c.append(x)
# json.dump(c,f)
# f.close


#############HOW TO READ A JSON FILE###########
#############CONVERT JSON DATA INTO PYTHON OBJ###########

# import json
# f=open('abhi.json','r')
# r=json.load(f)
# print(r)
# print(type(r))


################FILE CREATE BY DICT###############
################PYHTON OBJ(dict) INTO JSON DATA#########


# import json
# with open('arun.json','w') as a:
#     c={'a':1,'b':2,'c':3}
#     json.dump(c,a)
   

##############READ


# import json
# with open('arun.json','r') as b:
#     d=json.load(b)
#     print(d)
#     print(type(d))


#################HOW TO APPEND ANOTHER PYTHON OBJ INTO JSON DATA###############

# import json
# e=[]
# with open('arun.json','r+') as c:
#     s=[1,2,3,4]
#     a=json.load(c)
#     e.append(a)
#     e.append(s)
#     json.dump(e,c)
#     print(type(c))


# with open('nav.txt','w') as n:
#     a={'name':'abhimanyu','pogestion':'ceo of navgurukul','gender':'male'}
#     b=str(a)+'\n'
#     n.write(b)



# with open ('nav.txt','r') as a:
#     b= a.read()
#     print(type(b))
#     import json
#     with open('nav.json','w') as c:
#         json.dump(b,c)


# with open('pradeep.txt','w') as p:
#     d={}
#     for i in range(1):
#         name=input('name')
#         post=input('post')
#         gender=input('gender')
#         value='NAME  '+name+'\n'+'POST  '+post+'\n'+'GENDER  '+gender+'\n'
#         p.write(value)

# with open('pradeep.txt','r') as a:
#     b=a.read()
#     print(b)
#     print(type(b))
#     import json
#     with open('pradeep.json','w') as c:
#         json.dump(b,c)
#         print(type(c))


################MAHENDER QUE LOOP#############


# a=int(input('num'))
# b = str(a)
# m=1
# for i in range(len(b)-1):
#     x=a%10
#     a=a//10
#     m*=x
# d=m*a
# print(d)


# import json      
# a={1:'abhi',2:'aadi',3:'mahendera'}  
# b=json.dumps(a)
# print(b)
# print(type(b))
# c=json.loads(b) 
# print(c)
# print(type(c))

            












