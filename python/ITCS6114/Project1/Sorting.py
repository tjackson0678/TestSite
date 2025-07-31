## Terrence Jackson 
## ITCS 6114 - Summer 2025
## Project 1 Code 
## July 18, 2025 

import time
import matplotlib.pyplot as plt
import numpy as np


# Generate a 1D array of 5 random integers between 1 and 10 (inclusive)
def randIntList(sz): 
    maxSz = sz + 1
    random_integers = np.random.randint(1, 100000, size=sz)
    #print(random_integers)

    return random_integers

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
     
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = 0  # Pointer for the left array
    j = 0  # Pointer for the right array

    # Compare elements from both arrays and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left array
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right array
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def heapInsert(lst):
    h = [0]

    # Loop through all elements in the list
    for value in lst:
        h.append(value)
        i = len(h) - 1

        # Add items the heap in sorted order 
        while i > 1:
            num1 = i//2
            if h[num1] > h[i]: 
                tmp = h[num1]
                h[num1] = h[i]
                h[i] = tmp
                i = i//2
            else: break 
    return h 


def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: an array with 0 or 1 element is already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
def quicksort_mod(arr):
    if len(arr) <= 1:
        return arr  # Mod with median-of-three as pivot
    if len(arr) <=20:
        return insertionSort(arr) # Use Insertion Sort if problem size <=20
    else:
        tmp = insertionSort(arr[1:4]) # Sort the three elements
        pivot =  tmp[2] # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
    

def rev_arr(sz):
    arr = []
    for i in range(sz, 0, -1):
       arr.append(i)
    return arr 


def timeSort(code_strg):
    try:
        # Measure quickSort run time
        start_time = time.time()
        exec(code_strg)
        end_time = time.time()
        rtn_time = end_time - start_time
    except Exception as e:
        print(f"Error executing code: {e}")

    return rtn_time

# Example usage:
input_lst = [1000, 2000, 5000, 10000, 30000, 50000]
input_sz = 5000
my_revlist = rev_arr(input_sz)

# Create random lists 
for num in range(1, 7):
    my_randlist1 = randIntList(input_lst[0])
    my_randlist1 = [int(x) for x in my_randlist1]
    my_randlist2 = randIntList(input_lst[1])
    my_randlist2 = [int(x) for x in my_randlist2]
    my_randlist3 = randIntList(input_lst[2])
    my_randlist3 = [int(x) for x in my_randlist3]
    my_randlist4 = randIntList(input_lst[3])
    my_randlist4 = [int(x) for x in my_randlist4]
    my_randlist5 = randIntList(input_lst[4])
    my_randlist5 = [int(x) for x in my_randlist5]
    my_randlist6 = randIntList(input_lst[5])
    my_randlist6 = [int(x) for x in my_randlist6]
print(" ")

# Create sorted lists
my_sortedlist1 = quicksort(my_randlist1)
my_sortedlist2 = quicksort(my_randlist2)
my_sortedlist3 = quicksort(my_randlist3)
my_sortedlist4 = quicksort(my_randlist4)
my_sortedlist5 = quicksort(my_randlist5)
my_sortedlist6 = quicksort(my_randlist6)

# Create reverse lists
my_revlist1 = rev_arr(len(my_sortedlist1))
my_revlist2 = rev_arr(len(my_sortedlist2))
my_revlist3 = rev_arr(len(my_sortedlist3))
my_revlist4 = rev_arr(len(my_sortedlist4))
my_revlist5 = rev_arr(len(my_sortedlist5))
my_revlist6 = rev_arr(len(my_sortedlist6))

# Measure quickSort run time
q = []
q_s = []
q_r = []
for num in range(1, 7):
    qS_string = f"sorted_list = quicksort(my_randlist{num})"
    qS_string_sorted = f"sorted_list2 = quicksort(my_sortedlist{num})"
    qS_string_reversed = f"sorted_list3 = quicksort(my_revlist{num})"
    qs_time = timeSort(qS_string)
    qs_time_sorted = timeSort(qS_string_sorted)
    qs_time_reversed = timeSort(qS_string_reversed)
    q.append(qs_time*10000)
    q_s.append(qs_time_sorted*10000)
    q_r.append(qs_time_reversed*10000)
print(f"QuickSort Elapsed time: {qs_time:.8f} seconds")

print(" ")

