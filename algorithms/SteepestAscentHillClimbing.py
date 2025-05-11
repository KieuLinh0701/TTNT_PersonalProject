# Hàm tính số ô không đúng vị trí (heuristic)
def calculateMisplacedTiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def steepestAscentHillClimbing(start, goal):
    # Bắt đầu từ trạng thái ban đầu
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

        neighbors = []  # Lưu các trạng thái lân cận

        # Duyệt tất cả các lân cận có thể
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

                # Kiểm tra xem trạng thái mới được thăm chưa
                if stateTuple not in visited:
                    # Tính giá trị heuristic cho trạng thái mới
                    heuristic = calculateMisplacedTiles(newState, goal)
                    neighbors.append((newState, heuristic))  # Lưu trạng thái và giá trị heuristic

        # Nếu không có trạng thái lân cận khả thi, trả về None
        if not neighbors:
            return None

        # Sắp xếp các trạng thái lân cận theo giá trị heuristic tăng dần
        neighbors.sort(key=lambda x: x[1])

        # Chọn trạng thái có giá trị heuristic nhỏ nhất (tốt nhất)
        bestNeighbor = neighbors[0]

        # Nếu trạng thái tốt nhất không tốt hơn trạng thái hiện tại, kết thúc thuật toán
        currentHeuristic = calculateMisplacedTiles(current, goal)
        if currentHeuristic <= bestNeighbor[1]:
            return None

        # Cập nhật trạng thái hiện tại thành trạng thái tốt nhất
        current = bestNeighbor[0]
        path.append(current)  # Thêm trạng thái mới vào đường đi
        visited.add(tuple(tuple(row) for row in current))  # Đánh dấu trạng thái mới là đã thăm