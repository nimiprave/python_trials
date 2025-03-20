# test for the length and type of the input string less than 30 characters


def compressor(selected_entity_name, ui_type, suffix):

    function_name = f"{selected_entity_name}_{ui_type}_{suffix}"
    print(f"Length of the function name: {len(function_name)}")
    length = len(function_name)
    if length > 30:
        # compression logic
        print(f"length of Entity Type: {len(selected_entity_name)}")
        print(f"Entity Type: {selected_entity_name}")

        # identify if the underscore is present if so remove it
        selected_list = selected_entity_name.split("_")
        print(selected_list)
        sel_list = selected_entity_name.split("_")[1:]
        print(sel_list)

    else:
        print(function_name)


if __name__ == "__main__":
    entity_name = input("Enter the entity name: ")
    ui_type = input("Enter the ui type: ")
    suffix = input("Enter the suffix: ")
    compressor(entity_name, ui_type, suffix)
