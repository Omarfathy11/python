from re import M
import random


print ("i love python"); print ("i love programing")

if True:
    print ("i love python")
    print ("i love programing")


print(type(10))    
print(type(-10))    

print(type(10.20))    
print(type(-90.2334))  

print(type("hello world"))    

print(type([1, 2, 3, 4]))    

print(type((1, 2, 3, 4)))    

print(type({"one": 1, "two": 2}))    

print(type(2 == 2))

myVariable = "omar"
print(myVariable)


x = 10
x = "hello"
print(x)

help("keywords")

a, b ,c = 1, 2, 3

print(a)
print(b)
print(c)

print("hello\b world ")  # will remove o

# escape new line + \
print("hello \
i Love\
python")

# escape new line + back slacht
print("hello world \\")

# escape single qoute
print('hello world \'test\' ')

# line feed 
print('hello world\n second line')

# carrige return
print('123456\rabcd')

# horizonal tap 
print ("hello\tworld")

#concatenation
msg = "i Love"
lang = "python"
print(msg + " " + lang)

a = "first \
second \
third"

b =" a \
b \
c"    
print(a + "\n" + b)

mystringone = 'this is single qoute'
mystribgtwo = "this is double qoute"
mystringthree = 'this is single qoute "test"'
mystringfour =  "this is double qoute 'test'"


print(mystringone)
print(mystribgtwo)
print(mystringthree)
print(mystringfour)

mystringfive = """first
second 'test' "test" 
third"""

mystringsix = '''first
second \\
third'''

print(mystringfive)
print(mystringsix)

# indexing (acsess single item)
myString = "i love python"
print(myString[0])
print(myString[-4])


# slicing (Access multiply  items)
# [start:end] end not included
myString = "i love python"
print(myString[8:11]) #yth

print(myString[0::1]) # full data
print(myString[0::2])

a = "i love pyhton"
print(len(a))

b = "i   love   pyhton"
print(len(b))

# strip() rstrip() lstrip()
a = "      i love pyhton     "
print(a.strip())
print(a.lstrip())
print(a.rstrip())


a = "#### i love pyhton ####"
print(a.strip("#"))
print(a.lstrip("#"))
print(a.rstrip("#"))

# title()

b = " I love 2d python"
print(b.title())

# capitalize
b = " I love 2d python"
print(b.capitalize())

# zfill

c, d, f = "1", "12", "112"
print(c.zfill(3))
print(d.zfill(3))
print(f.zfill(3))

# lower()
a= "OMAR"
print(a.lower())


# upper()
a = "omar"
print(a.upper())

# split() rsplit()
a = "i love python and php"
print(a.split())

a = "i-love-python-and-php"
print(a.split("-"))

a = "i-love-python-and-php"
print(a.split("-", 2))


a = "i-love-python-and-php"
print(a.rsplit("-", 2))

# center()
e = "omar"
print(e. center(8)) # spaces
print(e. center(8, "#")) # hashes

# count()
f = " i love omar and not ali because omar is beutiful"
print(f.count("omar"))
print(f.count("omar", 0,12))

# swapcase
g = "I LOVE PYTHON"
f = "i love python"

print(g.swapcase())
print(f.swapcase())

# startswith()

g = "I LOVE PYTHON"
print(g.startswith("I"))
print(g.startswith("s"))
print(g.startswith("I", 7))
print(g.startswith("P", 7))


# endswith()

g = "I LOVE PYTHON"
print(g.endswith("N"))
print(g.endswith("v"))
print(g.endswith("N", 7))
print(g.endswith("P", 7))
print(g.endswith("N", 7,17))


# index(supstring, start , end)
a = "i love python"
print(a.index("p"))
print(a.index("p", 0,10))

# find(supstring, start , end)
b = "i love python"
print(a.find("p"))
print(a.find("p", 0,3)) # error -1

# rjust() ljust()
a = "omar"
print(a.rjust(7))
print(a.rjust(7, "#"))

b = "omar"
print(b.ljust(7))
print(b.ljust(7, "#"))

# splitlines
e = """first line
second line
third line"""
print(e.splitlines())


f= "firstline\nsecondline\nthirdline"

# expandtabs()

o = " i\tlove\tpython"
print(o.expandtabs(4))

one = "I Love Python 4G"
two = "I Love Python 4g" # because g small
print(one.istitle())
print(two.istitle())

three = ""
four = " "
print(three.isspace())
print(four.isspace())

five = "i love python"
six =  "I Love Python"

print(five.islower())
print(six.islower())

seven = "omar_fathy"
eight = "omarfathy11"
nine = "omar--fathy11"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

a= "aaalllll"
b = "akkkkk111"
print(a.isalpha())
print(b.isalpha())

a= "aaalllll"
b = "akkkkk111"
print(a.isalnum())
print(b.isalnum())

