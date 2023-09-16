checklist = list()


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    return checklist[index]


# UPDATE
def update(index, item):
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(index)


# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# MARK ITEM IN CHECKLIST WITH √
def mark_completed(index):
    checklist[index] = '√' + checklist[index]


# GET USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input


# LOWERCASE USER INPUT
def lower_user_input(user_input):
    return user_input.lower()


# VALIDATE INDEX EXISTS IN LIST
def validate_index(index):
    if len(checklist) == 0:
        return True
    elif index >= len(checklist):
        return True
    else:
        return False
    

# MATCH FUNCTION CODE WITH AVAILABLE FUNCTIONS
def select(function_code):
    function_code = lower_user_input(function_code)
    
    # Create item
    if function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)
        return True

    # Read item
    elif function_code == "r":
        item_index = int(user_input("Index number? "))
        
        while validate_index(item_index):
            print("Invalid index! Please try again.")
            item_index = int(user_input("Index number? "))

        print(read(item_index))
        return True

    elif function_code == "u":
        item_index = int(user_input("Index number? "))
        
        while validate_index(item_index):
            print("Invalid index! Please try again.")
            item_index = int(user_input("Index number? "))
            
        updated_item = user_input("Input updated item: ")
        update(item_index, updated_item)
        return True
    
    elif function_code == "d":
        item_index = int(user_input("Index number? "))
        
        while validate_index(item_index):
            print("Invalid index! Please try again.")
            item_index = int(user_input("Index number? "))
            
        destroy(item_index)
        return True
    
    # Print all items
    elif function_code == "p":
        list_all_items()
        return True
        
    elif function_code == "q":
        return False

    # Catch all
    else:
        print("Unknown option")


# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    
    list_all_items()
    
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    
    user_value = user_input("Please Enter a value: ")
    print(user_value)


# RUN TESTS
# test()


running = True
while running:
    selection = user_input("""
Press C to Add to checklist
Press R to Read from checklist
Press U to Update item in checklist
Press D to Delete item in checklist
Press P to display checklist
Press Q to quit

---> """)
    running = select(selection)