
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
# відповідь на перше питання і додає друге питання - Бардакова Надія

def add_answer_and_question():
    try:
        # читаємо поточний вміст файлу
        with open("team_work.txt", "r", encoding="utf-8") as file:
            content = file.read()
        print("Поточний вміст файлу:")
        print("----------------------------")
        print(content)
        print("----------------------------")

        # додаємо відповідь і нове питання
        with open("team_work.txt", "a", encoding="utf-8") as file:
            file.write("\nВідповідь №1: Бардакова Надія\n")
            file.write(
                "Список (list) у Python — це впорядкована колекція елементів, "
                "яка може містити об’єкти різних типів. "
                "Списки створюються за допомогою квадратних дужок []. "
                "Новий елемент можна додати методом append(), наприклад:\n"
                "my_list = [1, 2, 3]\nmy_list.append(4)  # [1, 2, 3, 4]\n"
            )
            file.write("\nПитання №2: Бардакова Надія\n")
            file.write("2. Як у Python створити словник (dict) та отримати доступ до його елементів?\n")

        print(" Відповідь і нове питання успішно додано до файлу.")

    except FileNotFoundError:
        print(" Помилка: файл 'team_work.txt' не знайдено. Спочатку виконай код першого студента.")
    except PermissionError:
        print(" Помилка: немає дозволу на зміну файлу.")
    except Exception as e:
        print(f" Несподівана помилка: {e}")


def read_updated_file():
    """Зчитуємо вміст файлу після змін"""
    try:
        with open("team_work.txt", "r", encoding="utf-8") as file:
            print("\nОновлений вміст файлу:")
            print("----------------------------")
            print(file.read())
    except Exception as e:
        print(f"Помилка під час читання: {e}")


# --- Виконання ---
add_answer_and_question()
read_updated_file()