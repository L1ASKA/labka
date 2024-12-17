import itertools
import math
import time
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики
# объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.
#	F(x<2) = 3; F(n) = (-1)n*(F(n-1)/n! + F(n-5) /(2n)!)
# Пример данных о претендентах (индекс - это номер претендента, а число - это его опыт в годах)
candidates_experience = [7, 3, 5, 6, 2, 4, 8, 1, 10, 3, 4, 6, 7, 5, 2, 9]

# Минимальные требования к опыту для каждой должности
min_experience = {
    "timlead": 5,
    "project_manager": 3,
    "senior": 4,
    "mid_level": 2,
    "junior": 1
}


# 1. Алгоритмический метод (с использованием сочетаний)
def combinations(n, k):
    return math.comb(n, k)


# 2. Метод с использованием itertools (функции Python)
def generate_combinations(n, k):
    return list(itertools.combinations(range(n), k))


# 3. Функция для подсчета суммарного опыта выбранных кандидатов
def calculate_experience(combination, candidates_experience):
    return sum(candidates_experience[i] for i in combination)


# 4. Функция для нахождения лучших вариантов по сумме опыта с учётом ограничений
def find_optimal_combination(candidates, num_selections, min_experience):
    optimal_combinations = []
    max_experience = 0

    # Пробуем все сочетания для заданного количества кандидатов
    for combination in itertools.combinations(candidates, num_selections):
        # Проверяем, что все кандидаты в комбинации соответствуют минимальным требованиям
        valid_combination = all(candidates_experience[i] >= min_experience for i in combination)
        if valid_combination:
            experience_sum = sum(candidates_experience[i] for i in combination)
            if experience_sum > max_experience:
                max_experience = experience_sum
                optimal_combinations = [combination]
            elif experience_sum == max_experience:
                optimal_combinations.append(combination)

    return optimal_combinations, max_experience


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

# Формируем все возможные варианты с использованием itertools
timleads = list(itertools.combinations(range(16), 2))
project_managers = list(itertools.combinations(range(14), 2))
seniors = list(itertools.combinations(range(12), 3))
mid_level = list(itertools.combinations(range(9), 3))
juniors = list(itertools.combinations(range(6), 4))

end_time_itertools = time.time()
execution_time_itertools = end_time_itertools - start_time_itertools

# 5. Применяем ограничение и целевую функцию для нахождения оптимальных комбинаций
optimal_timleads, max_timlead_experience = find_optimal_combination(range(16), 2, min_experience["timlead"])
optimal_project_managers, max_project_manager_experience = find_optimal_combination(range(14), 2,
                                                                                    min_experience["project_manager"])
optimal_seniors, max_senior_experience = find_optimal_combination(range(12), 3, min_experience["senior"])
optimal_mid_level, max_mid_level_experience = find_optimal_combination(range(9), 3, min_experience["mid_level"])
optimal_juniors, max_junior_experience = find_optimal_combination(range(6), 4, min_experience["junior"])

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
print(
    f"2. Для проджек-менеджеров (выбор 2 из 14): C(14, 2) = {len(project_managers)} - комбинации из 14 претендентов, выбраны 2.")
print(f"3. Для синьоров (выбор 3 из 12): C(12, 3) = {len(seniors)} - комбинации из 12 претендентов, выбраны 3.")
print(f"4. Для мидлов (выбор 3 из 9): C(9, 3) = {len(mid_level)} - комбинации из 9 претендентов, выбраны 3.")
print(f"5. Для юниоров (выбор 4 из 6): C(6, 4) = {len(juniors)} - комбинации из 6 претендентов, выбраны 4.")

# Выводим общий результат для метода с использованием itertools
total_combinations = len(timleads) * len(project_managers) * len(seniors) * len(mid_level) * len(juniors)
print(f"\nОбщее количество вариантов (itertools): {total_combinations}")
print(f"Время выполнения (itertools): {execution_time_itertools:.6f} секунд")

# Выводим результаты для оптимизации по опыту
print("\nОптимизация по опыту:")
print(f"\n1. Для тимлидов с минимальным опытом {min_experience['timlead']} лет:")
print(f"   Лучшие кандидаты: {optimal_timleads} с максимальным опытом {max_timlead_experience} лет.")
print(f"2. Для проджек-менеджеров с минимальным опытом {min_experience['project_manager']} лет:")
print(f"   Лучшие кандидаты: {optimal_project_managers} с максимальным опытом {max_project_manager_experience} лет.")
print(f"3. Для синьоров с минимальным опытом {min_experience['senior']} лет:")
print(f"   Лучшие кандидаты: {optimal_seniors} с максимальным опытом {max_senior_experience} лет.")
print(f"4. Для мидлов с минимальным опытом {min_experience['mid_level']} лет:")
print(f"   Лучшие кандидаты: {optimal_mid_level} с максимальным опытом {max_mid_level_experience} лет.")
print(f"5. Для юниоров с минимальным опытом {min_experience['junior']} лет:")
print(f"   Лучшие кандидаты: {optimal_juniors} с максимальным опытом {max_junior_experience} лет.")