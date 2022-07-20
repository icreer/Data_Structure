# Set

## Questions
###	What is the purpose of the data structure?
The definition of of a Set is a unordered collection of data type that is iterable(an object that can be looped over  or iterated over with the help from a for loop), mutable and has no duplicates. The really power fact of a set is that is a methoid that is a highly optimized method for checking whether a object is in a set.

###	What is the performance of the data structure (Big O)?
So the biggest thing is to compare set vs a list. So a list a mutable sequence, typically used to store collections of homogeneous items. As for a set object is an unordered collection of distinct hashable object. So List are a little bit faster than sets when you just want to iterate over the values. As for sets are significantly faster than lists if you want ot check if an item is in the set. 

### What kind of problems can be solved using the data structure?
The kind of problems that can be solved with Sets are once that you can set up a set and check if something is in it. Do to the fact that there only can be no duplicates in a set and there is no order you can see that to quick check if that object exsiet. So like checking if a username is free to use or any thing were something must be unique.

###	How would the data structure be used in Python?
Here are the function you use for python sets:
* add() -- Add element to a set
* remove() -- Remove an element from a set
* clear() -- Clears all elements from a set
* copy() -- copy the set
* pop() -- Remove and return an arbitrary set element
* update() -- Updates a set with the union of itself and others
* union() -- Returns the union of sets in a new set
* difference() -- Returns the difference of two or more sets as a new set
* intersection() -- Returns the intersection of two sets as a new set
* isdisjoint() -- Returns True if two sets have a null intersection
* issubset() -- Returns True if another set contains this set
* issuperset() -- Returns True if this set contains another set


###	What kind of errors are common when using the data structure?
When using the remove()  function if a element is not present in the set raise a Key Error.
When using the pop() function Raise a KeyError if the set is empty

###	Does converting objects to a set keep the order that they are in?
No, converting a objects to a set it doesnot keep the order that they are in. Keep in mid that sets can not have any duplicates and sets are unorder in there nature.
###	What is the difference between subset, superset, and sets?
So we have a base set of A with is all the programming laugages that I have used. As we have a set B witch is all the programming laugages ever made. So A is a SUBSET of B. From the other end B is a SUPERSET of A. 
###	What is the difference between a subset and a proper subset?
A proper subset of a set is a subset of a set that is not equal to the set.
As a subset can be a set that is equal to the main set.
Example:
```python
# Main Set
A = set([1,2,3,4,5,6])
# Proper Subset
B = set([1,2,3,4])
# Subset but is not a proper subset
C = set([1,2,3,4,5,6])
```
###	What makes a set different between list?
List
* The List is an indexed sequence 
* List allows duplicated elements
* Elements by their position can be accessed
* Multiple null elements can be stored
* List implementations are ArrayList, LinkedList, Vector, or Stack, Queue
Set
* The Set is an non-indexed sequence
* Set doesn't allow duplicate elements
* Position access to elements is not allowed
* Null element can store only once
* Set implementations are HashSet, LinkedHashSet

###	Can you access a set by indexing?
Do to the fact that sets are unordered there for there is no index. So in python loop though it using a for loop or us the in keyword

## Skills

###	Check if a set is a subset or a superset
```python
s1 = set([2,6,87,9,5,78])
s2 = set([90,80,45,65,89])
s3 = set([90,80])
s4 = set([5,6])

z = s1.issubset(s2)
e = s1.issubset(s4)
y = s2.issubset(s3)
g = s3.issubset(s2)
m = s4.issubset(s1)

print(z)
print(e)
print(y)
print(g)
print(m)
```
###	Know how to check if a value is in a set
```python
sets = set()
sets.add(9)
sets.add(10)
sets.add(94)
sets.add(91)
if 14 in sets:
    print(false)
elif 9 in sets:
    print(true)

```
###	Know how to find the intersection of 2 sets
```python
s1 = set([1,2,3,4,5,6,7,8])
s2 = set([7,8,9,10,11,12,23]) 

i = s1.intersection(s2)

print(i)
```

## Problems
### Eample Problem
Lets see the code to find the differnect between two sets with out using the difference() function
```python
def difference(s1,s2):
    save = set()
    for i in s1:
        if i not in s2:
            save.add(i)
    return(save)

s1 = set([1,2,3,4])
s2 = set([2,4])
print(difference(s1,s2))


```
### Student Problem 
You need need to remove the intersection between two sets with out using the python .difference_update()
```python
def difference_update(s1,s2):
    # Your Code Here
    pass

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(difference_update(s1,s2))
# {1,2,3}

```
[Solution](Set_Student_Solution.py) 