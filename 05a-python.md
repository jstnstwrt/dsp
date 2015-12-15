# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are both collection, or array, data types. However, lists are mutable and tuples are immutable objects. This simply means that the collection of values referred to by the list can be mutated or changed after the list has been created. For example, you can append elements to the end of a list or delete elements from a list. These operations do not work on tuples because they cannot be mutated after it has been created. Mutability is precisely the reason that you can use tuples as the keys in a dictionary but you can't use lists.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both data types that store collections of values in python. A list is an *ordered* collection, whereas sets are an *unordered* collection. This means that one should use a list (as opposed to a set) when the particular sequence (or indexing) of elements is important. On the other hand, sets guarantee that every element in the collection is unique while lists may contain as many repeated values as you like. Sets also cannot contain any mutuable elements, although lists can. 

>> Some examples of both:

>>```
s1 = {'c','a','t'}
```
>>```
s2 = set(['cat'])
```
>>```
'c' in s1
```
>>```
for i in ['c','a','t']:
	print i
```

 >> Finding out if an element is contained in a collection is vastly faster when checking a set compared to checking a list. This is because sets are implemented using a hash table and lists simply use an index. This means that when you check membership in a list, you have to actually iterate through the entire list every time checking against every element. On the other hand, when checking in a set, the hash of the value tells you which bucket of elements to check (which is a much smaller collection of objects). This performance benefit increases as the size of the list/set gets large. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is an anonymous function that can be defined at runtime. They constrained to be only one single expression and can reference functions for the containing scope. 

>> It is very helpful, and often more concise, when a small function is needed on the fly. Also, it is useful when you want to define a function as the output of another function or use a function as the input of another function. 

>> I used a lambda function in my solution to the front_back fucntion in q6_strings.py:

>>```
def front_back(a, b):
	g = lambda s: (len(s) + 1)/2
    return a[:g(a)] + b[:g(b)] + a[g(a):] + b[g(b):]
```
>> Here is another example using sorted:
>>```
sorted([(1,2),(7,3),(5,1)],key=lambda x: x[1])
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a succint way to construct lists. It does so 

>>```
[x%2 for x in range(6)] # yields [0, 1, 0, 1, 0, 1]
```

>> The map function creates a list by applying a specified function to every element of an iterable. So I can construct the same list as above using map as follows:

>>```
map(lambda x: x%2, range(6)) # yields [0, 1, 0, 1, 0, 1]
```

>> The filter function is very similar to map and applies a specified function to every element of an iterable, but returns the list of elements for which the function returned True. 

>>```
filter(lambda x: x%2, range(6)) # yields [1, 3, 5]
```

>> Equivalent lists (to the output of the filter function) can always also be created using list comprehensions and including the corresponding if clause. For example, the equivalent list is found using a list comp:

>>```
[x for x in range(6) if x%2 > 0] # yields [1, 3, 5]
```

>> It is generally regarded that using list comprehensions is the more 'pythonic' way to consicely create lists, however there are certain situations where map and filter aare useful (e.g., when you want to introduce an additional scope within a function). 

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





