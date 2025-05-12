def backtrackingWithForwardChecking(start, goal):
    # Tìm vị trí của ô giá trị 0
    def findEmptyTile(state):
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    return row, col
        return None

    def getNextPossibleStates(state):
        nextPossibleStates = []

        zeroX, zeroY = findEmptyTile(state)

        # Nếu không tìm thấy ô trống, không thể sinh trạng thái
        if zeroX is None:  
            return []
        
        # Hướng di chuyển của ô trống
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Duyệt theo các hướng di chuyển có thể có của ô giá trị 0
        for dx, dy in directions:
            newX = zeroX + dx
            newY = zeroY + dy

            # Kiểm tra xem ô mới có nằm trong ma trận không
            if 0 <= newX < 3 and 0 <= newY < 3:
                # Tạo trạng thái mới
                newState = [list(row) for row in state]
                # Hoán đổi vị trí ô trống với ô ở tọa độ mới
                newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]
                nextPossibleStates.append(newState)
        return nextPossibleStates

    # Kiểm tra tính nhất quán của trạng thái
    def isConsistent(state, goal):
        misplacedTiles = sum(1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal[i][j])
        return misplacedTiles <= 2  

    def solve8PuzzleUtil(current, path, visited):
        # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
        if current == goal:
            return path

        nextPossibleStates = getNextPossibleStates(current)
        
        for nextState in nextPossibleStates:
        
            # Chuyển trạng thái mới thành dạng tuple để lưu trữ
            stateTuple = tuple(tuple(row) for row in nextState)

            if stateTuple not in visited and isConsistent(nextState, goal):  
                visited.add(stateTuple)  # Đánh dấu trạng thái là đã duyệt
                result = solve8PuzzleUtil(nextState, path + [nextState], visited)  
                if result:  # Nếu tìm được lời giải
                    return result
                visited.remove(stateTuple)  # Nếu không thành công, bỏ đánh dấu trạng thái
        return None  # Nếu không có lời giải từ trạng thái hiện tại, quay lui
    
    # Bắt đầu tìm kiếm từ trạng thái ban đầu
    visited = set()  # Tập hợp các trạng thái đã duyệt
    visited.add(tuple(tuple(row) for row in start))  # Đánh dấu trạng thái ban đầu là đã duyệt
    return solve8PuzzleUtil(start, [], visited) # Gọi hàm hỗ trợ để bắt đầu tìm kiếm