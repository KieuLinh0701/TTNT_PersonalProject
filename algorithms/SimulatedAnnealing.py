import random
import math
from algorithms.BeliefState import beliefState

def simulatedAnnealing(start, goal):
    # Định nghĩa các tham số cố định bên trong hàm
    initial_temp = 10000   # Nhiệt độ ban đầu
    cooling_rate = 0.99   # Hệ số làm nguội
    min_temp = 1          # Ngưỡng dừng

    current = start
    current_heuristic = beliefState(current, goal)  # Sử dụng môi trường niềm tin từ hàm belief_state
    path = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, xuống, trái, phải
    temp = initial_temp

    while current != goal and temp > min_temp:
        zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if current[i][j] == 0)

        # Danh sách các trạng thái lân cận
        neighbors = []
        for dx, dy in directions:
            newX, newY = zeroX + dx, zeroY + dy
            if 0 <= newX < 3 and 0 <= newY < 3:
                newState = [row[:] for row in current]
                newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]
                neighbors.append((newState, beliefState(newState, goal)))  # Sử dụng môi trường niềm tin

        if not neighbors:
            break

        # Chọn ngẫu nhiên một trạng thái lân cận
        next_state, next_heuristic = random.choice(neighbors)

        # Tính chênh lệch heuristic
        delta = next_heuristic - current_heuristic

        # Quyết định chấp nhận trạng thái mới hay không
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = next_state
            current_heuristic = next_heuristic
            path.append(current)

        # Giảm nhiệt độ
        temp *= cooling_rate

    return path if current == goal else None