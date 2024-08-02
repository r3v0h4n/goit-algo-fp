def greedy_algorithm(items, budget):
    # Сортування за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    current_budget = budget
    
    for item, info in sorted_items:
        if info['cost'] <= current_budget:
            chosen_items.append(item)
            total_calories += info['calories']
            current_budget -= info['cost']
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    total_calories = dp[n][budget]
    chosen_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, info = item_list[i - 1]
            chosen_items.append(name)
            w -= info['cost']
    
    return chosen_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Загальна калорійність:", greedy_calories)

dp_items, dp_calories = dynamic_programming(items, budget)
print()
print("Динамічне програмування:")
print("Вибрані страви:", dp_items)
print("Загальна калорійність:", dp_calories)