a = "hello one two three one one"
print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))

# join iterable 
mylist = ["omar", "mohamed", "fathy"]
print("-".join(mylist))
print(" ".join(mylist))
print(",".join(mylist))

name = "omar"
age = 20
rank = 10
print("my name is : " + name)

print("my name is: {}" .format(name))


print("my name is : %s" % name)
print("my name is : {} and my age is : {}" .format(name,age)) # new way 
print("my name is : %s and my age is : %d and my age is : %f" %(name,age,rank))
print("my name is : {:s} and my age is : {:d} and my age is : {:f}" .format(name,age,rank)) #new way

# %s string
# %d number
# %f float

n = "omar"
l = "python"
y = 5
print("my name is %s i am %s developer with %d years" %(n, l, y))
print("my name is {} i am {} developer with {} years" .format(n, l, y)) # new way


# control floating point number

myNumber = 10
print("my number is : %d" %(myNumber))
print("my number is : %f" %(myNumber))
print("my number is : %.2f" %(myNumber))

print("my number is : {:d}" .format(myNumber))# new way
print("my number is : {:f}" .format(myNumber))# new way
print("my number is : {:.2f}" .format(myNumber))# new way

# truncate string
mylongstring = " hello people i love you"
print("message is %s " % mylongstring)
print("message is %.5s " % mylongstring)

print("message is {:s} " .format (mylongstring))# new way
print("message is {:.5s} " .format( mylongstring))# new way
print("message is {:.13s} " .format( mylongstring))# new way

mymoney = 1234567
print("my money bank is : {:d}".format(mymoney))# new way
print("my money bank is : {:_d}".format(mymoney))# new way
print("my money bank is : {:,d}".format(mymoney))# new way

a, b, c = "one", "two", "three"
print("hello {} {} {} " .format(a, b, c)) # hello one two three
print("hello {1} {2} {0} " .format(a, b, c))# hello two three one 
#print("hello {1:d} {2:d} {0:d} ".format(a, b, c)) wrong ? 

myname = "omar"
myage = 20
print("my name is : {myname} and my age is : {myage}" )
print(f"my name is : {myname} and my age is : {myage}" )


# complex 

number = 5 + 8j
print(type(number))
print(" my number : {}" .format(number))

# you can convert int to float or complex
# you can convert float to int or complex
# you cannot complex to any type

print(100)
print(float(100))
print(complex(100))

print(100.40)
print(int(100.40))
print(complex(100.40))

#print(20+9j)
#print(int(20+9j))
#print(float(20+9j))


# addition 

print(10 + 20)
print(-10 + 20)
print(1 + 2.66)
print(1.3 + 2.5)

# substraction

print(10 - 20)
print(-10 - 20)
print(5 - 2.66)
print(4.3 - 2.5)


# multpliaction

print(3 * 10)
print(3 * 10)
print(5 + 3 * 10)
print((5 + 3 )* 10)

# Division

print(100 / 20)
print(int(100 / 20))

# moduls 

print(8 % 2)
print(9 % 2)
print(20 % 2)
print(22 % 5)

# Exponent

print(2 ** 5)
print(5 ** 4)

# floor Division

