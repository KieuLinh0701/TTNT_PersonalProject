import random
import copy

def qLearning(start, goal, episodes=1000):
    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    qTable = {}  # Q-table để lưu giá trị Q cho từng trạng thái và hành động
    
    learningRate = 0.1  # Tốc độ học
    discountFactor = 0.9  # Hệ số chiết khấu
    epsilon = 0.1  # Xác suất chọn hành động ngẫu nhiên (epsilon-greedy)

    # Kiểm tra xem có phải trạng thái đích chưa
    def isGoal(state):
        return state == goal

    # Tìm vị trí của ô giá trị 0
    def findEmptyTile(state):
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    return row, col
        return None

    # Kiểm tra xem hành động có hợp lệ không
    def isValidMove(state, move):
        zeroX, zeroY = findEmptyTile(state)
        newX, newY = zeroX + move[0], zeroY + move[1]

        # Kiểm tra xem ô mới có nằm trong ma trận không
        if 0 <= newX < 3 and 0 <= newY < 3:
            return True
        return False

    # Tạo trạng thái mới bằng cách thực hiện hành động
    def getNewState(state, move):
        zeroX, zeroY = findEmptyTile(state)
        newX, newY = zeroX + move[0], zeroY + move[1]
        
        # Tạo trạng thái mới
        newState = [list(row) for row in state]
        # Hoán đổi vị trí ô trống với ô đích
        newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]
        
        return newState

    # Tính toán phần thưởng dựa trên trạng thái
    def getReward(state):
        if isGoal(state):  # Trạng thái đích
            return 100
        return -1  # Trạng thái thông thường

    # Huấn luyện Q-table qua nhiều episode
    for episode in range(episodes):

        # Bắt đầu từ trạng thái ban đầu
        current = start  
        epsilon = max(0.01, epsilon * 0.995)  # Giảm epsilon theo thời gian

        # Tiếp tục cho đến khi đạt trạng thái đích
        while not isGoal(current):
            # Nếu trạng thái hiện tại chưa có trong Q-table, khởi tạo giá trị Q cho tất cả hành động
            if tuple(tuple(row) for row in current) not in qTable:
                qTable[tuple(tuple(row) for row in current)] = {a: 0 for a in directions}

            # Chọn hành động (epsilon-greedy)
            if random.random() < epsilon:  # Chọn hành động ngẫu nhiên với xác suất epsilon
                action = random.choice(directions)
            else:  # Chọn hành động có giá trị Q cao nhất
                action = max(qTable[tuple(tuple(row) for row in current)], 
                        key=qTable[tuple(tuple(row) for row in current)].get)

            # Thực hiện hành động
            if isValidMove(current, action):
                nextState = getNewState(current, action)
            else:
                nextState = current  # Nếu không hợp lệ, giữ nguyên trạng thái

            reward = getReward(nextState)  # Nhận phần thưởng

            # Nếu trạng thái mới chưa có trong Q-table, khởi tạo giá trị Q
            if tuple(tuple(row) for row in nextState) not in qTable:
                qTable[tuple(tuple(row) for row in nextState)] = {a: 0 for a in directions}

            # Cập nhật Q-value theo công thức Q-learning
            currentQ = qTable[tuple(tuple(row) for row in current)][action]
            maxNextQ = max(qTable[tuple(tuple(row) for row in nextState)].values())
            newQ = currentQ + learningRate * (
                reward + discountFactor * maxNextQ - currentQ
            )
            qTable[tuple(tuple(row) for row in current)][action] = newQ

            # Di chuyển đến trạng thái tiếp theo
            current = nextState

    # Tái tạo đường đi sử dụng Q-table
    path = []
    current = start
    visited = set([tuple(tuple(row) for row in start)])  # Đánh dấu trạng thái đã thăm
    max_steps = 9 * 9  # Giới hạn bước để tránh vòng lặp vô hạn

    while not isGoal(current) and len(path) < max_steps:
        # Nếu trạng thái không có trong Q-table, không thể tái tạo đường đi
        if tuple(tuple(row) for row in current) not in qTable:
            return []
        # Chọn hành động tốt nhất từ Q-table
        action = max(qTable[tuple(tuple(row) for row in current)], 
                     key=qTable[tuple(tuple(row) for row in current)].get)

        if isValidMove(current, action):  # Nếu hành động hợp lệ
            nextState = getNewState(current, action)
        else:  # Nếu không hợp lệ, giữ nguyên trạng thái
            nextState = current

        # Kiểm tra trạng thái đã được thăm chưa để tránh vòng lặp
        if tuple(tuple(row) for row in nextState) in visited:
            return []

        path.append(nextState)  # Thêm trạng thái mới vào đường đi
        visited.add(tuple(tuple(row) for row in nextState))  # Đánh dấu trạng thái là đã thăm
        current = nextState

    # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
    if isGoal(current):
        return path
    return []  # Không tìm thấy đường đi