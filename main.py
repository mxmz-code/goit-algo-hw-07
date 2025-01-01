import os
import random
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

# Очищення екрану
def clear_screen():
    """Очищає екран залежно від операційної системи."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Привітання та опис задач
def print_welcome_message():
    """Виводить привітання користувачу та опис задач."""
    print(Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════╗")
    print(Fore.GREEN + "  Привіт, користувач!")
    print(Fore.CYAN + "╚════════════════════════════════════════════╝")
    print()

# Клас для вузлів двійкового дерева пошуку
class Node:
    def __init__(self, key):
        """Ініціалізація вузла дерева з ключем."""
        self.left = None
        self.right = None
        self.value = key

# Клас для двійкового дерева пошуку
class BinarySearchTree:
    def __init__(self):
        """Ініціалізація порожнього дерева."""
        self.root = None

    def insert(self, key):
        """Метод для вставки нового елемента в дерево."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        """Рекурсивний метод для вставки елемента в дерево."""
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.value:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def find_max(self):
        """Метод для знаходження найбільшого елемента в дереві."""
        current = self.root
        while current and current.right:
            current = current.right
        return current.value if current else None

    def find_min(self):
        """Метод для знаходження найменшого елемента в дереві."""
        current = self.root
        while current and current.left:
            current = current.left
        return current.value if current else None

    def sum_all_values(self):
        """Метод для обчислення суми всіх значень у дереві."""
        return self._sum_all_values(self.root, 0)

    def _sum_all_values(self, node, current_sum):
        """Рекурсивний метод для обчислення суми всіх значень."""
        if node:
            current_sum += node.value
            current_sum = self._sum_all_values(node.left, current_sum)
            current_sum = self._sum_all_values(node.right, current_sum)
        return current_sum

    def display(self, indent=0):
        """Метод для виведення дерева на екран з відступами для ієрархії."""
        if self.root:
            self._display(self.root, indent)

    def _display(self, node, indent):
        """Рекурсивний метод для виведення дерева з відступами."""
        print(" " * indent + str(node.value))
        if node.left:
            self._display(node.left, indent + 4)
        if node.right:
            self._display(node.right, indent + 4)

# Генерація випадкових даних для дерева з перевіркою
def generate_unique_tree_data(size, min_value, max_value):
    """Генерує унікальні випадкові значення для дерева."""
    data = set()
    while len(data) < size:
        value = random.randint(min_value, max_value)
        if value not in data:
            data.add(value)
    return list(data)

# Клас для коментарів та їх відповідей
class Comment:
    def __init__(self, text, author):
        """Ініціалізація коментаря з текстом та автором."""
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додавання відповіді до коментаря."""
        self.replies.append(reply)

    def remove_reply(self):
        """Видалення відповіді та зміна тексту на стандартне повідомлення."""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        """Рекурсивне виведення коментаря та всіх відповідей з відступами."""
        author_color = self._get_author_color()  # Підсвічуємо різних авторів різними кольорами
        deleted_marker = " (видалено)" if self.is_deleted else ""
        print(" " * indent + author_color + f"{self.author}: {self.text}{deleted_marker}")
        
        for reply in self.replies:
            reply.display(indent + 4)

    def _get_author_color(self):
        """Метод для підсвічування авторів різними кольорами."""
        if self.author == "Бодя":
            return Fore.BLUE
        elif self.author == "Андрій":
            return Fore.RED
        elif self.author == "Марина":
            return Fore.GREEN
        else:
            return Fore.YELLOW

# Функція для виведення результатів
def print_results(fact, result):
    """Виводить факти та відповідні результати різними кольорами."""
    print(Fore.YELLOW + fact, end=" ")
    print(Fore.GREEN + f"{result}")

# Завдання 3: Пошук суми всіх значень у двійковому дереві
def task3_example():
    """Приклад для завдання 3, де обчислюється сума всіх значень у дереві."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(30)
    bst.insert(15)

    sum_values = bst.sum_all_values()
    return sum_values

# Завдання 4: Система коментарів
def task4_example():
    """Приклад для завдання 4, де створюється система коментарів та відповідей."""
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")
    reply3 = Comment("Мені дуже сподобалась!", "Бодя")
    reply4 = Comment("Може, це залежить від смаку?", "Андрій")
    reply5 = Comment("Я не розумію, чому так багато негативу", "Марина")
    
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)
    root_comment.add_reply(reply3)
    reply1.add_reply(reply4)
    reply2.add_reply(reply5)

    reply1.remove_reply()  # Видаляємо відповідь

    print(Fore.YELLOW + "\nКоментарі з відповідями:")
    root_comment.display()

# Основний код для виконання задач
if __name__ == "__main__":
    clear_screen()  # Очищаємо екран
    print_welcome_message()  # Печатаємо привітання та опис задач

    # Генерація даних для дерева
    tree_data = generate_unique_tree_data(10, 1, 50)  # Генеруємо 10 унікальних значень для дерева
    print(Fore.GREEN + "\nЗгенеровані дані для дерева:", tree_data)

    bst = BinarySearchTree()
    for value in tree_data:
        bst.insert(value)

    # Завдання 1: Побудова дерева пошуку
    print(Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════╗")
    print(Fore.GREEN + "  Завдання 1: Побудова двійкового дерева пошуку")
    print(Fore.YELLOW + "Опис задачі:")
    print("Створити двійкове дерево пошуку, виконати операції вставки, пошуку максимального та мінімального елемента, обходи дерева та вивести його візуально.")
    
    print(Fore.GREEN + "\nРішення задачі:")
    print(Fore.YELLOW + "\nДерево в порядку зростання (InOrder):")
    bst.display()
    
    # Завдання 1: Результати
    print(Fore.GREEN + "\nРезультати:")
    print_results("Максимальне значення у дереві:", bst.find_max()) 
    print_results("Найменше значення у дереві:", bst.find_min())
    print_results("Сума всіх значень у дереві:", bst.sum_all_values())
    
    print(Fore.CYAN + "╚════════════════════════════════════════════╝")

    # Завдання 2: Пошук найменшого елемента
    print(Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════╗")
    print(Fore.GREEN + "  Завдання 2: Пошук найменшого елемента")
    print(Fore.YELLOW + "Опис задачі:")
    print("Напишіть функцію для знаходження найменшого елемента у двійковому дереві пошуку.")
    
    print(Fore.GREEN + "\nРішення задачі:")
    print(Fore.YELLOW + "\nЗнаходимо найменше значення у дереві...")
    min_value = bst.find_min()
    
    print(Fore.GREEN + "\nРезультат:")
    print_results("Найменше значення у дереві:", min_value)
    print(Fore.CYAN + "╚════════════════════════════════════════════╝")
    
    # Завдання 3: Пошук суми всіх значень у дереві
    print(Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════╗")
    print(Fore.GREEN + "  Завдання 3: Пошук суми всіх значень")
    sum_values = task3_example()
    print_results("Сума всіх значень у дереві:", sum_values)
    print(Fore.CYAN + "╚════════════════════════════════════════════╝")

    # Завдання 4: Система коментарів
    print(Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════╗")
    print(Fore.GREEN + "  Завдання 4: Система коментарів")
    task4_example()
    print(Fore.CYAN + "╚════════════════════════════════════════════╝")
