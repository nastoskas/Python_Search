"""x=100
if x:
    print("1-Got a true expression value.")
    print(x)
y=0
if y:
    print("2-Got true expression value.")
    print(y)
    print("Goodbye")
#-----------------------------------------------#
x=100
if x:
    print("Got a true expression value.")
    print(x)
else:
    print("Got a false expression value.")
    print(x)
    print("Goodbye")

#------------------------------------------------#
x=2
if x==3:
    print("X equals 3.")
elif x==2:
    print("X equals 2.")
else:
    print("X equals to something else.")

fruit='apple'
is_apple = True if fruit=='apple' else False
print(is_apple)
#-------------------------------------------------#
x=3
while x<5:
    print(x,"still in the loop")
    x+=1
x=6
while x<5:
    print(x,"still in the loop")
#-------------------------------------------------#
x=3
while x<5:
    print(x,"still in the loop.")
    x+=1
else:
    print(x,"out of the loop.")
#-------------------------------------------------#

x=0
while x<10:
    x+=1
    if x%2!=0:
        continue
    print(x,"even number")
    if x==6:
        break
#-------------------------------------------------#

for (x,y) in [('a',1),('b',2),('c',3),('d',4)]:
    print(x)
#--------------------------------------------------#

l = range(0,6,2)
for x in l:
    print(x)

#---------------------------------------------------#
fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print(fruits[index])
#--------------------------------------------------#

ages = {'Sam': 4, 'Mary': 3, 'Bill': 2}
for name in ages.keys():
    print(name,ages[name])
#--------------------------------------------------#

li = [3,6,2,7]
li_comprehension = [elem*2 for elem in li]
print(li_comprehension)
#--------------------------------------------------#

li = [('a',1), ('b',2), ('c',7)]
li_comp = [n*3 for (x,n) in li]
print(li_comp)
#--------------------------------------------------#

def subtract (a,b):
    return a-b
li = [(6, 3), (1, 7), (5, 5)]
li_comp = [subtract(y,x) for  (x,y) in li]
print(li_comp)
#---------------------------------------------------#

li = [3,6,2,7,1,9]
li_comp = [elem*2 for elem in li if elem > 4]
print(li_comp)
#---------------------------------------------------#

li = [3,2,4,1]
li_comp = [elem*2 for elem in [item+1 for item in li]]
print(li_comp)
#---------------------------------------------------#

nested = [[3,'a',9],[2,7],[4,1,8,'d']]
flatten = [val for elem in nested for val in elem]
#ili
flatten1 = []
for elem in nested:
    for val in elem:
        flatten1.append(val)
print(flatten1)
#----------------------------------------------------#

from script import divide
print(divide(6,3))
#---------------Class------------------------------#

class Student:
    def __init__(self,n,a):
        self.full_name = n
        self.age = a


    def get_age(self):
        return self.age

b = Student("Marko",21)
print(b.get_age(),b.full_name)
print(getattr(b,'get_age')())
print(hasattr(b,'age'),hasattr(b,'get_age'),hasattr(b,"birthday"))
class Sample:
    x=23
    def increment(self):
        self.__class__.x += 1

c = Sample()
c.increment()
d = Sample()
d.increment()
d.increment()
print(c.__class__.x,d.__class__.x)
#--------------class vs data attribute----------------#

class Counter:
    overall_total = 0 #class
    def __init__(self):
        self.my_total = 0 #data
    def increment(self):
        Counter.overall_total = Counter.overall_total+1
        self.my_total = self.my_total+1
b = Counter()
c = Counter()
b.increment()
c.increment()
c.increment()
print(b.my_total,b.__class__.overall_total)
print(c.my_total,c.__class__.overall_total)
#----------------------------------------------------#

class Parent:
    parent_attr = 100 #class attribute
    def __init__(self):
        print("Calling parent constructor.")
    def parent_method(self):
        print("Calling parent method.")
    def set_attr(self,attr):
        Parent.parent_attr = attr
    def get_attr(self):
        print("Parent attribute:",Parent.parent_attr)
class Child(Parent):
    def __init__(self):
        #super().__init__()
        print("Calling child constructor.")
    def child_method(self):
        print("Calling child method.")
c = Child()
c.child_method()
c.parent_method()
c.set_attr(200)
c.get_attr()
#----------------------------------------------------#

class Student:
    def __init__(self,n,a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age
class AIStudent(Student):
    def __init__(self,n,a,s):
        super(AIStudent,self).__init__(n,a)
        self.section_num = s
    def get_age(self): #override
        print("age:"+str(self.age))
ss = AIStudent(input(),input(),input())
ss.get_age()
#----------------------------------------------------#
"""
from itertools import islice


class FibNum:
    def __init__(self):
        self.fn2 = 1
        self.fn1 = 1
    def __next__(self):
        (self.fn1, self.fn2, old_fn2) = (self.fn1 + self.fn2, self.fn1, self.fn2)
        if old_fn2>20:
            raise StopIteration
        return old_fn2
    def __iter__(self):
        return self
f = FibNum()
l = list(islice(f,6,10))
print(l)

