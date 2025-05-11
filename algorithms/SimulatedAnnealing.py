import random
import math
from algorithms.BeliefState import beliefState

def simulatedAnnealing(start, goal):
    # Định nghĩa các tham số cố định bên trong hàm
    initialTemp = 10000   # Nhiệt độ ban đầu
    coolingRate = 0.99   # Hệ số làm nguội
    minTemp = 1          # Ngưỡng dừng

    current = start
    currentHeuristic = beliefState(current, goal)  # Sử dụng môi trường niềm tin từ hàm belief_state
    path = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, xuống, trái, phải
    temp = initialTemp

    while current != goal and temp > minTemp:
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
        nextState, nextHeuristic = random.choice(neighbors)

        # Tính chênh lệch heuristic
        delta = nextHeuristic - currentHeuristic

        # Quyết định chấp nhận trạng thái mới hay không
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = nextState
            currentHeuristic = nextHeuristic
            path.append(current)

        # Giảm nhiệt độ
        temp *= coolingRate

    return path if current == goal else None