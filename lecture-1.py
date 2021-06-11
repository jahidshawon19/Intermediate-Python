############################### COMPREHENSIONS ###############################

## List Comprehension ##

#prog-1 (Find square value from list)

# Traditional Way
item = [1,2,3,4,5,6,7,8,9,10,11]

for i in item:
    if i % 2 == 0:
        print(i**2)

# Using List Comprehension 
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

## Dictionary Comprehension ##

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


## Set Comprehension ##

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
