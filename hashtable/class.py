#
# resize

# step1: make a new bigger table/array
# stpe2: go through all the old elements, and hash into the new list
    # :going through all the elements is O(n)
    # :Double the size of the table every resize


# When you put()
#     if load > 0.7:
#         double capacioty

# when you del()
#     if load < .2:
#         havle the capacioty/down to some minimum


# import math

# cache = {}

# def inv_sqr_root(n):
#     if n not in cache:
#         cache[n] = 1/math.sqrt(n)

#     return cache[n]

# for i in range(1,6):
#     print(inv_sqr_root(i))


d = {
    'foo':12,
    'bar':17,
    'qux': 3
}

# # sort by key

# items = list(d.items())

# print(items)

# items.sort()

# print(items)

# sort by value

items = list(d.items())

print(items)

items.sort(key=lambda e: e[1])

print(items)
