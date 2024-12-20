import itertools
import math
import time
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
# (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.

# Функция для вычисления сочетаний (комбинаций)
def combinations(n, k):
    return math.comb(n, k)

# Ограничения: кандидаты с определенными номерами не могут занимать высокие должности
restricted_for_senior = {0, 1, 2}  # Не могут быть синьорами
restricted_for_timlead = {0, 1, 2}  # Не могут быть тимлидами
restricted_for_project_manager = {0, 1, 2}  # Не могут быть проджек-менеджерами

# Генерация кандидатов
candidates = list(range(16))

# Фильтрация кандидатов с учетом ограничений для должностей
def filter_candidates_for_position(candidates_list, restricted_candidates):
    return [candidate for candidate in candidates_list if candidate not in restricted_candidates]

# Функция для поиска всех возможных комбинаций для каждой должности с учетом ограничений
def generate_teams():
    timleads = filter_candidates_for_position(candidates, restricted_for_timlead)
    project_managers = filter_candidates_for_position(candidates, restricted_for_project_manager)
    seniors = filter_candidates_for_position(candidates, restricted_for_senior)

    # Для каждого кандидата находим все возможные комбинации
    timlead_combinations = itertools.combinations(timleads, 2)
    project_manager_combinations = itertools.combinations(project_managers, 2)
    senior_combinations = itertools.combinations(seniors, 3)
    mid_level_combinations = itertools.combinations(candidates, 3)
    junior_combinations = itertools.combinations(candidates, 4)

    return timlead_combinations, project_manager_combinations, senior_combinations, mid_level_combinations, junior_combinations

# Замер времени для выполнения
start_time = time.time()

# Генерация комбинаций для каждой должности
timlead_combinations, project_manager_combinations, senior_combinations, mid_level_combinations, junior_combinations = generate_teams()

# Целевая функция для оценки комбинации
def evaluate_combination(timlead_combo, project_manager_combo, senior_combo, mid_level_combo, junior_combo):
    # Мы можем, например, максимизировать количество уникальных кандидатов
    total_candidates = set(timlead_combo + project_manager_combo + senior_combo + mid_level_combo + junior_combo)
    return len(total_candidates)

best_combination = None
best_score = 0

# Перебор всех комбинаций для каждой должности
for timlead_combo in timlead_combinations:
    for project_manager_combo in project_manager_combinations:
        for senior_combo in senior_combinations:
            for mid_level_combo in mid_level_combinations:
                for junior_combo in junior_combinations:
                    score = evaluate_combination(timlead_combo, project_manager_combo, senior_combo, mid_level_combo, junior_combo)
                    if score > best_score:
                        best_score = score
                        best_combination = (timlead_combo, project_manager_combo, senior_combo, mid_level_combo, junior_combo)

end_time = time.time()
execution_time = end_time - start_time

# Вывод лучших результатов
print("Лучшее распределение с учетом ограничений (по должностям):")
print(f"Лучшее распределение кандидатов: {best_combination}")
print(f"Общее количество уникальных кандидатов: {best_score}")
print(f"\nВремя выполнения: {execution_time:.6f} секунд")
