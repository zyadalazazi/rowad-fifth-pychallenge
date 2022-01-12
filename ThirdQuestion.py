# Initializaing the main list
names_list = []


# A function to display the elements of the list
def view_list():
    print("\nThe list:")
    for name in names_list:
        print(name)


# A function to add a name to the list
def add_name():
    name = input("Please enter the name you want to add:")
    while not name.isalpha():
        name = input("Please enter the name you want to add with no numbers or symbols:")

    names_list.append(name)
    print("{0} has been added to the list".format(name))
    view_list()


# A function to change a name in the list
def change_name():
    name_del = input("Enter the name you want to change:")
    name_add = input("Enter the new name:")

    fl = False
    while not fl:
        if not name_del.isalpha and not name_add.isalpha():
            print("Please enter names with no numbers or symbols:")
        else:
            fl = True

    if name_del not in names_list:
        print("The name you want to change is not in the list.")
    else:
        ind = names_list.index(name_del)
        names_list[ind] = name_add
        print("{0} has been replaced with {1} in the list".format(name_del, name_add))

    view_list()


# A function to remove a name from the list
def remove_name():
    name = input("Please enter the name you want to remove:")
    while not name.isalpha():
        name = input("Please enter the name you want to add with no numbers or symbols:")

    if name not in names_list:
        print("The name is not in the list")
    else:
        names_list.remove(name)
        print("{0} has been removed from the list".format(name))

    view_list()


# A function to exit the system
def exit_system():
    print("Thank you for using our System :)")
    exit()


# A function to display the options of the system to the user
def view_options():
    print("\nChoose the number of the operations you want to do:\n"
          "0 - Exit the System\n1 - Add a name\n2 - Change a name\n3 - Remove a name\n4 - View the list")


# The main program
print("Welcome to our System".center(125, "-"))
view_options()
op_num = input("Please enter the operation you want to complete:")

while op_num != '0':
    if op_num == '1':
        add_name()
    elif op_num == '2':
        change_name()
    elif op_num == '3':
        remove_name()
    elif op_num == '4':
        view_list()
    else:
        print("Please enter a valid operation number")

    view_options()
    op_num = input("Please enter the operation you want to complete:")

exit_system()




