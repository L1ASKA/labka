import time
from math import factorial

def f_recursive(n, memo={}):
    """Рекурсивный подход с мемоизацией."""
    if n in memo:
        return memo[n]
    if n < 2:
        return 3
    sign = -1 if n % 2 != 0 else 1
    result = sign * (f_recursive(n - 1, memo) / factorial(n) + \
                     (f_recursive(n - 5, memo) if n >= 5 else 0) / factorial(2 * n))
    memo[n] = result
    return result

def f_iterative(n):
    """Итеративный подход."""
    if n < 2:
        return 3
    values = [3] * max(5, n + 1)  # инициализация значений для первых 5 элементов
    for i in range(2, n + 1):
        sign = -1 if i % 2 != 0 else 1
        prev = values[i - 1] / factorial(i)
        prev5 = values[i - 5] / factorial(2 * i) if i >= 5 else 0
        values[i] = sign * (prev + prev5)
    return values[n]

def measure_time(func, n):
    """Измерение времени выполнения функции."""
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    # Параметры тестирования
    test_values = [5, 10, 15, 20, 25, 30]  # значения n для теста
    results = []

    print("n\tRecursive Result\tRecursive Time\tIterative Result\tIterative Time")
    print("-" * 60)

    for n in test_values:
        try:
            rec_result, rec_time = measure_time(f_recursive, n)
        except RecursionError:
            rec_result, rec_time = "Overflow", "N/A"

        try:
            it_result, it_time = measure_time(f_iterative, n)
        except MemoryError:
            it_result, it_time = "Overflow", "N/A"

        results.append((n, rec_result, rec_time, it_result, it_time))
        print(f"{n}\t{rec_result}\t{rec_time:.6f}\t{it_result}\t{it_time:.6f}")

    # Анализ границ применимости
    print("\nAnalysis:")
    print("Recursive approach is limited by the recursion depth (default: 1000).")
    print("Iterative approach is generally more efficient in terms of memory and avoids recursion depth limitations.")