print(100 // 20)
print(119 // 20)
print(120 // 20)
print(130 // 20)
print(140 // 20)
print(142 // 20)

# list 

myfirstlist =  ["one", "two", "one", 1, True]
print(myfirstlist[1])
print(myfirstlist[-1])
print(myfirstlist[-3])

print(myfirstlist[1:3])
print(myfirstlist[:5])
print(myfirstlist[0:])

print(myfirstlist[::1])
print(myfirstlist[::2])

print(myfirstlist)

myfirstlist[1] = 2
myfirstlist[-1] = False
myfirstlist[0:3] = ['a', "b", "c"]


print(myfirstlist)

# append 

myfriends = ["omar", "mohmed", "fathy"]
myoldfriends = ["sayed", "hefny", "abdo"]

myfriends.append("ali")
myfriends.append(11)
myfriends.append(True)

myfriends.append(myoldfriends)

print(myfriends)
print(myfriends[6])
print(myfriends[6][2])

# extend

a = [1, 2, 3, 4]
b = ["one", "two", "three"]
c = ["four", "five"]


a.extend(b)
a.extend(c)

print(a)

# remove

o = [1, 2, 3, "one", "two", "two"]
o.remove("two")
print(o)

# sort 

y = [10, 4, 90, -39 ,-66 , 22]

y.sort()  #ترتيب
#y.sort(reverse=False) ترتيب
#y.sort(reverse=True) ترتيب معكوس
print(y)
#print(y)

#reverse()

z = [1, 2, 4, 100 , -22, "omar", 33]
z.reverse()
print(z)

# clear

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy

a = [1, 2, 3, 4]
b = a.copy()

print(a)
print(b)

a.append(5)

print(a)
print(b)

# count()

a = [1, 2,  3, 4, 1, 6, 1]
print(a.count(1))

# index()

d = ["omar", "fathy", "ali"]
print(d.index("ali"))

# insert

o = [1, 2, 3, "omar", 100]
#o.insert(0, "test")
o.insert(3, "test")

#print(o)
print(o)

# pop()

a = [1, 2, 3, 4, "omar"]
print(a.pop(3))


# Tuple syntax & type test

myfirsttupleone = ("one", "omar")
myfirsttupletwo = "one", "omar"

print(myfirsttupleone)
print(myfirsttupletwo)

print(type(myfirsttupleone))
print(type(myfirsttupletwo))

#  Tuple indexing

mythreetuple = (1, 2, 3, 4, 5)
print(mythreetuple[0])
print(mythreetuple[-1])
print(mythreetuple[-3])

# tuple asssign values

myfourtuple = (1, 2, 3, 4, 5)

#myfourtuple[2] = "three"
#print(myfourtuple) # tuple' object does not support item assignment

# tuple items

myfiveTuple = ("omar", "fathy", 1, 2, 3, True)
print(myfiveTuple[1])
print(myfiveTuple[-1])

# tuple with one element 

mytuple1 = ("omar",)
mytuple2 = "omar",

print(mytuple1)
print(mytuple2)

print(type(mytuple1))
print(type(mytuple2))


print(len(mytuple1))
print(len(mytuple2))

# tuple concations

a = (1, 2, 3, 4, 5)
b = (6, 7)

c = a + b 
d = a + ("omar", "fahy") + b
print(c)
print(d)

# tuple list, string repeat (*)

mystring = "omar"
mylist = [1, 2]
mytuple = ("omar", "fathy")

print(mystring * 6)
print(mylist * 6)
print(mytuple * 6)

# methods => count()

a = (1, 2, 3, 4, 5, 1, 2, 1)
print(a.count(1))

# methods => index()

b = (1, 2, 3, 4, 5)
print("the position of index is : {:d}" .format (b.index(2)))
print(f"the position of index is : {b.index(2)}")

# tuple destruct 

a= ("A", "B", 4, "C")

X, Y, _, Z = a

print(X)
print(Y)
print(Z)

# set 

# not orderd and not indexed

mysetone = {"omar", "fathy", 100}
print(mysetone)
#print(mysetone[0])

# slicing cnt be done

mysettwo = {1, 2, 3, 4}

#print(mysettwo[0:3])

# has only immutable data types

#mysetthree = {"omar", "fathy", 100, 12.3, True, [1, 2, 3]} # unhasable type ' list '
mysetthree = {"omar", "fathy", 100, 12.3, True, (1, 2, 3)}
print(mysetthree)

# items is uniqe

mysetfour = {1, 2, "one", 1}
print(mysetfour)

# set methods 

a = {1, 2, 3}
a.clear()
print(a)

# union

a = {1, 2, 3}
b = {"one", "two", "three"}
x = {12, False}

print(a | b |x)
print(a.union(b, x))

# add

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d) 

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove 

g = {1, 2, 3, 4}
g.remove(1)
#g.remove(7)

print(g)


# discard 

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)

print(h)

# pop()

a = {1, 2, 3, 4}
print(a.pop())

# update()

j = {1, 2, 3, 4}
k = {"one", "two", 1}
j.update(["css", "java"])
j.update(k)

print(j)

# difference

a = {1, 2, 3, 4}
b  = {1, 2, "one", "two"}
print(a)

print(a.difference(b))
print(a)

print("=" * 30)


# difference_update

c = {1, 2, 3, 4}
d  = {1, 2, "one", "two"}
print(c)
c.difference_update(d)
print(c)

print("=" * 30)

# intersecions

a = {1, 2, 3, 4, "x"}
b = {"omar", 2, "x"}
print(a)
print(a.intersection(b)) # a & b
print(a)


# intersecions_update

c = {1, 2, 3, 4, "x"}
d = {"omar", 2, "x"}
print(c)
c.intersection_update(d) # c & d
print(c)

# symetric_difference

i = {1, 2, 3, 4, 5, "x"}
j = {"omar", 1, 2 , "x"}
print(i)
print(i.symmetric_difference(j))
print(i)

print("=" * 30)

# symetric_difference_update()

k = {1, 2, 3, 4, 5, "x"}
l = {"omar", 1, 2 , "x"}
print(k)
k.symmetric_difference_update(l)
print(k)

print("=" * 30)

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b)) #  a موجودة في b  هل عناصر 
print(a.issuperset(c)) #  a موجودة في c  هل عناصر 

print("=" * 30)

# issubset()
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issubset(b)) #  b موجودة في a  هل عناصر 
print(a.issubset(c)) #  c موجودة في a  هل عناصر 

print("=" * 30)

# isdisjoint()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {6, 7, 8}
print(a.isdisjoint(b)) #  b منفصلة عن  a  هل عناصر 
print(a.isdisjoint(c)) #  c منفصلة عن a  هل عناصر 

print("=" * 30)

# dictionery
# isunqie يعني مينفعش تكرر الاسم مرتين

user = {
    "name" : "omar",
    "age" : 20,
    "country" : "egypt",
    "skills" : ["html", "css", "java"],
    "rating" : 19
}

print(user)
print(user["country"])
print(user.get("name"))


print(user.keys())
print(user.values())

# two dimiontion dictionery

languages = {
    "one": {
        "name": "java",
        "progress": "40%"
    },
    "two" : {
        "name": "css",
        "progress" : "80%" 
    }
    
}

print(languages)
print(languages["one"])
print(languages["two"]["name"])

# dictionery length

print(len(languages))
print(len(languages["one"]))


# create dictionery from variables

frameworkone = {
    "name" : "node",
    "progress" : "80%" 

}


frameworktwo = {
    "name" : "flusk",
    "progress" : "80%" 

}


frameworkthree = {
    "name" : "django",
    "progress" : "80%" 

}

allframeworks = {
    "one": frameworkone,
    "two": frameworktwo,
    "three": frameworkthree
}

print(allframeworks)

print("=" * 30)

# clear 

user = {
    "name" : "omar"
}
print(user)
user.clear()
print(user)

print("=" * 30)

# update()

user = {
    "name" : "omar"
}
print(user)
user["age"] = 20
print(user)
user.update({"country": "egypt"})
print(user)

# copy()

user = {
    "name" : "omar"
}
print(user)
b = user.copy()
print(b)
user.update({"skkils":"figting"})
print(user)
print(b)

# keys() values()

print(user.keys())
print(user.values())


print("=" * 30)

# setdefault()

member = {
    "name" : "omar"
}
print(member)
print(member.setdefault("name", "fathy"))
print(member.setdefault("age", 20))

# popitem  بتجيب اخر حاجة في ال ميثود

member = {
    "name" : "omar",
    "skkils":"figting"
}
print(member)
member.update({"age": 20})
print(member.popitem())

print("=" * 30)

# items

member = {
    "name" : "omar",
    "skkils":"figting"
}

allitems = member.items()
print(allitems)
member["age"] = 20
print(allitems)

print("=" * 30)

# fromkeys()

a = ('name1', 'name2')
b = "oamr"

print(dict.fromkeys(a, b))

# boolean

name = ""
print(name.isspace())

print("=" * 30)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 30)

