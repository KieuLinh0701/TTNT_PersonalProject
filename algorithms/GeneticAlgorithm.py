import random
from CheckSolvable import isSolvable

def geneticAlgorithm(start, goal):
    populationSize = 50  # Số lượng cá thể trong quần thể
    generations = 500  # Số thế hệ tối đa
    mutationRate = 0.1  # Xác suất đột biến
    solutionSteps = [start]  # Danh sách lưu các trạng thái (dùng để xuất kết quả)

    def fitness(state):
        # Hàm tính điểm fitness: Số lượng ô đúng vị trí so với trạng thái đích
        return sum(state[i][j] == goal[i][j] for i in range(3) for j in range(3))

    def flatten(state):
        # Chuyển trạng thái 2D thành danh sách 1D
        return [cell for row in state for cell in row]

    def unflatten(flat):
        # Chuyển danh sách 1D thành trạng thái 2D
        return [flat[i:i+3] for i in range(0, len(flat), 3)]

    def generatePopulation():
        # Tạo quần thể ban đầu
        population = []
        while len(population) < populationSize:
            candidate = random.sample(flatGoal, len(flatGoal))  # Sinh ngẫu nhiên cá thể
            if isSolvable(unflatten(candidate)): # Kiểm tra xem cá thể có thể giải được không
                population.append(candidate)
        return population

    def crossover(parent1, parent2):
        # Lai ghép hai cá thể bằng phương pháp Order Crossover (OX)
        size = len(parent1)
        start, end = sorted(random.sample(range(size), 2)) # Chọn đoạn cắt ngẫu nhiên
        child = [None] * size # Khởi tạo cá thể con
        child[start:end + 1] = parent1[start:end + 1] # Sao chép đoạn cắt từ parent1
        remaining = [item for item in parent2 if item not in child] # Các phần tử còn lại từ parent2
        pointer = 0
        for i in range(size):
            if child[i] is None: # Điền các ô còn lại vào cá thể con
                child[i] = remaining[pointer]
                pointer += 1
        return child

    def mutate(individual):
        # Đột biến: Hoán đổi hai ô ngẫu nhiên
        idx1, idx2 = random.sample(range(len(individual)), 2) # Chọn 2 chỉ số ngẫu nhiên
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1] # Hoán đổi

    # Bắt đầu thuật toán
    flatStart = flatten(start)
    flatGoal = flatten(goal)

    # Nếu trạng thái bắt đầu đã là đích, trả về kết quả ngay
    if flatStart == flatGoal:
        return solutionSteps

    # Tạo quần thể ban đầu
    population = generatePopulation()

    for generation in range(generations):
        # Tính fitness cho từng cá thể trong quần thể
        fitnessScores = []

        for individual in population:
            score = fitness(unflatten(individual))
            fitnessScores.append((individual, score))
        
        # Sắp xếp cá thể theo điểm fitness, cá thể tốt nhất ở đầu
        fitnessScores.sort(key=lambda x: x[1], reverse=True)

        # Chọn lọc: Chọn 50% cá thể tốt nhất
        population = [individual for individual, score in fitnessScores[:populationSize // 2]]

        # Tạo thế hệ mới
        nextGeneration = []
        while len(nextGeneration) < populationSize:
            parent1, parent2 = random.sample(population, 2) # Chọn ngẫu nhiên 2 cá thể làm cha mẹ
            child = crossover(parent1, parent2)  # Lai ghép tạo con
            if random.random() < mutationRate: # Kiểm tra có đột biến không
                mutate(child)
            if child not in nextGeneration:  # Tránh trùng lặp cá thể
                nextGeneration.append(child)

        population = nextGeneration # Cập nhật quần thể với thế hệ mới

        # Kiểm tra xem có cá thể nào đạt được trạng thái đích không
        for individual in population:
            if individual == flatGoal:
                solutionSteps.append(unflatten(individual))  # Lưu lại kết quả
                return solutionSteps

        # Lưu trạng thái hiện tại tốt nhất của quần thể
        solutionSteps.append(unflatten(population[0]))

    # Trả về danh sách các trạng thái đã duyệt
    return solutionSteps