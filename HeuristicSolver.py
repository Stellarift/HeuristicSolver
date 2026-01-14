#задание 1
def min_refuels(distances, S, L):
    current_fuel = S
    current_pos = 0
    refuels = []
    
    stations = [0]
    for d in distances:
        stations.append(stations[-1] + d)
    
    i = 0
    n = len(stations) - 1
    
    while i < n:
        max_reach = current_pos + current_fuel
        
        next_station = i
        while next_station < n and stations[next_station + 1] <= max_reach:
            next_station += 1
        
        if next_station == i:
            return "Невозможно доехать"
        
        distance_traveled = stations[next_station] - current_pos
        current_fuel -= distance_traveled
        current_pos = stations[next_station]
        i = next_station
        
        if i < n:
            if current_fuel >= (L - current_pos):
                break
            else:
                refuels.append(i + 1)
                current_fuel = S
    
    return refuels
#задание 2
def max_meetings(meetings, min_break=0):
    if not meetings:
        return []
    
    meetings_sorted = sorted(meetings, key=lambda x: x[1])
    
    selected = []
    last_end = -float('inf')
    
    for start, end in meetings_sorted:
        if start >= last_end + min_break:
            selected.append((start, end))
            last_end = end
    
    return selected

if __name__ == "__main__":
    print("Оценка сложности эвристических алгоритмов")

    print("1.Минимальное количество заправок")
    
    try:
        n = int(input("Введите количество отрезков между заправками: "))
        distances = []
        for i in range(n):
            d = float(input(f"  Расстояние D{i+1} (км): "))
            distances.append(d)
        
        S = float(input("Запас хода на полном баке S (км): "))
        
        L = sum(distances)
        print(f"\nОбщее расстояние от Петербурга до Москвы: {L} км")
        
        result = min_refuels(distances, S, L)
        
        if isinstance(result, str):
            print(f"\nРезультат: {result}")
        else:
            print(f"\nНомера заправок для дозаправки: {result}")
            print(f"Минимальное количество заправок: {len(result)}")
    
    except ValueError:
        print("Ошибка ввода данных!")
    
    print("2. Максимальное количество заседаний")
    
    try:
        m = int(input("Введите количество заседаний: "))
        meetings = []
        for i in range(m):
            start = float(input(f"  Начало заседания {i+1}: "))
            end = float(input(f"  Конец заседания {i+1}: "))
            meetings.append((start, end))
        
        min_break = float(input("Минимальный перерыв между заседаниями: "))
        
        result = max_meetings(meetings, min_break)
        
        print(f"\nВыбранные заседания:")
        for i, (start, end) in enumerate(result, 1):
            print(f"  {i}. С {start} до {end}")
        print(f"Максимальное количество заседаний: {len(result)}")
    
    except ValueError:
        print("Ошибка ввода данных!")
    
    print("РАБОТА ЗАВЕРШЕНА")