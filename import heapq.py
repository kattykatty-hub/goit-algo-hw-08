import heapq

def minimize_cost(cables):
    heapq.heapify(cables)  # перетворюємо список в купу
    
    total_cost = 0
    
    while len(cables) > 1:
        # беремо два найкоротших кабелі з купи
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        
        # об'єднуємо їх та додаємо витрати до загальних витрат
        cost = shortest1 + shortest2
        total_cost += cost
        
        # додаємо об'єднаний кабель назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [8, 5, 4, 2]
min_cost = minimize_cost(cables)
print("Мінімальні витрати на об'єднання кабелів:", min_cost)  # Виведе 36
