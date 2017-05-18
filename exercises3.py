"""
1. Write a Python program to create an Enum object and display a member name and value.
Sample data :
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
Expected Output :
Member name: Albania
Member value: 355
"""
enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra =376
    Angola = 244
    Antartica = 672

def print_afghanistan():
  print("Country name:",Country.Afghanistan.name,"\nCountry code:",Country.Afghanistan.value)

"""
2. Write a Python program to iterate over an enum class and display individual member and their value.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
"""

def print_all():
  for country in Country:
      print("Country name:",country.name,"\nCountry code:",country.value)

"""
3. Write a Python program to display all the member name of an enum class ordered by their values.
Expected Output:
Country Name ordered by Country Code:
Afghanistan
Algeria
Angola
Albania
Andorra
Antarctica
"""
def ordered_value():
    order = []
    for country in Country:
        order.append((country.name,country.value))
    order.sort(key=lambda x: x[1])
    for i in order:
        print(i[0])

"""
4. Write a Python program to get all values from an enum class.
Expected output:
[93, 355, 213, 376, 244, 672]
"""
def print_values():
    ret = []
    for country in Country:
        ret.append(country.value)
    print(ret)
"""
5. Write a Python program to count the most common words in a dictionary. 
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
"""
dictionary = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]

def common_words():
    words = []
    count = []
    ret = []
    for i in dictionary:
        if i in words:
            count[words.index(i)] += 1
        else:
            words.append(i)
            count.append(1)
    for i in range(len(words)):
        ret.append((words[i],count[i]))
    ret.sort(key=lambda x: x[1],reverse=True)
    print(ret[:4])

#from collections import Counter
#word_counts = Counter(dictionary)
#top_four = word_counts.most_common(4)
#print(top_four)

"""
6. Write a Python program to find the class wise roll number from a tuple-of-tuples. 
Expected Output:
defaultdict(, {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]}) 
"""

from collections import defaultdict
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

def class_wise_roll_number():
    class_roll_number = defaultdict(list)
    for name,number in classes:
        class_roll_number[name].append(number)
    print(class_roll_number)

"""
7. Write a Python program to count the number of students of individual class. 
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
Expected Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})
"""
from collections import Counter
def count_classes():
    return Counter(t[0] for t in classes).items()
"""
8.Write a Python program to get the unique enumeration values. 
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""
def enum_values():
    for country in Country:
        print(country.name,"=",country.value)
"""
9. Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order. 
Expected Output: 
Angola 244
Andorra 376
Algeria 213
Afghanistan 93
Albania 355
In reverse order:
Albania 355
Afghanistan 93
Algeria 213
Andorra 376
Angola 244
"""
from collections import OrderedDict
def ordered_dict():
    dictionary = {}
    for country in Country:
        dictionary.update({country.name:country.value})
    odict = OrderedDict(dictionary)
    for key in odict:
        print(key, odict[key])
    print("Reverse")
    for key in reversed(odict):
        print(key, odict[key])
"""
10. Write a Python program to compare two unordered lists (not sets).
Expected Output: False
"""
def compare_lists(a,b):
    a_stack = []
    for i in a:
        a_stack.append(i)
    for j in b:
        try:
            a_stack.remove(j)
        except ValueError:
            return False
    return len(a_stack) == 0

  #from collections import Counter
#def compare_lists(x, y):
#    return Counter(x) == Counter(y)
#n1 = [20, 10, 30, 10, 20, 30]
#n2 = [30, 20, 10, 30, 20, 50]
#print(compare_lists(n1, n2))

"""
11. Write a Python program to create an array contains six integers. Also print all the members of the array.
Expected Output:
10
20
30
40
50
"""
arr = [10,20,30,40,50,60]
def print_arr():
    for i in arr:
        print(i)
"""
13. Write a Python program to get the array size of types unsigned integer and float. Go to the editor
Expected Output:
4 
4
Click me to see the sample solution
"""
"""
14. Write a Python program to get an array buffer information. Go to the editor
Expected Output:
Array buffer start address in memory and number of elements.
(25855056, 2)
Click me to see the sample solution
"""
"""
15. Write a Python program to get the length of an array. Go to the editor
Expected Output:
Length of the array is: 
5
Click me to see the sample solution
"""
"""
16. Write a Python program to convert an array to an ordinary list with the same items. Go to the editor
Expected Output:
Original array:
array('b', [1, 2, 3, 4])
Array to list:
[1, 2, 3, 4] 
Click me to see the sample solution
"""
"""
17. Write a Python program to convert an array to an array of machine values and return the bytes representation. Go to the editor
Expected Output:
Original array: 
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000' 
Click me to see the sample solution
"""
"""
18. Write a Python program to read a string and interpreting the string as an array of machine values. Go to the editor
Expected Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000' 
array2: array('i', [7, 8, 9, 10])
Click me to see the sample solution
"""
"""
19. Write a Python program to push three items into the heap and print the items from the heap. Go to the editor
Expected Output:
('V', 1)
('V', 2)
('V', 3)
Click me to see the sample solution
"""
"""
20. Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap. Go to the editor
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2) 
---------------------- 
The smallest item in the heap:
('V', 1) 
----------------------
Pop the smallest item in the heap:
('V', 2) 
('V', 3) 
Click me to see the sample solution
"""
"""
21. Write a Python program to push an item on the heap, then pop and return the smallest item from the heap. Go to the editor
Expected Output:
Items in the heap:
('V', 1) 
('V', 3) 
('V', 2) 
----------------------
Using heappushpop push item on the heap and return the smallest item.
('V', 2) 
('V', 3) 
('V', 6)
Click me to see the sample solution
"""
"""
22. Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time. Go to the editor
Expected Output:
[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
Click me to see the sample solution
"""
"""
23. Write a Python program to get the two largest and three smallest items from a dataset. Go to the editor
Expected Output:
[100, 90]
[10, 20, 20]
Click me to see the sample solution
"""
"""
24. Write a Python program to locate the left insertion point for a specified value in sorted order. Go to the editor
Expected Output:
4 
2
Click me to see the sample solution
"""
"""
25. Write a Python program to locate the right insertion point for a specified value in sorted order. Go to the editor
Expected Output:
3 
2
Click me to see the sample solution
"""
"""
26. Write a Python program to insert items into a list in sorted order. Go to the editor
Expected Output:
Original List: 
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36] 
Sorted List: 
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
Click me to see the sample solution
"""
"""
27. a Python program to create a queue and display all the members and size of the queue. Go to the editor
Expected Output:
Members of the queue:
0 1 2 3 
Size of the queue:
4 
Click me to see the sample solution
"""
"""
28. Write a Python program to find whether a queue is empty or not. Go to the editor
Expected Output:
True 
False 
Click me to see the sample solution
"""
"""
29. Write a Python program to create a FIFO queue. Go to the editor
Expected Output:
0 1 2 3 
Click me to see the sample solution
"""
"""
30. Write a Python program to create a LIFO queue. Go to the editor
Expected Output:
3 2 1 0
Click me to see the sample solution
"""
