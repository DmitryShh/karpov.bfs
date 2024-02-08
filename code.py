import pandas as pd
from collections import deque
#Проверка клетки
def is_valid_move(y, x, city_map_list):
    return 0 <= y < len(city_map_list) and 0 <= x < len(city_map_list[0]) and city_map_list[x][y] == 1

def findpath(start, end, city_map_list):
    rows, cols = len(city_map_list), len(city_map_list[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]

    sy,sx = start
    queue = deque([(sy,sx)])  # (x, y)
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        # Проверяем, достигли ли мы конечной точки
        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[x][y]
            return path[::-1]

        # Перебираем соседей и добавляем их в очередь, если они доступны
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for nx, ny in neighbors:
            if is_valid_move(nx, ny, city_map_list) and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)

    # Если не удалось достичь конечной точки
    return None

# Пример использования
df = pd.read_csv('city_map.csv', names=list(range(0, 100, 1)))
city_map_list = df.values.tolist()

courier_location = (17, 99)
orders_location = [(42, 76), (27, 80), (43, 52), (26, 75)]

route = []
for destination in orders_location:
    path = findpath(courier_location, destination, city_map_list)
    if path:
        route.extend(path)
        courier_location = destination
    print (route)
