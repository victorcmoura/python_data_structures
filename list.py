l = [1, 10, 4, 8, 6, 4, 5]

# Search -> O(n)
if 6 in l:
    print("6 is in l")

# Insertion in end -> O(1)
l.append(7)
print(l)

# Access item -> O(1)
print(l[0])

# Remove item -> O(n)
l.remove(10)
print(l)

# Slice -> O(k) where k is the size of the slice
print(l[:3])

# Sort -> O(n log n) with timsort (makes use of merge and insertion sort)
l.sort()
print(l)