# true values

print(bool("omar"))
print(bool(1010))
print(bool(63.38))
print(bool([1, 2, 3]))
print(bool(True))

print("=" * 30)


# False values

print(bool(""))
print(bool(0))
print(bool())
print(bool([]))
print(bool(False))
print(bool(None))

print("=" * 30)

age = 20
country = "egypt"
rank = 10

# and لازم يتحقق الشرطين
print(age > 10 and country == "egypt" and rank > 9)
print(age > 20 and country == "egypt" and rank > 9)


print("=" * 30)
#or  لازم يتحقق احد الشرطين


print(age > 10 or country == "egypt" or rank > 9)
print(age > 20 or country == "egypt" or rank > 9)


# not

print(not age > 10) # not true = false

print("=" * 30)

# Assignment operators

x = 10 # var one
y = 20 # var two

# var one = Self [operator] var two
# var one  [operator]= var two

#x += y

x -= y
print(x)

print("=" * 30)
# comparison operator
# Equal + not Equal

print(100 == 100)
print(100 == 200)
print(100 == 100.00)

print("=" * 30)

print(100 != 100)
print(100 != 200)
print(100 != 100.00)

print("=" * 30)

# greater than + less than

print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 50)

print("=" * 30)

print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print(100 < 50)

print("=" * 30)

# greater than  or Equal+ less than or Equal

print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
print(100 >= 50)

print("=" * 30)

print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)
print(100 <= 50)

print("=" * 30)


# type conversion

# str()

a = 10
b = 20.22

print(type(str(a)))
print(type(str(b)))

print("=" * 30)

# tuple()

c = "omar"
d = [1, 2, 3, 4]
f = {"o", "v", "s"} # set
g = {"name" : "omar", "id" : 20} # dictionery

print(tuple(c))
print(tuple(d))
print(tuple(f))
print(tuple(g))

print("=" * 30)

# list()

c = "omar"
d = (1, 2, 3, 4)
f = {"o", "v", "s"} # set
g = {"name" : "omar", "id" : 20} # dictionery

