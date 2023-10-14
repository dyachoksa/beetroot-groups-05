an_empty_dict = {}

# key: any immutable type
# value: any type
a_dict = {
    1: "Value 1",
    "2": "Value 2",
    2.0: "Value 2.0",
    True: "Boolean True",
    False: "Boolean False",
    None: "The Nothing",
    (1, 0): "A tuple a a key",
    "inner_dict": {
        "a": "A",
        "b": "B",
    },
    "a_list": ["a", "b", "c"]
}

# getting value from dict
print(a_dict[(1, 0)])
print(a_dict["a_list"])
print(a_dict["inner_dict"]["a"])

# get all keys from dict
print(a_dict.keys())
