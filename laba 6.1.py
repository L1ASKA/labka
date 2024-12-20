import itertools
import math
import time
# 1 часть – написать программу в соответствии со своим вариантом задания.
# Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
# 1. Алгоритмический вариант (с использованием сочетаний)
# IT-предприятие набирает сотрудников: 2 тимлида, 2 проджек-менеджера, 3 синьера, 3 мидла, 4 юниора.
# Сформировать все возможные варианты заполнения вакантных мест, если имеются 16 претендентов.
# 1. Алгоритмический вариант (с использованием сочетаний)
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
candidates = list(range(16))

# Формируем все возможные варианты для каждой должности
timleads = list(itertools.combinations(candidates, 2))  # 2 тимлида из 16
project_managers = [combo for combo in itertools.combinations([i for i in candidates if i not in timleads[0]], 2)]  # 2 проджек-менеджера из оставшихся
seniors = [combo for combo in itertools.combinations([i for i in candidates if i not in timleads[0] and i not in project_managers[0]], 3)]  # 3 синьора из оставшихся
mid_level = [combo for combo in itertools.combinations([i for i in candidates if i not in timleads[0] and i not in project_managers[0] and i not in seniors[0]], 3)]  # 3 мидла из оставшихся
juniors = [combo for combo in itertools.combinations([i for i in candidates if i not in timleads[0] and i not in project_managers[0] and i not in seniors[0] and i not in mid_level[0]], 4)]  # 4 юниора из оставшихся

end_time_itertools = time.time()
execution_time_itertools = end_time_itertools - start_time_itertools

# Выводим все возможные варианты для каждой группы
print("Все возможные варианты распределения должностей:")

print("\nТимлиды (выбор 2 из 16):")
for combo in timleads:
    print(combo)

print("\nПроджек-менеджеры (выбор 2 из оставшихся):")
for combo in project_managers:
    print(combo)

print("\nСиньоры (выбор 3 из оставшихся):")
for combo in seniors:
    print(combo)

print("\nМидлы (выбор 3 из оставшихся):")
for combo in mid_level:
    print(combo)

print("\nЮниоры (выбор 4 из оставшихся):")
for combo in juniors:
    print(combo)

# Выводим результаты для алгоритмического подхода
print("\nАлгоритмический подход (с пояснениями):")
print(f"\n1. Для тимлидов (выбор 2 из 16): C(16, 2) = {timleads_combinations}")
print(f"2. Для проджек-менеджеров (выбор 2 из 14): C(14, 2) = {project_managers_combinations}")
print(f"3. Для синьоров (выбор 3 из 12): C(12, 3) = {seniors_combinations}")
print(f"4. Для мидлов (выбор 3 из 9): C(9, 3) = {mid_level_combinations}")
print(f"5. Для юниоров (выбор 4 из 6): C(6, 4) = {juniors_combinations}")

# Выводим общий результат для алгоритмического метода
print(f"\nОбщее количество вариантов (алгоритмическим методом): {result_algorithmic}")
print(f"Время выполнения (алгоритмический метод): {execution_time_algorithmic:.6f} секунд")

# Выводим результаты для метода с использованием itertools
print("\nМетод с использованием itertools (с пояснениями):")
print(f"\n1. Для тимлидов (выбор 2 из 16): C(16, 2) = {len(timleads)}")
print(f"2. Для проджек-менеджеров (выбор 2 из оставшихся): C(14, 2) = {len(project_managers)}")
print(f"3. Для синьоров (выбор 3 из оставшихся): C(12, 3) = {len(seniors)}")
print(f"4. Для мидлов (выбор 3 из оставшихся): C(9, 3) = {len(mid_level)}")
print(f"5. Для юниоров (выбор 4 из оставшихся): C(6, 4) = {len(juniors)}")

# Выводим все возможные варианты для метода с использованием itertools
total_combinations_itertools = len(timleads) * len(project_managers) * len(seniors) * len(mid_level) * len(juniors)
print(f"\nОбщее количество вариантов (itertools): {total_combinations_itertools}")
print(f"Время выполнения (itertools): {execution_time_itertools:.6f} секунд")
