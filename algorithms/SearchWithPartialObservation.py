import heapq

# Tính toán độ khó của trạng thái (heuristic) dựa trên khoảng cách Manhattan
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                # Tìm vị trí của giá trị trong goal_state
                for gi in range(3):
                    for gj in range(3):
                        if goal_state[gi][gj] == state[i][j]:
                            goal_i, goal_j = gi, gj
                            break
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Hàm sinh các trạng thái kế tiếp từ trạng thái hiện tại
def get_neighbors(state):
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Di chuyển lên, xuống, trái, phải
    empty_row, empty_col = find_empty_tile(state)
    neighbors = []
    
    for action in actions:
        new_row, new_col = empty_row + action[0], empty_col + action[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]  # Tạo bản sao của state
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

# Tìm vị trí của ô trống (0)
def find_empty_tile(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col
    return None

# A* Search với partial observation
def searchWithPartialObservation(start_state, goal_state):
    open_list = []
    closed_list = set()
    
    # Dùng heap (priority queue) để giữ trạng thái theo chi phí
    heapq.heappush(open_list, (0 + manhattan_distance(start_state, goal_state), 0, start_state, []))
    
    while open_list:
        _, cost, current_state, path = heapq.heappop(open_list)
        
        # Nếu trạng thái đã được thăm, bỏ qua
        if tuple(map(tuple, current_state)) in closed_list:
            continue
        closed_list.add(tuple(map(tuple, current_state)))
        
        # Kiểm tra xem đã đạt được trạng thái mục tiêu chưa
        if current_state == goal_state:
            return path
        
        # Sinh các trạng thái kế tiếp và tính toán chi phí
        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in closed_list:
                new_cost = cost + 1  # Giả sử mỗi bước có chi phí bằng 1
                new_heuristic = manhattan_distance(neighbor, goal_state)
                heapq.heappush(open_list, (new_cost + new_heuristic, new_cost, neighbor, path + [neighbor]))
    
    return None  # Không tìm thấy giải pháp

# Ví dụ sử dụng
start_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Trạng thái bắt đầu
goal_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  # Trạng thái mục tiêu

solution_path = searchWithPartialObservation(start_state, goal_state)

# Hiển thị kết quả
if solution_path:
    print("Tìm thấy giải pháp:")
    for i, state in enumerate(solution_path):
        print(f"Bước {i + 1}:")
        for row in state:
            print(row)
else:
    print("Không tìm thấy giải pháp.")