print(list(c))
print(list(d))
print(list(f))
print(list(g))

print("=" * 30)

# set()

c = "omar"
d = (1, 2, 3, 4)
f = ["o", "v", "s"]
g = {"name" : "omar", "id" : 20} # dictionery

print(set(c))
print(set(d))
print(set(f))
print(set(g))

print("=" * 30)


# dict()

d = [["name", "omar"], ["id", 1]]
e = (("a", 1), ("b", 2))

print(dict(d))
print(dict(e))

print("=" * 30)


# User Input

#fName = input('what\'s Is Your First Name ?')
#mName = input('what\'s Is Your Middle Name ?')
#lName = input('what\'s Is Your Last Name ?')

#fName = fName.strip().capitalize()
#mName = mName.strip().capitalize()
#lName = lName.strip().capitalize()


#print(f"Hello {fName} {mName} {lName} Happy to see you")


# practical slice email

# email = "omar_fathyy@yahoo.com"

#print(email[0:email.index("@")])

#TheName = input("what\'s your name ?").strip().capitalize()
#TheEmail = input("what\'s your Email ?").strip().capitalize()

#UserName =  TheEmail[0:TheEmail.index("@")]
#Website = TheEmail[TheEmail.index("@") +1 :]

#print(f"hello {TheName} the email is {TheEmail}")
#print(f" UserName is {UserName} \n thewebsite is {Website}")

# Age input 

#age = int(input('what\'s your Age ?').strip())

# Get age in all time Units

#months = age * 12
#weeks = months * 4
#days = weeks * 365
#minutes  = hours * 60
#seconds = minutes * 60

#print(' You Lived For :')
#print(f"{months} months.")
#print(f"{weeks:,} weeks.")
#print(f"{days:,} days.")
#print(f"{hours:,} hours.")
#print(f"{minutes:,} minutes.")
#print(f"{seconds:,} seconds..")


print("=" * 30)

# if, elif, else

#uName = "omar"
#uCountry = "ksa"
#isstudent = "no"
#cName = "java course"

#cPrice = 100

#if uCountry == "egypt" or "iran":

    #if isstudent == "yes":

        #print(f"hello {uName} because you are from {uCountry} And yOUR Student")
        #print(f"the course {cName} the price is : ${cPrice - 90}")

   # else:
      #  print(f"hello {uName} because you are from {uCountry}")
       # print(f"the course {cName} the price is : ${cPrice - 80}")


#elif uCountry == "ksa" or "spain":

    #print(f"hello {uName} because you are from {uCountry}")
    #print(f"the course {cName} the price is : ${cPrice - 50}")

#else :
    #print(f"hello {uName} because you are from {uCountry}")
    #print(f"the course {cName} the price is : ${cPrice - 30}")


Country = "mm" 

if Country == "egypt":
    print(f"the weather in {Country} is 13")

elif Country == "ksa":
     print(f"the weather in {Country} is 14")

else :
    print("contry is not in the list")

movierate = 18
age = 20

if age < movierate :
    print("movie is not good for you")

else:
    print("movie is  good for you")

print("movie is not good for you" if age < movierate else "movie is  good for you")


print("=" * 30)

# note
#print("you can write the first letter or full name in the time unit")

# collect age 

#age =  input("please enter your age").strip()

# collect unit time data

#unit = input("please chosee time unit : months, weeks, days ").strip().lower()

# get time units


#months = int(age) * 12
#weeks = months * 4
#days = int(age) * 365

#if unit == "months"  or unit == "m" :
 #   print("you chossed the unit months")
   # print(f"you lived for{months:,} months")

#elif unit == "weeks" or unit == "w" :
 #   print("you chossed the unit weeks")
  #  print(f"you lived for{weeks:,} weeks")

#elif unit == "days" or unit == "d" :
 #   print("you chossed the unit days")
  #  print(f"you lived for{days:,} days")


  #  Membership Operator

# string 

name = "omar"

print("o" in name)
print("f" in name)

print("=" * 30)

# list

friends = ["omar", "mohamed", "fathy"]
print("omar" in friends)
print("ali" not in friends)

print("=" * 30)

# if, elif, else

#uName = "omar"
#Country = ["ksa", "egypt"]
#cName = "java course"

#mycountry = "aaa"
#cPrice = 100

#if mycountry in Country :


    #    print(f"hello {uName} because you are from {Country} And yOUR Student")
   #     print(f"the course {cName} the price is : ${cPrice - 90}")

#else :
 #   print(f"hello {uName} because you are from {Country}")
  #  print(f"the course {cName} the price is : ${cPrice - 30}")

print("=" * 30)

# partical membership contain

# liat contains admins o

#admins = ["omar", "ahmed", "said"]

# login

#name = input("please type your name ")

