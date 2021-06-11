"""
Author: Jahid Hasan Shawon
Email: jahidshawon1730@gmail.com

"""
############################### COMPREHENSIONS ###############################

# List Comprehension ##

#prog-1 (Find square value from list)

#Traditional Way
item = [1,2,3,4,5,6,7,8,9,10,11]

for i in item:
    if i % 2 == 0:
        print(i**2)

#gitgitUsing List Comprehension 
my_list = [i**2 for i in range(1,10) if i %2 == 0]
print(my_list)

#prog-2(i want 'n' for each 'n' in nums)

#Traditional Way 
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

#Using List Comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [n for n in nums]
print(my_list)

#prog-3(I wnat 'n' for each 'n' in nums if 'n' is even)

#Traditional Way 
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

#Using List Comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

#prog-4(I want a (letter,num) pair for each letter in 'abcd'  and each number in '0123')
#Traditional Way 
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))

print(my_list)
#Using List Comprehension
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehension ##

#prog-1( I want a dict{'language': 'framework'} for each language,framework in zip(language,framework) if language is not equal 'PHP' )
#Traditional Way 
language = ['Python', 'Dart', 'Ruby', 'Javascript', 'Java']
framework = ['Django', 'Flutter','Rails', 'Node JS', 'JSP']
my_dict = {}
for lang, frame in  zip(language,framework):
    if lang != 'PHP':
        my_dict[lang] = frame
print(my_dict)
#Using List Comprehension
language = ['Python', 'Dart', 'Ruby', 'Javascript', 'PHP', 'Java']
framework = ['Django', 'Flutter','Rails', 'Node JS', 'Laravel', 'JSP']

my_dict = {lang:frame for lang,frame in zip(language,framework) if lang != 'PHP'}
print(my_dict)


# Set Comprehension ##

#prog-1
#Traditional Way 
nums = [1,1,1,12,5,6,6,6,7,5,5,2,1,6,7,2,9,10,1,0,1,6,8,8]
my_set = set() # create new set 
for n in nums:
    my_set.add(n)
print(my_set) # set contains unique value
#Using List Comprehension
nums = [1,1,1,12,5,6,6,6,7,5,5,2,1,6,7,2,9,10,1,0,1,6,8,8]
my_set  = {n for n in nums}
print (my_set)


############################ Lambda + Map + Filter ########################################
#Lambda also called as annonymous function#

#lambda function 


#prog-1:(sum of two values)
sum = lambda a,b:a+b
print(sum(10,20))

#prog-2(find square of any integer)
square = lambda a:a**2
print(square(10))

#prog-3(even or odd)

even_func = lambda num: num % 2 == 0 
print(even_func(10))

#prog-3(lambda in general function)
def func1(x):
    func2 = lambda x: x+5
    return func2(x) + 90

print(func1(5))

# Map Function

# map takes two arguments. one is normal function another one is a iterator object.# 

#prog-1
my_list = [2,3,4,5,6,7]

def square(x):
    return x * x

new_list = map(square, my_list)
print(new_list) # create map object 
print(list(new_list)) # apply  list type cast

#prog-2(implement lambda on map)
a = [1,2,3,4,5,6,7,8,9,10]

new_list = (map (lambda x: x+5, a))
print (list(new_list))


# Filter Function

#prog-1
num = [1,2,3,4,5,6,7,8,9,10]

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

new_list = filter(is_even, num) #only take True value from function 'is_even()'
print(list(new_list))




############################ *args and **kwargs(Variable Length Argument) ################################
# *args create a Tuple that hold the values. it is also called non-keywarded variable length.

#prog-1

def my_func(*args):
    print("Hello World", args)

my_func("abc", 1234, True)

#prog-2
def add(*args):
    temp = 0
    for n in args:
        temp = temp + n 
    
    return temp 

result = add(1,2,3,5,6,7,8,9,10)
print(result)



# **kwargs create a Dictionary that hold the values. it is also called keywarded variable length.

#prog-1
def my_func(**kwargs):
    print("Hello World", kwargs)

print(my_func(name="Jahid", id=1251))


#prog-2
def add(**kwargs):
    temp = 0
    for key in kwargs:
        temp = temp + kwargs[key]
    return temp 

result = add(a=10, b=15, c=20)
print(result)




####################################### Collections ########################################

#Counter

#prog-1

from collections import Counter 

a = "uuuuoooasdasdrsadjdsa"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items()) # wrapper with parenthesis
print(my_counter.keys()) # only show keys 
print(my_counter.values()) # only show values

print(list(my_counter.elements())) # get as a list


#deque

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(4)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([7,8,9])
print(d)
d.extendleft([10,11,12])
print(d)

