# Sequence types: list, tuple, set

# a mutable (changable) sequence: list
a_list = [10, 12, 15]
a_str_list = ["abc", "cde"]

a_list.append(100)
print(a_list)

# an immutable sequence: tuple
a_tuple = (10,)
a_tuple_2 = ("a", "b", "c",)

print(a_tuple_2)

# a mutable sequence of unique elements: set
a_set = {10, 12, 100, 12, 100}
# but 
a_empty_set = set()

print(a_set)
