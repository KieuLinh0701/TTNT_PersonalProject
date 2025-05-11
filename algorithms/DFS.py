def dfs(start, goal):
    # Ngăn xếp để lưu các trạng thái cần kiểm tra + đường đi.
    stack = [(start, [])]
    visited = set() # Lưu các trạng thái đã thăm
    
    # Thêm trạng thái ban đầu là đã thăm
    visited.add(tuple(tuple(row) for row in start))

    # Hướng di chuyển của ô trống
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Lặp cho đến khi ngăn xếp trống.
    while len(stack) > 0:
        # Lấy trạng thái hiện tại và đường đi từ ngăn xếp.
        current, path = stack.pop()

        # Kiểm tra xem có phải trạng thái đích chưa, đúng thì trả về đường đi
        if current == goal:
            return path 

        # Tìm vị trí của ô giá trị 0
        zeroX, zeroY = next((i, j) for i in range(3) for j in range(3) if current[i][j] == 0)

        # Duyệt qua các hướng di chuyển khả thi của ô trống.
        for dx, dy in directions:
            newX = zeroX + dx
            newY = zeroY + dy

            # Kiểm tra xem vị trí mới có nằm trong phạm vi ma trận hay không.
            if 0 <= newX < 3 and 0 <= newY < 3:
                # Tạo trạng thái mới
                newState = [row[:] for row in current]
                # Hoán đổi vị trí ô trống với ô ở tọa độ mới
                newState[zeroX][zeroY], newState[newX][newY] = newState[newX][newY], newState[zeroX][zeroY]

                # Chuyển trạng thái mới thành dạng tuple để lưu trữ
                stateTuple = tuple(tuple(row) for row in newState)

                # Nếu trạng thái mới chưa được thăm, thêm vào ngăn xếp và đánh dấu đã thăm.
                if stateTuple not in visited:
                    stack.append((newState, path + [newState])) 
                    visited.add(stateTuple)  

    # Nếu không tìm thấy đường đi đến trạng thái mục tiêu, trả về None.
    return None