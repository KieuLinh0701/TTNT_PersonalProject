# Hàm tính số ô không đúng vị trí (heuristic)
def calculateMisplacedTiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def simpleHillClimbing(start, goal):
    # Bắt đầu tại trạng thái ban đầu
    current = start

    # Lưu lại các trạng thái đã đi qua
    path = []  
    visited = set()  # Lưu các trạng thái đã thăm

    # Thêm trạng thái ban đầu là đã thăm
    visited.add(tuple(tuple(row) for row in current))

    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    
    while True:
        # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
        if current == goal:
            return path

        # Tìm vị trí của ô giá trị 0
        zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if current[i][j] == 0)

        # Duyệt theo các hướng di chuyển có thể có của ô giá trị 0
        for dx, dy in directions:
            newX = zeroX + dx
            newY = zeroY + dy

            # Kiểm tra xem ô mới có nằm trong ma trận không
            if 0 <= newX < 3 and 0 <= newY < 3:
                # Tạo trạng thái mới
                newState = [row[:] for row in current]
                # Hoán đổi vị trí ô trống với ô ở tọa độ mới
                newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]

                # Chuyển trạng thái mới thành dạng tuple để lưu trữ
                stateTuple = tuple(tuple(row) for row in newState)

                # Kiểm tra xem trạng thái mới được thăm chưa, nếu chưa thêm vào hàng đợi và đánh dấu đã thăm
                if stateTuple not in visited:
                    # Tính giá trị heuristic cho trạng thái mới
                    heuristic = calculateMisplacedTiles(newState, goal)

                    # Nếu trạng thái mới có giá trị heuristic tốt hơn trạng thái hiện tại
                    if heuristic < calculateMisplacedTiles(current, goal):
                        current = newState # Cập nhật trạng thái hiện tại thành trạng thái mới
                        path.append(current) # Thêm trạng thái mới vào đường đi
                        visited.add(stateTuple) # Đánh dấu trạng thái mới là đã thăm
                        break # Thoát khỏi vòng lặp lân cận để tiếp tục tìm kiếm
        else:
            return None # Nếu duyệt hết lân cận mà không tìm thấy trạng thái tốt hơn, dừng thuật toán