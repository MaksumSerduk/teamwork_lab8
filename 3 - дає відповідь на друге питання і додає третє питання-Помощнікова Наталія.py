
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

#Відповідь на друге питання і запис третього питання - Помощнікова Наталія

def add_answer2_and_question3():
    try:
        # читання поточного вмісту файлу
        with open("team_work.txt", "r", encoding="utf-8") as file:
            content = file.read()
        print("Поточний вміст файлу:")
        print("----------------------------")
        print(content)
        print("----------------------------")

        # додавання відповідь №2 і нове питання №3
        with open("team_work.txt", "a", encoding="utf-8") as file:
            file.write("\nВідповідь №2: Помощнікова Наталія\n")
            file.write(
                "Словник (dict) у Python — це структура даних, яка зберігає пари ключ:значення. "
                "Ключі мають бути унікальними. Словник можна створити так:\n"
                "my_dict = {'name': 'Anna', 'age': 20}\n"
                "Щоб отримати доступ до значення, використовують ключ:\n"
                "print(my_dict['name'])  # Anna\n"
            )

            file.write("\nПитання №3: Помощнікова Наталія\n")
            file.write("3. Що таке цикл for у Python і як він працює?\n")

        print("Відповідь №2 і питання №3 успішно додано!")

    except FileNotFoundError:
        print("Помилка: файл 'team_work.txt' не знайдено.")
    except PermissionError:
        print("Помилка: немає дозволу для запису у файл.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")


def read_file_after_q3():
    try:
        with open("team_work.txt", "r", encoding="utf-8") as file:
            print("\nВміст файлу після додавання відповіді №2 і питання №3:")
            print("----------------------------")
            print(file.read())
    except Exception as e:
        print("Помилка:", e)


# Виклик:
add_answer2_and_question3()
read_file_after_q3()
