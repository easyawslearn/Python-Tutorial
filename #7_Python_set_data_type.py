# A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
#
# Operators for Sets
# Sets and frozen sets support the following operators:
#
# key in set-example       # containment check
#
# key not in set-example   # non-containment check
#
# set-1 == set-2       # set-1 is equivalent to set-2
#
# set-1 != set-2       # set-1 is not equivalent to set-2
#
# set-1 <= set-2       # set-1is subset of set-2 set-1 < set-2     # set-1 is proper subset of set-2 set-1 >= set-2    # set-1is superset of set-2
#
# set-1 > set-2        # set-1 is proper superset of set-2
#
# set-1 | set-2        # the union of set-1 and set-2
#
# set-1 & set-2        # the intersection of set-1 and set-2
#
# set-1 – set-2        # the set of elements in set-1 but not set-2
#
# set-1 ˆ set-2        # the set of elements in precisely one of set-1 or set-2
#

set1=set('abc')
set2=set('bcd')

output=set1|set2
print ("Output for : ", end="")
print (output)

print("Set1 = ", set1)
print("Set2 = ", set2)
print("\n")

# Union of set1 and set2
set3 = set1 | set2# set1.union(set2)
print("Union of Set1 & Set2: Set3 = ", set3)

# Intersection of set1 and set2
set4 = set1 & set2# set1.intersection(set2)
print("Intersection of Set1 & Set2: Set4 = ", set4)
print("\n")

# Checking relation between set3 and set4
if set3 > set4: # set3.issuperset(set4)
	print("Set3 is superset of Set4")
elif set3 < set4: # set3.issubset(set4)
	print("Set3 is subset of Set4")
else : # set3 == set4
	print("Set3 is same as Set4")

# displaying relation between set4 and set3
if set4 < set3: # set4.issubset(set3)
	print("Set4 is subset of Set3")
	print("\n")

# difference between set3 and set4
set3 = set1 - set2
print("Elements in Set1 and not in Set2: Set3 = ", set3)
print("\n")

# checkv if set4 and set5 are disjoint sets
if set1.isdisjoint(set2):
	print("Set1 and Set2 have nothing in common\n")

# Removing all the values of set5
set1.clear()

print("After applying clear on sets Set5: ")
print("Set1 = ", set1)
