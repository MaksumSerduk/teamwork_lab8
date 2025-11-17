# Створення файлу та запис першого питання - Сердюк Максим
def create_file():
    try:
        with open("team_work.txt", "w", encoding="utf-8") as file:
            file.write("Файл для лабораторної роботи №8.Тема Python: запитання - відповідь\n")
        print("Файл team_work.txt успішно створено")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

def first_question():
    try:
        with open("team_work.txt", "a", encoding="utf-8") as file:
            file.write("\nПитання №1: Сердюк Максим\n")
            file.write("1. Що таке список (list) у Python і як додати новий елемент у список?\n")
        print("Питання №1 успішно додано до файлу")
    except PermissionError:
        print("Помилка: немає дозволу на запис у файл")
    except FileNotFoundError:
        print("Помилка: файл не знайдено")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

def read_file():
    try:
        with open("team_work.txt", "r", encoding="utf-8") as file:
            print("Вміст файлу після створення питання:")
            print("----------------------------")
            print(file.read())
    except FileNotFoundError:
        print("Помилка: файл не знайдено")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

# Виклик функцій
create_file()
first_question()
read_file()
