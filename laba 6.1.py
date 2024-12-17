import itertools
import math
import time
# 1 часть – написать программу в соответствии со своим вариантом задания.
# Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
# 1. Алгоритмический вариант (с использованием сочетаний)
# IT-предприятие набирает сотрудников: 2 тимлида, 2 проджек-менеджера, 3 синьера, 3 мидла, 4 юниора.
# Сформировать все возможные варианты заполнения вакантных мест, если имеются 16 претендентов.
def combinations(n, k):
    return math.comb(n, k)

# 2. Вариант с использованием функций Python (itertools)
def generate_combinations(n, k):
    return list(itertools.combinations(range(n), k))

# Замер времени для алгоритмического метода
start_time_algorithmic = time.time()

# Вычисляем количество вариантов для каждой должности (алгоритмический метод)
timleads_combinations = combinations(16, 2)
project_managers_combinations = combinations(14, 2)
seniors_combinations = combinations(12, 3)
mid_level_combinations = combinations(9, 3)
juniors_combinations = combinations(6, 4)

# Общий результат (алгоритмический метод)
result_algorithmic = (timleads_combinations * project_managers_combinations * seniors_combinations *
                      mid_level_combinations * juniors_combinations)

end_time_algorithmic = time.time()
execution_time_algorithmic = end_time_algorithmic - start_time_algorithmic

# Замер времени для метода с использованием itertools
start_time_itertools = time.time()

# Формируем все возможные варианты с помощью itertools (функциональный метод)
timleads = list(itertools.combinations(range(16), 2))
project_managers = list(itertools.combinations(range(14), 2))
seniors = list(itertools.combinations(range(12), 3))
mid_level = list(itertools.combinations(range(9), 3))
juniors = list(itertools.combinations(range(6), 4))

end_time_itertools = time.time()
execution_time_itertools = end_time_itertools - start_time_itertools

# Выводим результаты для алгоритмического подхода
print("Алгоритмический подход (с пояснениями):")
print(f"\n1. Для тимлидов (выбор 2 из 16): C(16, 2) = {timleads_combinations} ({16} * {15} / 2!)")
print(f"2. Для проджек-менеджеров (выбор 2 из 14): C(14, 2) = {project_managers_combinations} ({14} * {13} / 2!)")
print(f"3. Для синьоров (выбор 3 из 12): C(12, 3) = {seniors_combinations} ({12} * {11} * {10} / 3!)")
print(f"4. Для мидлов (выбор 3 из 9): C(9, 3) = {mid_level_combinations} ({9} * {8} * {7} / 3!)")
print(f"5. Для юниоров (выбор 4 из 6): C(6, 4) = {juniors_combinations} ({6} * {5} / 2!)")

# Выводим общий результат для алгоритмического метода
print(f"\nОбщее количество вариантов (алгоритмическим методом): {result_algorithmic}")
print(f"Время выполнения (алгоритмический метод): {execution_time_algorithmic:.6f} секунд")

# Выводим результаты для метода с использованием itertools
print("\nМетод с использованием itertools (с пояснениями):")
print(f"\n1. Для тимлидов (выбор 2 из 16): C(16, 2) = {len(timleads)} - комбинации из 16 претендентов, выбраны 2.")
print(f"2. Для проджек-менеджеров (выбор 2 из 14): C(14, 2) = {len(project_managers)} - комбинации из 14 претендентов, выбраны 2.")
print(f"3. Для синьоров (выбор 3 из 12): C(12, 3) = {len(seniors)} - комбинации из 12 претендентов, выбраны 3.")
print(f"4. Для мидлов (выбор 3 из 9): C(9, 3) = {len(mid_level)} - комбинации из 9 претендентов, выбраны 3.")
print(f"5. Для юниоров (выбор 4 из 6): C(6, 4) = {len(juniors)} - комбинации из 6 претендентов, выбраны 4.")

# Выводим общий результат для метода с использованием itertools
total_combinations = len(timleads) * len(project_managers) * len(seniors) * len(mid_level) * len(juniors)
print(f"\nОбщее количество вариантов (itertools): {total_combinations}")
print(f"Время выполнения (itertools): {execution_time_itertools:.6f} секунд")