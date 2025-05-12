import heapq

# Tính toán độ khó của trạng thái (heuristic) dựa trên khoảng cách Manhattan
# Hàm này tính tổng khoảng cách Manhattan giữa các ô trong trạng thái hiện tại và vị trí của chúng trong trạng thái đích, chỉ dựa trên phần trạng thái quan sát được.
def manhattanDistance(state, goal, observedState):
    distance = 0
    for i in range(3):  
        for j in range(3):  
            if observedState[i][j] != 0:  # Nếu ô này có thể quan sát
                # Tìm vị trí của giá trị này trong trạng thái đích (goal)
                for gi in range(3):
                    for gj in range(3):
                        if goal[gi][gj] == state[i][j]:
                            goalI, goalJ = gi, gj
                            break
                # Tính khoảng cách Manhattan giữa vị trí hiện tại và vị trí mục tiêu
                distance += abs(i - goalI) + abs(j - goalJ)
    return distance

# Sinh các trạng thái kế tiếp từ trạng thái hiện tại
def getNeighbors(state):
    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Tìm vị trí của ô giá trị 0
    emptyRow, emptyCol = findEmptyTile(state)
    neighbors = []
    
    # Duyệt theo các hướng di chuyển có thể có của ô giá trị 0
    for action in directions:
        newRow = emptyRow + action[0]
        newCol = emptyCol + action[1]

        # Kiểm tra xem ô mới có nằm trong ma trận không
        if 0 <= newRow < 3 and 0 <= newCol < 3:
            # Tạo trạng thái mới
            newState = [row[:] for row in state]  
            # Hoán đổi vị trí ô trống với ô ở tọa độ mới
            newState[emptyRow][emptyCol], newState[newRow][newCol] = newState[newRow][newCol], newState[emptyRow][emptyCol]
            neighbors.append(newState)  # Thêm trạng thái mới vào danh sách
    return neighbors

# Tìm vị trí của ô giá trị 0
def findEmptyTile(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col
    return None

# Hàm tạo trạng thái quan sát một phần (Chỉ quan sát hàng đầu tiên của trạng thái hiện tại, các ô còn lại được ẩn đi (gán giá trị 0))
def partialObservation(state):
    observedState = [[0]*3 for _ in range(3)]  # Tạo ma trận 3x3 toàn giá trị 0
    for col in range(3):  # Sao chép hàng đầu tiên từ trạng thái gốc
        observedState[0][col] = state[0][col]
    return observedState

# Tìm kiếm A* với việc chỉ quan sát một phần trạng thái
def searchWithPartialObservation(start, goal):
    openList = [] # Hàng đợi ưu tiên (priority queue) để lưu trữ các trạng thái dựa trên chi phí f(n) = g(n) + h(n)
    closedList = set() # Danh sách các trạng thái đã duyệt qua
    observedStart = partialObservation(start) # Quan sát một phần trạng thái ban đầu
    
    # Thêm trạng thái bắt đầu vào hàng đợi ưu tiên với chi phí ban đầu
    heapq.heappush(openList, (0 + manhattanDistance(start, goal, observedStart), 0, start, []))
    
    while openList:
        # Lấy trạng thái có chi phí thấp nhất từ hàng đợi
        _, cost, current, path = heapq.heappop(openList)
        
        # Bỏ qua nếu trạng thái đã được duyệt
        if tuple(map(tuple, current)) in closedList:
            continue
        # Đánh dấu trạng thái hiện tại là đã duyệt
        closedList.add(tuple(map(tuple, current)))
        
        # Quan sát phần trạng thái hiện tại
        observedCurrent = partialObservation(current)
        
        # Nếu trạng thái hiện tại là trạng thái đích, trả về đường đi
        if current == goal:
            return path  
        
        # Sinh các trạng thái kế tiếp
        for neighbor in getNeighbors(current):
            if tuple(map(tuple, neighbor)) not in closedList:  # Nếu trạng thái chưa được duyệt
                newCost = cost + 1  # Tính chi phí thực tế g(n)
                newHeuristic = manhattanDistance(neighbor, goal, observedCurrent)  # Tính heuristic h(n)
                # Thêm trạng thái vào hàng đợi với chi phí f(n) = g(n) + h(n)
                heapq.heappush(openList, (newCost + newHeuristic, newCost, neighbor, path + [neighbor]))
    
    # Không tìm thấy đường đi, trả về None
    return None