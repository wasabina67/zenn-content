import copy


dict_1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": ["value3", "value4", "value5"],
    "key4": {"sub_key": "sub_value"},
}

dict_2 = {
    "key1": "value1",
    "key2": "value2",
    "key3": ["value3", "value4", "value5"],
    "key4": {"sub_key": "sub_value"},
}

copy_dict = dict_1
dict_1["key3"].append("value6")

print("- dict_1")
print(dict_1)
print(copy_dict)
print("---")

deepcopy_dict = copy.deepcopy(dict_2)
dict_2["key3"].append("value6")

print("- dict_2")
print(dict_2)
print(deepcopy_dict)
print("---")
