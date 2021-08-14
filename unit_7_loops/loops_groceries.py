def print_items(my_list):
    print(my_list)


def print_item_amount(my_list):
    print(len(my_list))


def is_item_in_list(my_list):
    item = input("Enter item name to check if in list: ")
    print(item in my_list)


def times_item_in_list(my_list):
    item = input("Enter item name to count amount in list: ")
    print(my_list.count(item))


def remove_item_from_list(my_list):
    item = input("Enter item name to remove form list: ")
    my_list.remove(item)
    print(my_list)


def add_item_to_list(my_list):
    item = input("Enter item name to add to list: ")
    my_list.append(item)
    print(my_list)


def print_illegal_items(my_list):
    illegal_list = list()
    for item in my_list:
        if len(item) < 3 or not item.isalpha():
            illegal_list.append(item)
    print("Illegal items:", illegal_list)


def remove_duplicate_items(my_list):
    # my_list = list(dict.fromkeys(my_list))
    for item in my_list:
        while my_list.count(item) > 1:
            my_list.remove(item)
    print("Items after removing duplicates:", my_list)


menu = """
1. הדפסת רשימת המוצרים
2. הדפסת מספר המוצרים ברשימה
3. הדפסת התשובה לבדיקה "האם המוצר נמצא ברשימה?" (המשתמש יתבקש להקיש שם מוצר)
4. הדפסת התשובה לבדיקה "כמה פעמים מופיע מוצר מסוים?" (המשתמש יתבקש להקיש שם מוצר)
5. מחיקת מוצר מהרשימה (המשתמש יתבקש להקיש שם מוצר, רק מוצר אחד ימחק)
6. הוספת מוצר לרשימה (המשתמש יתבקש להקיש שם מוצר)
7. הדפסת כל המוצרים שאינם חוקיים (מוצר אינו חוקי אם אורכו קטן מ-3 או שהוא כולל תווים שאינם אותיות)
8. הסרת כל הכפילויות הקיימות ברשימה
9. יציאה
"""

actions = [print_items, print_item_amount, is_item_in_list, times_item_in_list,
           remove_item_from_list, add_item_to_list, print_illegal_items, remove_duplicate_items]

groceries = input("Enter grocery string: ")
grocery_list = groceries.split(',')
print(menu)

while True:
    choice = input("Choose 1-9: ")
    if not choice.isdigit():
        print("Not a number")
        continue
    choice = int(choice)
    if not 1 <= choice <= 9:
        print("Not in menu")
        continue
    if choice == 9:
        print("Thanks, come again soon!")
        break
    actions[choice - 1](grocery_list)