#if name in admins:
    #print(f"hello {name} welcome back")

    #option = input("delete or update name ?")
    
    # update option
    #if option == "update" or option == "u":

    #    newname = input("please type new name ")    

   #     admins[admins.index(name)]= newname

  #      print("name updated ")
 #       print(admins)

#    elif option == "delete" or option == "d":

        #admins.remove(name)

       # print(" name deleted")

      #  print(admins)

    #else:

        #print(" wrong option choosed")   
#else:
     #status = input("not admin, add  you y, n ? ")

     #if status == "y":

        #admins.append(name)

        #print(admins)

# while + else

number = 0 

while number < 15:
    print(number)

    number += 1

print(" loop is done")


print("=" * 30)

# while

myfriends = ["omar", "ali", "fady", "mai", "said", "mona", "rolla", "wagdy", "salah", "adel"]

a = 0

while a < len(myfriends):
    print(f"#{str(a).zfill(3)} {myfriends[a]}")

    a += 1
    
print("=" * 30)
   
myfavouratewebs = []

maximumwebs = 5

while maximumwebs > 0 :
    #web = input("website name without http://")

   # myfavouratewebs.append(f"https://{web}")

    maximumwebs -= 1

    print(f"website added {maximumwebs} places left")

    print(myfavouratewebs)

myfavouratewebs.sort()

index = 0 

while index < len(myfavouratewebs):

    print(myfavouratewebs[index])

    index += 1

# simple password guess

#tries = 3

#mainpassword = "omar123"

#inputpassword = input("write your password : ")
 
#while inputpassword != mainpassword :

    # tries -= 1

   # print(f"wrong password  {'last' if tries == 0 else tries } chance left ")

   # inputpassword = input("write your password : ")

   # if tries == 0:

       # print("all tries is finished")

       # break

#else:

 #   print("correct password")
    

print("=" * 30)


# for 

mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in mynumbers :
    
    if number % 2 == 0:
        print(f"this number {number} is even")
    else:
         print(f"this number {number} is odd")

print("=" * 30)

# range loop

myrange = range(1, 100)

for number in myrange :

    if number % 2 == 0:
        print(f"this number {number} is even")
    else:
         print(f"this number {number} is odd")

print("=" * 30)
 
myskills = {
    "python":"90%",
    "html":"80%",
    "java":"70%",
    "c++":"60%"
}

for skill in myskills :

    print(f"my progress in lang {skill} is {myskills.get(skill)}")

print("=" * 30)

# nested loop 

peoples = {
    "omar":{
        "c++": "80%",
        "python": "60%",
        "java": "90%"
    },
     "ali":{
        "c++": "70%",
        "python": "40%",
        "java": "20%"
     },
       "ahmed":{
        "c++": "10%",
        "python": "50%",
        "java": "30%"
     },
}

for name in peoples :

    print(f"skills and progress for {name} is :")

    for skill in  peoples[name]:

        print(f"{skill} => {peoples[name][skill]}")

print("=" * 30)

# continue بيتجاهل

mynumbers = [1, 2, 3, 7, 19, 12, 20]

for number in mynumbers:
    
    if number == 12:

        continue
    print(number)

print("=" * 30)

# break بيوقف

mynumbers = [1, 2, 3, 7, 19, 12, 20]

for number in mynumbers:
    
    if number == 12:

        break
    print(number)   

print("=" * 30)

# pass 

mynumbers = [1, 2, 3, 7, 19, 12, 20]

for number in mynumbers:
    
    if number == 12:

        pass
    print(number)        

# loop
print("=" * 30)

myskills= {
        "c++": "80%",
        "python": "60%",
        "java": "90%"
    }

for skill_key, skill_value in myskills.items():

    print(f"{skill_key} => {skill_value}")    

print("=" * 30)

peoples = {
    "omar":{
        "c++": "80%",
        "python": "60%",
        "java": "90%"
    },
     "ali":{
        "c++": "70%",
        "python": "40%",
        "java": "20%"
     },
       "ahmed":{
        "c++": "10%",
        "python": "50%",
        "java": "30%"
     },
}

for name_key, name_value in peoples.items():

    print(f"{name_key} progress is : ")

    for skill_key, skill_value in name_value.items():

     print(f" -{skill_key} => {skill_value}")


print("=" * 30)

# function

def function_name():

    return "hello python from isnside function"

datafromfunction = function_name()

print(datafromfunction)


def say_hello(name):

    print(f"hello {name}")

say_hello("omar")
say_hello("ali")
say_hello("fathy")

print("=" * 30)

def Addition(n1, n2):

    if type(n1) != int or type(n2) != int:
        print("only intger allowd ")
    else:
        print(n1+n2)

print("=" * 30)
       

Addition("omar",222)  


def full_name(first, middle, last):

    print(f"Hello {first.strip().capitalize()} {middle.strip().capitalize()} {last.strip().capitalize()}")

