import random

# Hàm tạo trạng thái lân cận ngẫu nhiên
def getRandomNeighbor(board):
    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    
    # Tìm vị trí của ô giá trị 0
    zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if board[i][j] == 0)
    
    # Tìm các ô có thể di chuyển đến
    possibleMoves = []
    
    # Duyệt theo các hướng di chuyển có thể có của ô giá trị 0
    for dx, dy in directions:
        newX = zeroX + dx
        newY = zeroY + dy
        
        # Kiểm tra xem ô mới có nằm trong ma trận không
        if 0 <= newX < 3 and 0 <= newY < 3:
            possibleMoves.append((newX, newY))
    
    # Nếu không có vị trí nào hợp lệ, trả về None
    if not possibleMoves:
        return None

    # Chọn một vị trí ngẫu nhiên trong các nước đi hợp lệ
    nx, ny = random.choice(possibleMoves)
    
    # Tạo trạng thái mới
    newState = [row[:] for row in board]  # Sao chép bảng
    # Hoán đổi vị trí ô trống với ô ở tọa độ mới
    newState[zeroX][zeroY], newState[nx][ny] = newState[nx][ny], newState[zeroX][zeroY]
    return newState  # Trả về trạng thái mới

# Hàm tìm kiếm lời giải
def generateAndTest(start, goal, maxIterations=10000):
    # Bắt đầu từ trạng thái ban đầu
    current = start  

    # Thử tối đa maxIterations lần
    for _ in range(maxIterations):
        # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về trạng thái đó
        if current == goal:
            return [current]
        
        # Sinh trạng thái mới từ trạng thái hiện tại
        current = getRandomNeighbor(current)
        
        # Nếu không thể sinh trạng thái mới, dừng lại
        if current is None:
            return None
    
    # Sau maxIterations mà không tìm thấy trạng thái đích, trả về None
    return None