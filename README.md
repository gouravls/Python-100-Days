# Python-100-Days

Databases vs (List\Tuple\Set\Dict)
Databases store structured data efficiently, but lists and dictionaries allow fast in-memory processing, quick lookups, and handling nested or API data without constant database queries. They’re essential for real-time operations, temporary computations, and flexible data manipulation.



Tuples are useful when data needs to remain unchanged. However, they have limited functionality compared to lists. Some of the key operations available for tuples include:

count() function – Counts the occurrences of a specific value.
index() function – Finds the first occurrence of a value.
Slicing – Extracts a portion of the tuple.
len() function – Returns the total number of elements.

Sets in Python are useful for storing unique values, as they automatically remove duplicates. Unlike lists or tuples, sets are unordered, meaning they do not support indexing, slicing, or the index() function.

Key Set Functions and Their Usage
len(set) → Returns the total number of unique elements in a set.
add(value) → Adds a new element to the set. If the element already exists, the set remains unchanged.
remove(value) → Removes a specified element from the set. If the element is not found, it raises an error.
discard(value) → Removes the specified element from the set, but does not raise an error if the element is missing.
pop() → Removes and returns a random element from the set. Unlike lists, pop() does not take an index as an argument.
copy() → Creates a duplicate of the set, useful for backup purposes.
clear() → Removes all elements from the set, leaving it empty.
union(set_B) → Similar to SQL’s UNION; combines two sets and removes duplicates.
intersection(set_B) → Returns only the common elements found in both sets.
difference(set_B) → Returns elements that exist only in the first set, removing common values.
symmetric_difference(set_B) → Removes common elements and returns only the unique elements from both sets.
