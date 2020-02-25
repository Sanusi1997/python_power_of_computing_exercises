def menu_storage():
    phone_dictionary = {"Contacts":
                            {"Ade": "080104576319", "Bayo": "08037017786"},
                        "Messages":
                            ["Hi, Pls call me", "Hey! I missed your call"],
                        "Games":
                            ["Snake Xenzia", "Bubble"],
                        "Settings":
                            ["Phones", "About", "Reset"]
                        }
    return phone_dictionary


def iterator(user_input):
    for key, values in menu_storage().items():
        if user_input == "Settings":
            return ((menu_storage()[user_input]))
        else:
            print(user_input, "-->", (menu_storage()[user_input]))
        break


def display_and_select_menu():
    """ A function that allows user to select from menu """
    phone_menu = {1: "Contacts", 2: "Messages", 3: "Games", 4: "Settings"}
    print("Please input a value to choose options from the menu below: ")
    for keys, values in phone_menu.items():
        print(values)
    user_input = input("Please type the choice of options to display: ")
    if user_input == "":
        print("Run the program again and input a valid value")
        pass
    elif user_input.title() == "Settings":
        list = iterator("Settings")
        for index, values in enumerate(list):
            print((index + 1), "-->", values)
    else:
        iterator(user_input.title())


display_and_select_menu()
