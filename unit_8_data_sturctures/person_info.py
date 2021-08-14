import calendar
from datetime import date

valid_types = (str, tuple)


def calc_age(day, month, year):
    today = date.today()
    return today.year - year - ((today.month, today.day) < (month, day))


def print_person_info(person):
    for item in person.items():
        print("{}".format(item))


def print_last_name(person):
    print(person['last_name'])


def print_birth_month(person):
    birth_date = person['birth_date']

    if type(birth_date) not in valid_types:
        print("Unrecognized type")
        return

    if type(birth_date) == str:
        birth_date = birth_date.split('.')

    month_name = calendar.month_name[int(birth_date[1])]
    print("{}'s birth month: {}".format(person['first_name'], month_name))


def print_num_of_hobbies(person):
    print('{} has {} hobbies'.format(person['first_name'], len(person['hobbies'])))


def print_last_hobby(person):
    print("{}'s most recent hobby: {}".format(person['first_name'], person['hobbies'][-1]))


def add_cooking_to_hobbies(person):
    hobbies = person['hobbies']
    hobby = 'Cooking'
    if hobby in hobbies:
        print("{} already has '{}' under 'hobbies'!".format(person['first_name'], hobby))
    else:
        person['hobbies'].append('Cooking')
        print("Added '{}' to hobbies!".format(hobby))
        print('Updated list of hobbies: {}'.format(person['hobbies']))


def convert_birth_date_to_tuple(person):
    birth_date = person['birth_date']
    if type(birth_date) == str:
        birth_date = birth_date.split('.')
        person['birth_date'] = (int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
        print('Converted birth date to tuple: {}'.format(person['birth_date']))
    elif type(birth_date) == tuple:
        print('Already a tuple!')
    else:
        print("Unrecognized type")


def add_age(person):
    birth_date = person['birth_date']

    if type(birth_date) not in valid_types:
        print("Unrecognized type")
        return

    if type(birth_date) == str:
        birth_date = birth_date.split('.')

    if 'age' in person.keys():
        print("Updating 'age'...")
    else:
        print("Adding 'age'...")

    person['age'] = calc_age(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
    print("Updated person:")
    print_person_info(person)


actions = [print_last_name, print_birth_month, print_num_of_hobbies, print_last_hobby,
           add_cooking_to_hobbies, convert_birth_date_to_tuple, add_age, print_person_info]

menu = """
1. הדפיסו למסך את שם המשפחה של מריה.
2. הדפיסו למסך את החודש בו נולדה מריה.
3. הדפיסו למסך את מספר התחביבים שיש למריה.
4. הדפיסו למסך את התחביב האחרון ברשימת התחביבים של מריה.
5. הוסיפו את התחביב "Cooking" לסוף רשימת התחביבים.
6. הפכו את טיפוס תאריך הלידה לטאפל שכולל 3 מספרים (יום, חודש ושנה - משמאל לימין) והדפיסו אותו.
7. הוסיפו מפתח חדש בשם age אשר כולל את גילה של מריה והציגו אותו.
8. הדפס את כל המידע על מריה.
9. יציאה.
"""

person_info = {'first_name': 'Mariah',
               'last_name': 'Carey',
               'birth_date': '27.03.1970',
               'hobbies': ['Sing', 'Compose', 'Act']}

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
    actions[choice - 1](person_info)
