from queue import PriorityQueue

# Thuật toán A* (viết lại để trả về trạng thái sau từng bước di chuyển)
def component(initial, goal):
    queue = PriorityQueue()
    queue.put((0, initial, [initial]))  # (cost, state, path (as a list of states))
    visited = set()

    while not queue.empty():
        cost, current_state, path = queue.get()
        if is_goal(current_state, goal):
            return path  # Trả về danh sách các trạng thái nếu đạt trạng thái mục tiêu

        visited.add(tuple(map(tuple, current_state)))  # Chuyển trạng thái sang tuple để lưu vào set

        for neighbor, action in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                new_cost = cost + 1 + heuristic(neighbor, goal)
                queue.put((new_cost, neighbor, path + [neighbor]))  # Thêm trạng thái mới vào path

    return None  # Không tìm thấy giải pháp

# Hàm tìm vị trí số 0
def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# Kiểm tra trạng thái mục tiêu
def is_goal(state, goal):
    return state == goal

# Tính toán heuristic (số ô sai vị trí)
def heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h += 1
    return h

# Lấy các trạng thái kế tiếp
def get_neighbors(state):
    neighbors = []
    zero_pos = find_zero(state)
    i, j = zero_pos

    directions = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1)
    }

    for direction, (di, dj) in directions.items():
        ni, nj = i + di, j + dj
        if 0 <= ni < len(state) and 0 <= nj < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append((new_state, direction))

    return neighbors