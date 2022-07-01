# Arrays (Lists) in Python

Python does not have a built-in array type, but you can use lists for all the same tasks.
An array is a collection of values of the same type saved under the same name.

An example about cars:

```py
cars = ["Fiat", "Volkswagen", "Toyota", "Renault", "GM", "Ford"]

print("The length of list 'cars': ", len(cars))
# output: The length of list 'cars':  6

cars.append("Honda")  # add element in the end-list

cars.pop(0)  # removing first element

for i in cars:
    print("Car Model:", i)
    
"""
output:

Car Model: Volkswagen
Car Model: Toyota
Car Model: Renault
Car Model: GM
Car Model: Ford
Car Model: Honda
"""
```

## Common Operations:

1 - Remove even integers from list;
2 - Merge two sorted lists;
3 - Find minimum value in a list;
4 - Maximum sum sublist;
5 - Print products of all elements;

*let's go explorer this operations*
