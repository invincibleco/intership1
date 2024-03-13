# Q1} Write a python program to flatten tuple of list to tuple

org_tuple=((1,2,3),[4,5],[6],(7,8))
new_tuple=[]
for i in org_tuple:
    for j in i:
        new_tuple.append(j)
print(tuple(new_tuple))

# Q2} Python program to convert Set into Tuple and Tuple into Set

my_tuple=(1,2,3,4,5,6)
my_set=set(my_tuple)
print(my_set)

new_set=set((1,2,6,7,8))
new_tuple=tuple(new_set)
print(new_tuple)

# #Q3}Convert List of Dictionary to Tuple list Python

this_list=[{'a':1, 'b':2},{'a':3, 'b':4}]
this_tuple=tuple(this_list)
print(this_tuple)
 
# Q4}Python Sort tuple list by Nth element of tuple

def sorter(tople, n):

  return sorted(tople, key=lambda x: x[n])

# Example usage
example_tuple = [(3, 1, 4), (1, 5, 2), (2, 4, 3)]
sorted_list = sorter(example_tuple, 2)  # ex. Sort by the second element (index 2)

print(sorted_list)


# Q5}Python Program to find tuple indices from other tuple list

def finderrr(local, finder):

  empty = []
  for indexes, values in enumerate(local):
    for searcher in finder:
      if values == searcher :
        empty.append([indexes])
        break  # Stop searching for the same match in the current main_tuple
  return empty


local = [(1, 2, 3), (5, 6), (1, 2), (7, 8, 9)]
finder = [(1, 2, 3), (5, 6)]

indices = finderrr(local, finder)
print(indices)


# Q6}Convert Dictionary Value list to Dictionary List Python

new_dict={1:["Apple","Mango"],2:["Ball","Bat"]}
new_list=list(new_dict.values())
print(new_list)




