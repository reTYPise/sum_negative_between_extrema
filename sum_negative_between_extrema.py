import random

def solve_task(arr):
    """
    Находит сумму отрицательных элементов, расположенных между 
    максимальным и минимальным элементами массива.
    """
    if len(arr) < 2:
        return 0, "Массив слишком мал для выполнения операции."

    # Поиск индексов максимального и минимального элементов
    # Используем enumerate для получения индекса и значения за один проход
    max_val = arr[0]
    min_val = arr[0]
    idx_max = 0
    idx_min = 0

    for i, val in enumerate(arr):
        if val > max_val:
            max_val = val
            idx_max = i
        if val < min_val:
            min_val = val
            idx_min = i

    # Определение границ диапазона (строго между элементами)
    left_bound = min(idx_max, idx_min)
    right_bound = max(idx_max, idx_min)

    # Если элементы стоят рядом, диапазон пуст
    if right_bound - left_bound <= 1:
        return 0, f"Максимум (индекс {idx_max}) и минимум (индекс {idx_min}) стоят рядом или совпадают."

    # Вычисление суммы отрицательных элементов в диапазоне
    negative_sum = 0
    subset = []
    
    # Проходим от left_bound + 1 до right_bound - 1
    for i in range(left_bound + 1, right_bound):
        if arr[i] < 0:
            negative_sum += arr[i]
            subset.append(arr[i])

    info = (f"Максимум: {max_val} (индекс {idx_max}), "
            f"Минимум: {min_val} (индекс {idx_min}). "
            f"Диапазон между индексами {left_bound+1} и {right_bound-1}. "
            f"Отрицательные элементы в диапазоне: {subset}")
            
    return negative_sum, info

# --- Блок выполнения и демонстрации ---
if __name__ == "__main__":
    # Генерация случайного массива для примера (можно заменить на input())
    N = random.randint(5, 15)
    A = [random.randint(-50, 50) for _ in range(N)]
    
    print(f"Исходный массив A: {A}")
    
    result, description = solve_task(A)
    
    print("\n--- Результаты вычислений ---")
    print(description)
    print(f"Итоговая сумма отрицательных элементов между экстремумами: {result}")
