def save_menu(menu):
    with open("menu.txt", "a") as file:
        for item in menu:
            file.write(item + "\n")
def show_menu():
    try:
        with open("menu.txt", "r") as file:
            menu_items=file.read().splitlines()
            print("Menu:")
            for item in menu_items:
                print("-" + item)
    except FileNotFoundError:
        print("Menu file not found. Please add items to the menu first.")
def delete_position():
    try:
        with open("menu.txt", "r", encoding="utf-8") as file:
            menu_items=file.read().splitlines()
            print("Menu:")
            for i, item in enumerate(menu_items, 1):
                print(f"{i}. {item}")
            try:
                position_to_delete=int(input("Enter the number of the item to delete:"))
                if 1 <= position_to_delete <= len(menu_items):
                    del menu_items[position_to_delete - 1]
                    with open("menu.txt", "w", encoding="utf-8") as file:
                        for item in menu_items:
                            file.write(item + "\n")
                            print("Item deleted successfully.")
                else:
                    print("Invalid position number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    except FileNotFoundError:
        print("Menu file not found. Please add items to the menu first.")
while True:
    try:
        first_ask=int(input("Choose an option:\n1. Look at the menu\n2. Add item to the menu\n3. Delete item from the menu\n4. Exit\n"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    if first_ask==1:
        show_menu()
    elif first_ask==2:
        menu=[]
        ask_to_add=input("Enter a menu item to add: ")
        menu.append(ask_to_add)
        save_menu(menu)
    elif first_ask==3:
        delete_position()
    elif first_ask==4:
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
