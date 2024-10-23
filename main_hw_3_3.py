#Домашнє завдання: Модуль - 3, завдання - 3(не обов'язкове). Python Core 2.0. (PYTHON SOFTWARE ENGINEERING. Гнучкий формат)

# Імпорт модуля re
import re
'''
ОПИС:
    Функція, яка нормалізує телефонні номери до стандартного формату.
ВХІДНІ ПАРАМЕТРИ:
    phone_number — рядок (str), з телефонним номером у різноманітних форматах.
ВИХІДНІ ДАНІ:
    modif_number - рядок (str), нормалізований телефонний номер.
'''
def normalize_phone(phone_number):
    # Видалення усіх символів окрім цифр, використовуючи регулярний вираз
    modif_number = re.sub(r'[^\d]', '', phone_number)
    # Добавлення знака "+" на початок номера
    if len(modif_number) == 12:
        modif_number = "+" + modif_number
    # Добавлення "+38" на початок номера
    if len(modif_number) == 10:
        modif_number = "+38" + modif_number
    # Повернення телефонного номера у правильному форматі (+38хххххххххх)
    return modif_number