# Measure quickSort_mod run time
q2 = []
q2_s = []
q2_r = []
for num in range(1, 7):
    qS2_string = f"sorted_list = quicksort_mod(my_randlist{num})"
    qS2_string_sorted = f"sorted_list2 = quicksort_mod(my_sortedlist{num})"
    qS2_string_reversed = f"sorted_list3 = quicksort_mod(my_revlist{num})"
    qs2_time = timeSort(qS2_string)
    qs2_time_sorted = timeSort(qS2_string_sorted)
    qs2_time_reversed = timeSort(qS2_string_reversed)
    q2.append(qs2_time*10000)
    q2_s.append(qs2_time_sorted*10000)
    q2_r.append(qs2_time_reversed*10000)
print(f"QuickSort_mod Elapsed time: {qs2_time:.8f} seconds")

print(" ")
# Measure HeapSort run time
h = []
h_s = []
h_r = []
for num in range(1, 7):
    hs_string = f"sorted_list = heapInsert(my_randlist{num})"
    hs_string_sorted = f"sorted_list2 = heapInsert(my_sortedlist{num})"
    hs_string_reversed = f"sorted_list3 = heapInsert(my_revlist{num})"
    hs_time = timeSort(hs_string)
    hs_time_sorted = timeSort(hs_string_sorted)
    hs_time_reversed = timeSort(hs_string_reversed)
    h.append(hs_time*10000)
    h_s.append(hs_time_sorted*10000)
    h_r.append(hs_time_reversed*10000)
print(f"HeapSort Elapsed time: {hs_time:.8f} seconds")

print(" ")
# Measure MergeSort run time
m = []
m_s = []
m_r = []
for num in range(1, 7):
    ms_string = f"sorted_list = merge_sort(my_randlist{num})"
    ms_string_sorted = f"sorted_list2 = merge_sort(my_sortedlist{num})"
    ms_string_reversed = f"sorted_list3 = merge_sort(my_revlist{num})"
    ms_time = timeSort(ms_string)
    ms_time_sorted = timeSort(ms_string_sorted)
    ms_time_reversed = timeSort(ms_string_reversed)
    m.append(ms_time*10000)
    m_s.append(ms_time_sorted*10000)
    m_r.append(ms_time_reversed*10000)
print(f"MergeSort Elapsed time: {ms_time:.8f} seconds")

print(" ")
# Measure sorted array
i = []
i_s = []
i_r = []
for num in range(1, 7):
    is_string = f"sorted_list = insertionSort(my_randlist{num})"
    is_string_sorted = f"sorted_list2 = insertionSort(my_sortedlist{num})"
    is_string_reversed = f"sorted_list3 = insertionSort(my_revlist{num})"
    is_time = timeSort(is_string)
    is_time_sorted = timeSort(is_string_sorted)
    is_time_reversed = timeSort(is_string_reversed)
    i.append(is_time*10000)
    i_s.append(is_time_sorted*10000)
    i_r.append(is_time_reversed*10000)
print(f"InsertionSort Elapsed time: {is_time:.8f} seconds")
print(" ")

x = [1000, 2000, 5000, 10000, 30000, 50000]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.plot(x,q, color='blue', label='Quick Sort')
ax1.plot(x,q2, color='orange', label='Quick Sort Mod')
ax1.plot(x,h, color='red', label='Heap Sort')
ax1.plot(x,m, color='green', label='Merge Sort')
ax1.plot(x,i, color='yellow', label='Insertion Sort')

# Add labels and title
ax1.set_xlabel("Random List Size")
ax1.set_ylabel("Running time (s/10000)")
ax1.set_title("Random List Chart")

ax2.plot(x,q_s, color='blue', label='Quick Sort')
ax2.plot(x,q2_s, color='orange', label='Quick Sort Mod')
ax2.plot(x,h_s, color='red', label='Heap Sort')
ax2.plot(x,m_s, color='green', label='Merge Sort')
ax2.plot(x,i_s, color='yellow', label='Insertion Sort')

# Add labels and title
ax2.set_xlabel("Sorted List Size")
ax2.set_ylabel("Running time (s/10000)")
ax2.set_title("Sorted List Run Chart")

ax3.plot(x,q_r, color='blue', label='Quick Sort')
ax3.plot(x,q2_r, color='orange', label='Quick Sort Mod')
ax3.plot(x,h_r, color='red', label='Heap Sort')
ax3.plot(x,m_r, color='green', label='Merge Sort')
ax3.plot(x,i_r, color='yellow', label='Insertion Sort')

# Add labels and title
ax3.set_xlabel("Reverse Sorted List Size")
ax3.set_ylabel("Running time (s/10000)")
ax3.set_title("Reverse Sorted List Run Chart")

plt.legend()
plt.savefig("Test.pdf")
plt.show()
