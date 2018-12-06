d = {}

# Dict's worst case seems to be O(n) because of the mathematical
# possibility of the different keys present the same hash value.

# Set item -> O(1) on avg, O(n) on worst case
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)

# Get item -> O(1) on avg, O(n) on worst case
print(d['a'])

# Delete item -> O(1) on avg, O(n) on worst case
d.pop('a')
print(d)

# Search -> O(1) on avg, O(n) on worst case
if 'a' in d:
    print("I have not deleted 'a'")
else:
    print("I have deleted 'a'")

