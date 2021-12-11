# Learning & useful snippets

## Data ingestion

### String to list

Some data has no separators, example ```'1598876345'``` or ```'aleorghauoer'```.
Inorder to parse into list a convienent function can be employed

```
    def convert_string_to_list(string):
        list1 = []
        list1[:0] = string
        return list1
```

This would return as ```['1', '5', '9', '8', '8', '7', '6', '3', '4', '5']```
which can be processed further either as a list or np array

## Iteration

### Multiple iterations at each step

Single iterations operate on row or column indices. Iterating diagonally needs both row and column step on each iteration. This can be achieved via the ```zip``` method (builtin)

```
    for i,j in zip(range(5),range(25,100)):
        print(i,j)
```

## Lists

### List comprehension

Efficent way to iterate thru a list and return either the element or ```f(element)``` into another list. In this example, the list has elements of varying length. Each element length is calculated and returned as a list in order of ```input_list```.

```
    element_lengths = [len(x) for x in input_key] # [4,1,5,10]
```

### Difference between lists

Checking the difference in unique elements in a list can be accomplished using ```set``` (builtin). The difference is returned back as a set that can be converted to a list using ```sorted``` (builtin)

```
    list = ['a', 'b', 'c', 'd', 'w'] 
    list2 = ['f', 'y', 'a', 'w', 'd']
    # returns a set of difference
    set(list) - set(list2) # {'b', 'c'}
    set(list2) - set(list) # {'y', 'f'}
    # returns a list of difference
    sorted(set(list) - set(list2)) # ['b', 'c']
```

## Numpy

### Read in string csv into np.array and convert values to integer type

Here is an example, where ln is the line being read via fileopen.readline()

```
    new_array = np.append(new_array, np.fromstring(ln, sep=",", dtype=int))
```

### Location of elements in np array

Numpy were to find the locations of an item in array.
Good reference : https://note.nkmk.me/en/python-numpy-where/

```
    locations = np.where(mynparray >= 10)
```

This returns a weird list of arrays of i and j locations separately. These can be convinently joined together as a list of tuples using ```zip`` (builtin : iterate in parallel)

```
    location_array = sorted(list(zip(locations[0], locations[1])))
    # or
    location_array = sorted(list(zip(*locations)))
```

### Convert list of string to np.array of type int and reshape to size of choice

If np array has string values, they can be cast to other types via ```astype()``` method. Here reshape places the array into a shape of choice.

```
    input_array = input_array.astype(int).reshape(lnheight, lnwidth)
```

### Histogram of consituent elements

There is probably a better way to specify the bins here, but the outcome is a list with count in the position elements of bins

```
    hist_elements = np.histogram(input_array, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

## Pandas

### Apply usage in pandas

Given a dataframe, function can be applied to all elements, using the ```df.apply``` method (pandas)

```
    df_numeric = df.apply(pd.to_numeric)
```

## Deques

### Deques ingesting a list

Deques (from collections) can ingest a list a la:
```
    location_array = collections.deque(location_array)
```

### Pop and append left (stack LIFO)

Deques can be used for stack implementation (LIFO)
```
    location_array.appendleft(new_addition)
    newest_item = location_array.popleft()
```