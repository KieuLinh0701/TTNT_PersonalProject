import random
import copy

def qLearning(start_state, goal_state, episodes=1000):
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Di chuyển lên, xuống, trái, phải
    q_table = {}
    learning_rate = 0.1
    discount_factor = 0.9
    epsilon = 0.1

    def is_goal_state(state):
        return state == goal_state

    def find_empty_tile(state):
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    return row, col
        return None

    def is_valid_move(state, move):
        empty_row, empty_col = find_empty_tile(state)
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            return True
        return False

    def get_new_state(state, move):
        empty_row, empty_col = find_empty_tile(state)
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        new_state = copy.deepcopy(state)
        new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
        return new_state

    def get_reward(state):
        if is_goal_state(state):
            return 100
        return -1

    # Huấn luyện Q-table qua nhiều episode
    for episode in range(episodes):
        current_state = start_state
        epsilon = max(0.01, epsilon * 0.995)  # Giảm epsilon theo thời gian

        while not is_goal_state(current_state):
            if tuple(tuple(row) for row in current_state) not in q_table:
                q_table[tuple(tuple(row) for row in current_state)] = {a: 0 for a in actions}

            # Chọn hành động (epsilon-greedy)
            if random.random() < epsilon:
                action = random.choice(actions)
            else:
                action = max(q_table[tuple(tuple(row) for row in current_state)], 
                              key=q_table[tuple(tuple(row) for row in current_state)].get)

            # Thực hiện hành động
            if is_valid_move(current_state, action):
                next_state = get_new_state(current_state, action)
            else:
                next_state = current_state  # Nếu không hợp lệ, giữ nguyên trạng thái hiện tại

            reward = get_reward(next_state)

            # Cập nhật Q-table
            if tuple(tuple(row) for row in next_state) not in q_table:
                q_table[tuple(tuple(row) for row in next_state)] = {a: 0 for a in actions}

            current_q = q_table[tuple(tuple(row) for row in current_state)][action]
            max_next_q = max(q_table[tuple(tuple(row) for row in next_state)].values())
            new_q = current_q + learning_rate * (
                reward + discount_factor * max_next_q - current_q
            )
            q_table[tuple(tuple(row) for row in current_state)][action] = new_q

            # Di chuyển đến trạng thái tiếp theo
            current_state = next_state

    # Tái tạo đường đi sử dụng Q-table
    path = []
    current_state = start_state
    visited = set([tuple(tuple(row) for row in start_state)])
    max_steps = 9 * 9  # Giới hạn bước để tránh vòng lặp vô hạn

    while not is_goal_state(current_state) and len(path) < max_steps:
        if tuple(tuple(row) for row in current_state) not in q_table:
            return []  # Không tìm thấy đường đi
        action = max(q_table[tuple(tuple(row) for row in current_state)], 
                      key=q_table[tuple(tuple(row) for row in current_state)].get)

        if is_valid_move(current_state, action):
            next_state = get_new_state(current_state, action)
        else:
            next_state = current_state

        if tuple(tuple(row) for row in next_state) in visited:
            return []  # Không tìm thấy đường đi

        path.append(next_state)  # Không thêm start_state vào path
        visited.add(tuple(tuple(row) for row in next_state))
        current_state = next_state

    if is_goal_state(current_state):
        return path
    return []  # Không tìm thấy đường đi


# Ví dụ sử dụng thuật toán Q-learning cho 8-puzzle
start_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Trạng thái bắt đầu
goal_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  # Trạng thái mục tiêu

solution_path = qLearning(start_state, goal_state)

# Hiển thị kết quả
if solution_path:
    print("Tìm thấy giải pháp:")
    for i, state in enumerate(solution_path):
        print(f"Bước {i + 1}:")
        for row in state:
            print(row)
else:
    print("Không tìm thấy giải pháp.")