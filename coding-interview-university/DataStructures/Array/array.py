# Implement a vector (mutable array with automatic resizing):
#     Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
#     New raw data array with allocated memory
#         can allocate int array under the hood, just not use its features
#         start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
#     size() - number of items
#     is_empty()
#     at(index) - returns item at given index, blows up if index out of bounds
#     push(item)
#     insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
#     prepend(item) - can use insert above at index 0
#     pop() - remove from end, return value
#     delete(index) - delete item at index, shifting all trailing elements left
#     remove(item) - looks for value and removes index holding it (even if in multiple places)
#     find(item) - looks for value and returns first index with that value, -1 if not found
#     resize(new_capacity) // private function
#         when you reach capacity, resize to double the size
#         when popping an item, if size is 1/4 of capacity, resize to half
def size(arr):
    return len(arr)

def is_empty(arr):
    return len(arr) == 0

def at(arr, index):
    return arr[index]

def push(arr, value):
    arr.append(value)

def insert(arr, index, val):
    arr.insert(index, val)

def prepend(arr, value):
    insert(arr, 0, value)

def pop(arr):
    arr.remove(len(arr) - 1)
    return arr[len(arr) - 1]

def delete(arr, index):
    arr.remove(arr[index])

def remove(arr, value):
    for i in arr:
        if i == value:
            arr.remove(i)

def find(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return i
    return -1    

arr = [1,2,3,2,5]

# insert(arr, 1, 5)
# prepend(arr, 4)
# delete(arr, 1)
# remove(arr, 2)
print(find(arr, 3))