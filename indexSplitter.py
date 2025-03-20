index_list = ["read_input_1", "read_text_1", "read_delete_1"]
converted_list = []
for item in index_list:
    print(item)
    new_item = item[:-1]
    # print(new_item)
    # print(int(item.split("_")[-1]) - 1)
    converted_list.append(new_item + str(int(item.split("_")[-1]) - 1))


# creating a dictionary by zip
dict1 = dict(zip(converted_list, index_list))

for converted_key, old_key in dict1.items():
    print(f"Key is {converted_key} and value is {old_key}")