full_name("omar",      "mohemd",              "FATHY")

print("=" * 30)

def say_hello(*peoples):

    for name in peoples:

        print(f"hello {name}")

say_hello("oamr", "ahmed", "fady")

print("=" * 30)


def show_details(name, *skills):

    print(f"hello {name} your skills is : ")

    for skill in skills:

        print(f"{skill}")

show_details("omar", "java", "html", "python")   
show_details("fathy", "java", "html", "python", "php", "mysql")     

print("=" * 30)

def say_hello(name, age ="UnKnown", country="UnKnown"):

    print(f"hello {name} your age is {age} your country is {country}")

say_hello("omar", 21, "egypt")
say_hello("omar", 21)
say_hello("omar")

print("=" * 30)

myskills={
    "python" : "70%",
     "java" : "40%",
     "php":"20%"
}

def show_skills(**skills):

    print(type(skills))

    for skill, value in skills.items():
        print(f"{skill} => {value}")

show_skills(**myskills)      

print("=" * 30)


mytuple = ("java", "c++", "python")

myskills = {
    "GO" : "80%",
    "js" : "20%",
    "c": "50%"
}

# tuple () بنضع لها نجمة واحدة 
# dic {} بنضع لها نجمتين

def show_skills(name, *skills, **skillswithprogress):

    print(f"hello {name} \n skills without progress :")

    for skill in skills:
        print(f" - {skill}")
    print(f" skills with progress : ")
    for skill_key, skill_value in skillswithprogress.items():
        print(f"{skill_key} => {skill_value}")

show_skills("omar", *mytuple, "c++", **myskills, python="70%")   

print("=" * 30)

# function scope

l = 1 # global scope

def one():

    global l

    l = 2

    print(f"print variable from function scope {l}")

def two():
    
    l = 4

    print(f"print variable from function scope {l}")

print(f"print variable from global Scope {l}")
one()
two()
print(f"print variable from global Scope After one funcion Is called {l}")

print("=" * 30)

# Recursion

def cleanword(word):

    if len(word) == 1:

        return word
    print(f"start function {word}")

    if word[0] == word[1]:

            print(f" before condition {word}")


            return cleanword(word[1:])

    print(f" before return {word}")

    return word[0] + cleanword(word[1:])

    # stach [world]

print(cleanword("wwwoooorrrldd"))    

print("=" * 30)

# lambda

def say_hello(name, age):
    return f"hello {name} your age is {age}"
hello =  lambda name, age : f"hello {name} your age is {age}"

print(say_hello("omar", 21))
print(hello("ahmed", 21))

print("=" * 30)


room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooom are dirty")
print(room)

x =0
y= 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0

print("Before cleaning the room I detect all of these random dirts")
print(room)

x =0
y= 0

while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print("Vaccum in this location now,",x, y)
            room[x][y] = 0
            print("cleaned", x, y)
        y+=1
    x+=1
    y=0

print("Room is clean now")
print(room)

print("=" * 30)


player = 'x'
opponent = 'o'

board = [
	[ 'x', 'o', 'x' ],
	[ 'o', 'o', 'x' ],
	[ '_', '_', '_' ]
]
def isMovesLeft(board):
	for i in range(3):
		for j in range(3):
			if (board[i][j] == '_'):
				return True
	return False

def evaluate(board) :
	for row in range(3) :	
		if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :	
			if (board[row][0] == player) :
				return 10
			elif (board[row][0] == opponent) :
				return -10

	for col in range(3) :
		if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
			if (board[0][col] == player) :
				return 10
			elif (board[0][col] == opponent) :
				return -10

	if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
		if (board[0][0] == player) :
			return 10
		elif (board[0][0] == opponent) :
			return -10

	if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
		if (board[0][2] == player) :
			return 10
		elif (board[0][2] == opponent) :
			return -10

	return 0
def minimax(board, depth, isMax):
	score = evaluate(board)

	if (score == 10):
		return score

	if (score == -10):
		return score

	if (isMovesLeft(board) == False):
		return 0

	if (isMax):	
		best = -1000

		for i in range(3):		
			for j in range(3):
				if (board[i][j]=='_'):
					board[i][j] = player
					best = max(best, minimax(board, depth + 1, False))
					board[i][j] = '_'
		return best

	else:
		best = 1000

		for i in range(3):		
			for j in range(3):
				if (board[i][j] == '_'):
					board[i][j] = opponent
					best = min(best, minimax(board, depth + 1, True))
					board[i][j] = '_'
		return best
