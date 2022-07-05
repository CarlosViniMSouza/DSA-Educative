# Hash tables in Python

Hash Tables are a *complex data structure* capable of storing large amounts of information and retrieving specific elements efficiently.

This *data structure uses key/value pairs*, where the key is the name of the desired element and the value is the data stored under that name.

Each input key goes through a **hash function** that converts it from its starting form into an integer value, called a hash. Hash functions must always produce the same **hash** from the same input, must compute quickly, and produce fixed-length values. Python includes a built-in `hash()` function that speeds up implementation.

The table then uses the hash to find the general location of the desired value, called a *storage bucket*. The program then only has to search this subgroup for the desired value rather than the entire *data pool*.

## Applications:

- Used for large, frequently-searched databases

- Retrieval systems that use input keys

## Common hash table interview questions in Python

- *Build a hash table from scratch* (without built-in functions)

- *Word formation* using a hash table

- *Find two numbers that add up to "k"*

- *Implement open addressing* for collision handling

- *Detect if a list is cyclical* using a hash table
