
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def permutations(elements):
    if len(elements) == 1:
        return [elements]
    result = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i + 1:]
        for p in permutations(rest):
            result.append([elements[i]] + p)
    return result


def print_distance_matrix(cities, distances):
    n = len(cities)
    width = max(len(city) for city in cities) + 3
    print("\nМАТРИЦЯ ВІДСТАНЕЙ:")
    print("".ljust(width), end="")
    for city in cities:
        print(city.ljust(width), end="")
    print()
    for i in range(n):
        print(cities[i].ljust(width), end="")
        for j in range(n):
            print(str(distances[i][j]).ljust(width), end="")
        print()


def main():
    cities = ["Київ", "Львів", "Одеса", "Дніпро"]
    distances = [
        [0, 540, 475, 480],
        [540, 0, 790, 830],
        [475, 790, 0, 620],
        [480, 830, 620, 0]
    ]

    distance_dict = {
        cities[i]: {cities[j]: distances[i][j] for j in range(len(cities)) if i != j}
        for i in range(len(cities))
    }

    print("СЛОВНИК ВІДСТАНЕЙ (місто: інші міста та відстані):")
    for city, d in distance_dict.items():
        print(f"  {city}: {d}")

    print_distance_matrix(cities, distances)

    all_routes = permutations([1, 2, 3])
    shortest_distance = float('inf')
    best_routes = []

    print("\nВСІ МОЖЛИВІ МАРШРУТИ ТА ЇХ ДОВЖИНИ:")
    for route in all_routes:
        full_route = [0] + route + [0]
        distance_sum = 0
        print("\nМаршрут:", " → ".join(cities[i] for i in full_route))
        for i in range(len(full_route) - 1):
            a, b = full_route[i], full_route[i + 1]
            step = distances[a][b]
            distance_sum += step
            print(f"  Крок {i + 1}: {cities[a]} → {cities[b]} = {step} км (сума: {distance_sum})")
        print(f"  Загальна довжина маршруту: {distance_sum} км")

        if distance_sum < shortest_distance:
            shortest_distance = distance_sum
            best_routes = [full_route]
        elif distance_sum == shortest_distance:
            best_routes.append(full_route)

    print("\n--- РЕЗУЛЬТАТ ---")
    print(f"Кількість можливих маршрутів: {len(all_routes)}")
    print(f"Найкоротша довжина маршруту: {shortest_distance} км")
    print("Оптимальні маршрути:")
    for r in best_routes:
        print(" → ".join(cities[i] for i in r))


if __name__ == "__main__":
    main()