def findBestMove(board):
	bestVal = -1000
	bestMove = (-1, -1)

	for i in range(3):	
		for j in range(3):
			if (board[i][j] == '_'):
				board[i][j] = player
				moveVal = minimax(board, 0, False)
				board[i][j] = '_'

				if (moveVal > bestVal):			
					bestMove = (i, j)
					bestVal = moveVal

	print("The value of the best Move is:", bestVal)
	print()
	return bestMove
bestMove = findBestMove(board)

print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])           

print("=" * 30)

x = [1, 2, 3, 4, False]

if all(x):
    print("all elements is true")

else :
     print("theres at least onre element is false")


print("=" * 30)

x = [0, False]

if any(x):
    print("theres at least one element is true")

else :
     print("theres no  element is true")

print("=" * 30)

print(bin(100))

print("=" * 30)

a = 10
b = 20 
print(id(a))

print("=" * 30)


class member:

    not_allowed_name = ["shit", "hell", "off"] 
    users_num = 0

    @classmethod
    def show_users_count(cls):

        print(f"we have {cls.users_num} users in our system")

    @staticmethod
    def say_hello():
        print("hello people")    





    


    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name   
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        member.users_num += 1


    def full_name(self):
        if self.fname in member.not_allowed_name:
            raise ValueError("name not allowed")

        return f"{self.fname} {self.mname} {self.lname}"
    def name_with_title(self):
        if self.gender == "male":
          return f"hello mr {self.fname}"   
        elif self.gender == "female" :
          return f"hello miss {self.fname}"   
        else :
            return f" {self.fname} {self.mname} {self.lname}" 
    def get_all_info(self):
        return f"{self.name_with_title()}, your full name is :{self.full_name()}"       

    def delete_user(self):
        member.users_num -= 1

        return f"{self.fname} delelted"


print(member.users_num)


member_one = member("omar", "mohamed", "fathy", "male")       
member_two = member("abdo", "khaled", "hassanin", "mmm")       
member_three = member("salma", "ahmed", "ali", "female")       

print(member_one.delete_user())

print(member.users_num)


print(member_one.full_name())
print(member_two.name_with_title())
print(member_one.get_all_info())

member.show_users_count()
member.say_hello()
 
  #  print(member_one.fname, member_one.mname, member_one.lname)
   # print(member_two.fname, member_two.mname)
    #print(member_three.fname)


print("=" * 30)

class skill:

    def __init__(self):

        self.skills = ["html", "css", "js"]

    def __str__(self) :

        return f"this is my skills {self.skills} "  

    def __len__(self):

        return len(self.skills)    

profile = skill()
print(profile)        
print(len(profile))
profile.skills.append("php")
print(len(profile))

print("=" * 30)

class food:

    def __init__(self, name, prise):

        self.name = name

        self.prise = prise

        print(f"{self.name} food is created from base class")

    def eat(self) :

        print("eat method from base class ") 

class Apple(food):

    def __init__(self,name,prise,amount):

        self.amount = amount

        food.__init__(self,name,prise) # create instance from base class

        print(f"{self.name} apple is created from derived class and prise {self.prise} and amount {self.amount}") 

    def eat(self) :

        print("eat method from drived class ")     

#food_one = food("pizza")
food_two = Apple("pizza",120,400)    
food_two.eat() 

print("=" * 30)

class Baseone:
    def __init__(self):
        print("baseone")

    def func_one(self):
        print("one")    

class BaseTwo:
    def __init__(self):
        print("BaseTwo")   
    def func_two(self):
        print("two")  
class Drived(Baseone, BaseTwo):
    pass


my_fav = Drived()
my_fav.func_one()
my_fav.func_two()

print("=" * 30)

class A:
    def do_somthing(self):
        print("FROM class A")
        raise NotImplementedError("Derived class must implement this method")

class B(A):
    def do_somthing(self):
        print("FROM class B")

class c(A):
    def do_somthing(self):
        print("FROM class C")



my_instance = c()
my_instance.do_somthing()





class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"{self.name}"
    @property
    def age_in_days(self):
        return self.age * 365

one = Person("ahmed", 50)    

print(one.name)
print(one.age)
print(one.say_hello())
print(one.age_in_days)
 
print("=" * 30)

# encsulation نظام التغليف

class Member:
    def __init__(self, name):
         self.__name = name # private
    def say_hello(self):
        return f"hello {self.__name}"     

one = Member("Ahmed")
#print(one.__name)
print(one.say_hello())
print(one._Member__name)

print("=" * 30)

class Member:
    def __init__(self, name):
         self._name = name # protcted
one = Member("Ahmed")
print(one._name)

print("=" * 30)

class Member:
    def __init__(self, name):
         self._name = name
    def say_hello(self):
        return f"hello {self.__name}"     

    def get_name(self): # Getter
        return self._name
    def set_name(self, new_name):
        self.__name = new_name

one = Member("Ahmed")
one.set_name('ali')    
print(one.get_name())   
one.set_name('ali')    







